[![en](https://img.shields.io/badge/lang-en-red.svg)](README.en.md)

# API торговой площадки
Демо API торговой площадки с использованием Django Rest Framework и PostgreSQL.

![Static Badge](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Static Badge](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/HTML-e34c26?style=flat&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS-563d7c?&style=flat&logo=css3&logoColor=white)

# Возможности
- PostgreSQL: масштабируемая реляционная база данных
- Django: полнофункциональный, легко расширяемый веб-фреймворк с панелью администратора и панелью инструментов отладки
- Django Rest Framework: эффективный RESTful API с представлениями на основе классов
- Аутентификация JWT: безопасная аутентификация с использованием JSON Web Tokens с Djoser
- Docker: контейнеры для разработки, тестирования и продакшн
- PyTest: набор тестов для основных функций
- Locust: нагрузочное тестирование
- Silk: профилирование производительности
- Waitress: сервер WSGI для продакшн

# Планируемые функции
- Celery: асинхронная очередь задач
- Расширенная документация API
- Фронтенд: React.js
- Развертывание проекта.

# Структура репозитория

```
.
├── .devcontainer                       # Настройки контейнеров для VSCode
├── .vscode                             # VSCode настройки
├── apps                                # Django приложения
│   ├── core                            # Общяя логика для разных приложений
│   │   ├── management                  # Команды Django
│   │   │   ├── commands                # -=- 
│   │   │   │   └── seed_db.py          # Скрипт популяции базы данных
│   │   │   └── seed_db.sql             # SQL скрипт и инкремент индекса PostgreSQL
│   ├── likes                           # Система лайков
│   ├── playground                      # Экспериментальные функции (почта и т.п.)
│   ├── store                           # Основные функции управления магазином
│   └── tags                            # Система тэгов для товаров
├── locustfiles                         # Скрипты нагрузочного тестирования
├── storefront                          # Основные настройки и тесты проекта
│   ├── settings                        # ❗🔧 Настройки проекта
│   │   │   ├── common.py               # Общие настройки для разработки, тестов и продакшн
│   │   │   ├── dev.py                  # Настройки для разработки
│   │   │   ├── prod.py                 # Настройки для продакшн
│   │   │   ├── secret_key_generator.py # Скрипт для генерации ключа Django
│   │   │   └── test.py                 # PyTest основные настройки
│   └── tests                           # PyTest тесты
├── .env.example                        # Пример файла переменных окружения
├── docker-compose.yml                  # Конфигурация Docker compose
├── docker-entrypoint.sh                # Скрипт точки входа для Docker
├── Dockerfile                          # Основные инструкции Docker
├── manage.py                           # Управление проектом Django
├── Pipfile                             # Pipenv файл зависимостей проекта
├── Pipfile.lock                        # Pipenv файл зависимостей проекта
├── pytest.ini                          # PyTest - настройки
├── README.en.md                        # Документация Англ.
├── README.ru.md                        # Документация Русс.
├── server.py                           # Waitress WSGI сервер для продакшн
└── wait-for-it.sh                      # Bash скрипт для Docker
```

# Установка
## Клонируйте репозиторий
`git clone https://github.com/mrBrain101/Storefront_Django_PostgreSql.git`

## Установите переменные окружения
- Измените имя файла `.env.example` на `.env`.
- Как минимум, установите переменную окружения `DJANGO_SECRET_KEY` в файле `.env`.<br>
Вы можете сгенерировать секретный ключ с помощью скрипта `storefront/settings/secret_key_generator.py` или на сайте [Djecrety](https://djecrety.ir/).
- Для разработки установите переменную окружения `DEBUG` в значение `True`.<br>

## Запуск проекта

### С Docker
- При необходимости установите [Docker](https://www.docker.com/get-started).
- Не запускайте все профили одновременно.<br>
- Опционально можно заполнить базу данных фиктивными данными о товарах и категориях, установив `POPULATE_DB` в значение `True` в `.env`.<br>
- Каждую службу можно запустить отдельно:
    - установив соответствующие переменные в `.env`;<br>
    - используя команду `docker compose --profile <service_name> up --build`.<br>
- Для общей разработки:<br>
    - установите `DEBUG=True` в `.env`;<br>
    - выполните `docker compose up --build`
- Для разработки с тестированием:<br>
    - опционально установите `TEST_METHOD` в `.env` (варианты: `pytest` и `ptw`);<br>
    - выполните `docker compose --profile test up --build`.
- Для разработки с использованием [профилирования Silk](https://silk.readthedocs.io/en/latest/), [нагрузочного тестирования Locust](https://locust.io/), [имитации SMTP-сервера](https://github.com/rnwood/smtp4dev) и тестирования PyTest:<br>
    - опционально установите `TEST_METHOD` в `.env` (возможны варианты `pytest` и `ptw`);<br>
    - установите `SILK_PROFILING=True` в `.env`;<br>
    - установите `LOAD_TESTING=True` в `.env`;<br>
    - выполните `docker compose --profile dev up --build`.
- Для запуска production с Waitress:<br>
    - установите `DEBUG=False` в `.env`;<br>
    - выполните `docker compose --profile production up --build`.

### Вручную
#### Установка Pipenv
В каталоге проекта выполните:
`pip install pipenv`
#### Установка зависимостей
`pipenv install`
#### Активация локальной среды
`pipenv shell` / `source venv/bin/activate`
#### Работа
- Опционально можно заполнить базу данных фиктивными данными о товарах и категориях с помощью скрипта `apps\core\management\commands\seed_db.py`:
`python manage.py seed_db`
- Тесты можно запустить с помощью PyTest:<br>
    - `pytest` для однократного запуска тестов,<br>
    - `ptw` для запуска тестов в режиме наблюдения.
- Сервер разработки можно запустить:<br>
    - `python manage.py runserver`
- Сервер продакшн можно запустить с помощью Waitress:<br>
    - `python server.py`

## Доступные конечные точки API:

### Аутентификация
| Описание/область действия | Конечная точка | Доступные действия CRUD |
|:--|:--|:--|
| Регистрация нового пользователя | /auth/users/ | POST |
| Создание токена регистрации | /auth/jwt/create/ | POST |
| Получение токена обновления | /auth/jwt/refresh/ | POST |

## Товары
| Описание/область действия | Конечная точка | Доступные действия CRUD |
|:--|:--|:--|
| Все товары | /store/products/ | GET / POST |
| Конкретный товар | /store/products/{id}/ | GET / PUT / DELETE|

## Коллекции
| Описание/область действия | Конечная точка | Доступные действия CRUD |
|:--|:--|:--|
| Список коллекций | /store/collections/ | GET / POST |
| конкретная коллекция | /store/collections/{id}/ | GET / PUT / DELETE|

### Заказы
| Описание/область действия | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Список заказов | /store/orders/ | GET / POST |
| Конечный заказ | /store/orders/{id}/ | GET / PUT / DELETE|

### Корзины
| Описание/область действия | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Список корзин | /store/carts/ | GET / POST |
| конкретная корзина | /store/carts/{id}/ | GET / PUT / DELETE|

### Клиенты
| Описание/область действия | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Список клиентов | /store/customers/ | GET |
| Конкретный клиент | /store/customers/{id}/ | GET |

# Благодарность
Спасибо Мошу Хамедани за [полный курс по Django Rest Framework] (codewithmosh.com/p/the-ultimate-django-series).

# Лицензия
Лицензия не требуется. Вы можете использовать этот код по своему усмотрению.

## Доступные конечные точки API:

### Аутентификация
| Описание/область | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Регистрация пользователя | /auth/users/ | POST |
| Создание регистрационного токена | /auth/jwt/create/ | POST |
| Создание токена обновления | /auth/jwt/refresh/ | POST |
     
### Товары
| Описание/область | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Вывести все товары | /store/products/ | GET |
| Создать товар | /store/products/ | POST |
| Конкретный товар | /store/products/{id}/ | GET / PUT / DELETE|
     
### Категории
| Описание/область | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Вывести все категории | /store/collections/ | GET |
| Конкретная категория | /store/products/{id}/ | GET / DELETE|

### Заказы
| Описание/область | Конечная точка | Доступные CRUD-действия |
|:--|:--|:--|
| Вывести все заказы | /store/orders/ | GET / POST |
| Кокретный заказ | /store/orders/{id}/ | GET / PUT / DELETE|

### Carts
| Описание/область | Конечная точка  | Доступные CRUD-действия |
|:--|:--|:--|
| Вывести корзины | /store/carts/ | GET / POST |
| Конкретныя корзина | /store/carts/{id}/ | GET / PUT / DELETE|

### Клиент
| Описание/область | Конечная точка  | Доступные CRUD-действия |
|:--|:--|:--|
| Вывести клиентов | /store/customers/ | GET |
| Кокретный клиент | /store/customers/{id}/ | GET |

# Лицензия
Лицензии и гарантий нет: используйте код по своему усмотрению без какой-либо поддержки с моей стороны.