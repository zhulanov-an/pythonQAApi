# pythonQAApi

1. Реализованы следующие тесты АПИ сервиса https://dog.ceo/api :
- test_list_breeds - тест списка пород
- test_random_subbreed - проверка апи получения случайного изображения подвида породы 
- test_schema_images_by_breed - проверка схемы ответа по породе
- test_unique_name_image_by_random_collection - сравнивается уникальность изображений по ссылкам на изображение.
- test_random_image_by_online_breed - проверка получения случайного изображения по породам.
  Получение списка пород происходит автоматически перед запуском теста.

2. Тесты для REST API сервиса: https://www.openbrewerydb.org/
с использованием параметризации

- test_schema_list_of_breweries - проверка схемы списка 
- test_get_id_of_a_single_brewery - проверка id элемента при поиске по id
- test_search_for_breweries_based_on_a_search_term - проверка поиска
- test_autocomplete - проверка происка
- test_filter_by_postal - проверка фильтрации по почтовому коду

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
