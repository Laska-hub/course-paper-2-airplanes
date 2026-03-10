- Aeroplanes API Project:

Программа для получения информации о самолетах, находящихся в воздушном пространстве выбранной страны.
Данные берутся из API:
OpenStreetMap Nominatim — получение координат страны
OpenSky Network — получение информации о самолетах
Программа позволяет:
получить самолеты в воздушном пространстве страны
сохранить данные в JSON-файл
фильтровать самолеты по стране регистрации
получить топ N самолетов по высоте
фильтровать самолеты по диапазону высот
Проект реализован с использованием принципов ООП и SOLID.

- Структура проекта:

aeroplane_project/
│
├── 
│   ├── api_adapter.py
│   └── aeroplanes_api.py
│
├── models/
│   └── aeroplane.py
│
├── storage/
│   ├── file_adapter.py
│   └── json_saver.py
│
├── utils/
│   └── helpers.py
│
├── tests/
│   └── test_aeroplanes.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Установка:
1. Клонировать репозиторий
git clone https://github.com/your-username/aeroplane_project.git
cd aeroplane_project
2. Создать виртуальное окружение
python -m venv venv
Linux / Mac:
source venv/bin/activate
Windows:
venv\Scripts\activate
3. Установить зависимости
pip install -r requirements.txt
▶️ Запуск программы
python main.py

Пример работы программы:

Введите название страны: Spain
Введите количество самолетов для топ N: 5
Фильтр по странам (через пробел): Spain France
Диапазон высот (min max): 5000 15000

После этого программа выведет самолеты, подходящие под условия.

🧪 Запуск тестов: pytest -v tests/
Тесты написаны с использованием pytest.
pytest
Покрытие тестами: >70% функционального кода.======== 5 passed in 0.01s ======

- Проверка качества кода
Проверка типизации
mypy .
Проверка PEP8
flake8 .
Форматирование кода
black .
Сортировка импортов
isort .

- Используемые технологии

Python 3.10+
requests
pytest
mypy
flake8
black
isort

🌐 Используемые API
OpenStreetMap Nominatim

Получение координат страны.

Документация:
https://nominatim.org/release-docs/develop/api/Search
OpenSky Network API
Получение данных о самолетах.

Документация:
https://opensky-network.org/apidoc/rest.html

- Возможности проекта

✔ Работа с внешними API
✔ ООП архитектура
✔ Абстрактные классы
✔ Сохранение данных в JSON
✔ Фильтрация и сортировка данных
✔ Консольный интерфейс
✔ Покрытие тестами

- Пример объекта самолета
UAL1621 (United States) — 10203м, 268.79м/с

Где:

callsign — позывной самолета
country — страна регистрации
velocity — скорость полета
altitude — высота полета

- Лицензия

Проект создан в учебных целях.
