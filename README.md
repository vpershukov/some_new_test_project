Шаблон автотестов REST API справочного сервиса. Проверяется эндпоинт `POST /api/v1/dict` — получение данных справочника за период.

Это не полный набор проверок, а иллюстрация структуры автотестов к ручным тест-кейсам. В описании задачи не указан адрес веб-сервиса, поэтому в качестве BASE_URL — заглушка (storage/urls.py). HTTP-коды ответа 200/400 и поведение без limit — принятые допущения, потому что в исходном описании это не зафиксировано.

Стек: Python, pytest, requests, Allure.

## Структура

```
clients/rest/          HTTP-клиент, валидации, методы сервиса
  base_http.py         отправка запросов и логирование в Allure
  base_validation.py   проверки кода ответа и сортировки
  references_service.py  метод retrieve_reference_data
storage/urls.py        базовый URL и пути эндпоинтов
tests/rest/            тест-кейсы
pytest.ini             pythonpath и маркеры pytest
requirements.txt       зависимости Python
```

## Настройка

1. Укажите `BASE_URL` в `storage/urls.py` (сейчас там заглушка).
2. Установите зависимости:

```bash
pip install -r requirements.txt
```

Для отчётов Allure нужен [Allure Commandline](https://allurereport.org/docs/install/).

Форматирование кода:

```bash
black .
```

## Запуск

Все тесты:

```bash
pytest
```

Только тесты справочника (`POST /api/v1/dict`):

```bash
pytest -m post_api_v1_dict
```

С отчётом Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Что покрыто

| ID  | Сценарий                                                         |
|-----|------------------------------------------------------------------|
| TC1 | Данные за корректный период, код 200                             |
| TC2 | Сортировка по `name` по возрастанию (`ASC`)                      |
| TC3 | Сортировка по `name` по убыванию (`DESC`)                        |
| TC4 | Параметр `limit=10`, в `data` не больше 10 элементов             |
| TC5 | Невалидный `start_date`, ожидается код 400                       |
| TC6 | Запрос без `limit`: код 200, в `data` не больше 50 элементов     |
