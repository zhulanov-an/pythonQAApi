# pythonQAApi

Реализация в отдельном модуле (файле) тестовой функции, которая принимает 2 параметра:
- url - значение по-умолчанию https://ya.ru
- status_code - значение по-умолчанию 200

Параметры реализованы через pytest.addoption

пример запуска: 
`pytest test_module.py --url=https://mail.ru --status_code=200`
