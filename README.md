# Recipes Browser

Веб-сайт-книга рецептов.

Неавторизованные пользователи:
- Могут просматривать рецепты.

Авторизованные пользователи:
- Могут просматривать рецепты в общем каталоге.
- Могут просматривать аккаунты других пользоватлей.
- Могут добавлять рецепты.
- - Публичные.
- - Приватные - не видны ни в общем каталоге, ни в аккаунте пользователя.

## Используемые технологии
Для реализации системы используется следующий стек технологий:

- Язык Python
- Микро-фреймворк Flask
- БД SQLite
- SQLAlchemy ORM

## Установка и запуск

Стабильной версией python'а для этого проекта является 3.9.16.

Linux:

```
mkdir recipes_browser
cd recipes_browser
git clone https://github.com/myrzh/recipes_browser .
py -3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python flask_app/run.py
```
