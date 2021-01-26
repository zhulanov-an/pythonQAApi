# pythonQAApi

3. Тестирование REST сервиса 3.
Написано 5 тестов для REST API сервиса: https://jsonplaceholder.typicode.com/
с параметризацией

- test_get_posts_by_id - проверка статьи по id
- test_get_users_by_id - проверка пользователя по id
- test_get_todos_by_id - проверка дела по id
- test_posts_schema - проверка списка статей на схему
- test_todos_schema - проверка списка дел на схему


4. Реализация в отдельном модуле (файле) тестовой функции, которая принимает 2 параметра:
- url - значение по-умолчанию https://ya.ru
- status_code - значение по-умолчанию 200

Параметры реализованы через pytest.addoption

пример запуска: 
`pytest --url=https://mail.ru --status_code=200`
