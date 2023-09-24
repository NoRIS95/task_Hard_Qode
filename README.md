# Бекэнд сервер для интернет-платформы.
## В этом проекте к сожалению статус “Просмотрено”/”Не просмотрено” не фиксируется, а считается налету и доступы пользователей к продуктам есть, но в отдельные сущности не вынесены
### Инструкция по запуску бекэнд-сервера: ### 
  1.Склонируем репозиторий нашего сайта и зайдём в в репозиторий:
  ```
  git clone https://github.com/NoRIS95/task_Hard_Qode
  cd task_Hard_Qode
  ```
  2. Создаём виртуальное окружение, указав нужную версию Python и устанавливаем зависимости:
  ```
  python3 -m venv env
  . ./env/bin/activate
  cd coursesshop
  pip install -r requirements.txt
  ```
  3. Заходим в директорию, где лежит файл `manage.py` и применяем миграции.
  ```
  python manage.py makemigrations 
  python manage.py migrate
  ```
  4. Создаем суперпользователя.
  ```
  python manage.py createsuperuser
  ```
  5. Запускаем сервер.
  ```
  python manage.py runserver
  ```
