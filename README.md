# Бекэнд сервер для интернет-платформы.
В этом проекте к сожалению статус “Просмотрено”/”Не просмотрено” не фиксируется, а считается налету и доступы пользователей к продуктам есть, но в отдельные сущности не вынесены
### Инструкция по запуску бекэнд-сервера: ### 
  1. Склонируем репозиторий нашего сервера и зайдём в репозиторий:
  ```
  git clone https://github.com/NoRIS95/task_Hard_Qode
  cd task_Hard_Qode
  ```
  2. Создаём виртуальное окружение и устанавливаем зависимости:
  ```
  python3 -m venv env
  . ./env/bin/activate
  cd coursesshop
  pip install -r requirements.txt
  ```
  3. Применяем миграции.
  ```
  python manage.py makemigrations 
  python manage.py migrate
  ```
  4. Создаем суперпользователя для управления административной панелью.
  ```
  python manage.py createsuperuser
  ```
  5. Запускаем сервер.
  ```
  python manage.py runserver
  ```
