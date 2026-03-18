from typing import Any, List
from unittest.mock import patch

import pytest

import main
from aeroplane_project import api_adapter
from aeroplane_project.models.aeroplane import Aeroplane
from aeroplane_project.processing import process_planes


# -----------------------------
# API ADAPTER TESTS
# -----------------------------
def test_api_adapter_returns_data() -> None:
    fake_data = {"states": [[1, 2, 3]]}

    with patch("aeroplane_project.api_adapter.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_data

        result = api_adapter.get_raw_data("https://example.com")
        assert result == fake_data["states"]


def test_api_adapter_raises() -> None:
    with patch("aeroplane_project.api_adapter.requests.get") as mock_get:
        mock_get.side_effect = Exception("Ошибка соединения")

        with pytest.raises(RuntimeError):
            api_adapter.get_raw_data("https://example.com")


# -----------------------------
# MAIN TESTS
# -----------------------------
def test_main_handles_api_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        api_adapter,
        "get_raw_data",
        lambda url: (_ for _ in ()).throw(RuntimeError("Ошибка API")),
    )
    monkeypatch.setattr("builtins.input", lambda prompt="": "US")

    with pytest.raises(SystemExit):
        main.main()


def test_main_with_data(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    raw_data: List[List[Any]] = [
        ["icao1", "A", "US", None, None, 0, 0, 1500, None, 250, None, None],
        ["icao2", "B", "FR", None, None, 0, 0, 5000, None, 300, None, None],
    ]

    monkeypatch.setattr(api_adapter, "get_raw_data", lambda url: raw_data)

    inputs = iter(["US", "1", "US", "1000 2000"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    def fake_process_planes(*args: Any, **kwargs: Any) -> List[Aeroplane]:
        return [
            Aeroplane("A", "US", 1500, 250),
            Aeroplane("B", "FR", 5000, 300),
        ]

    monkeypatch.setattr(main, "process_planes", fake_process_planes)

    main.main()
    captured = capsys.readouterr()

    assert "A" in captured.out


def test_main_no_matching_planes(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    raw_data: List[List[Any]] = [
        ["icao1", "A", "US", None, None, 0, 0, 1500, None, 250, None, None],
    ]

    monkeypatch.setattr(api_adapter, "get_raw_data", lambda url: raw_data)

    inputs = iter(["FR", "1", "FR", "0 1000"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    def empty_process(*args: Any, **kwargs: Any) -> List[Aeroplane]:
        return []

    monkeypatch.setattr(main, "process_planes", empty_process)

    main.main()
    captured = capsys.readouterr()

    assert "нет самолетов" in captured.out.lower()


# -----------------------------
# PROCESSING TESTS
# -----------------------------
def test_process_planes_filters_correctly() -> None:
    raw_data: List[List[Any]] = [
        ["icao1", "A", "US", None, None, 0, 0, 1500, None, 250, None, None],
        ["icao2", "B", "FR", None, None, 0, 0, 5000, None, 300, None, None],
    ]

    result = process_planes(
        raw_data=raw_data,
        countries=["US"],
        alt_min=1000,
        alt_max=2000,
        top_n=10,
    )

    assert len(result) == 1
    assert result[0].callsign == "A"


def test_process_planes_empty_result() -> None:
    raw_data: List[List[Any]] = [
        ["icao1", "A", "US", None, None, 0, 0, 1500, None, 250, None, None],
    ]

    result = process_planes(
        raw_data=raw_data,
        countries=["FR"],
        alt_min=0,
        alt_max=1000,
        top_n=10,
    )

    assert result == []


def test_process_planes_top_n_limit() -> None:
    raw_data: List[List[Any]] = [
        ["icao1", "A", "US", None, None, 0, 0, 1500, None, 250, None, None],
        ["icao2", "B", "US", None, None, 0, 0, 1600, None, 260, None, None],
    ]

    result = process_planes(
        raw_data=raw_data,
        countries=["US"],
        alt_min=1000,
        alt_max=2000,
        top_n=1,
    )

    assert len(result) == 1
