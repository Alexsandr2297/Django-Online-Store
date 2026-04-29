# Django-Online-Store
Проект интернет-магазина с использованием фреймворка Django для веб-приложений на Python.
## Технологии

- **Python** 3.12
- **Django** 6.0.3
- **Bootstrap** (для стилизации)
- **PostgreSQL** (база данных)
- **Poetry** (управление зависимостями)

##  Структура проекта
Django-Online-Store/
├── catalog/ # Основное приложение магазина
│ ├── migrations/ # Миграции базы данных
│ ├── templates/ # HTML-шаблоны
│ │ ├── home.html # Главная страница (каталог)
│ │ └── contact.html # Страница контактов
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── config/ # Настройки проекта
│ ├── settings.py # Основные настройки Django
│ ├── urls.py # Главные URL-маршруты
│ └── wsgi.py
├── static/ # Статические файлы
│ ├── css/ # Стили (Bootstrap)
│ │ └── bootstrap.min.css
│ └── js/ # JavaScript-скрипты
│ └── script.js
├── venv/ # Виртуальное окружение
├── .gitignore # Игнорируемые файлы для Git
├── db.sqlite3 # База данных SQLite
├── manage.py # Управляющий скрипт Django
├── poetry.lock # Фиксация версий зависимостей
└── pyproject.toml # Конфигурация Poetry

text

##  Установка и запуск
после запуска сервера нужно прописать в сторке поиска /blog/ чтобы перейти во второе приложение Blog

### 1. Клонирование репозитория

```bash
git clone https://github.com/Alexsandr2297/Django-Online-Store.git
cd Django-Online-Store
