"""
Файл содержит функции-помощники для валидации данных
"""


def check_response_code(response, expected_code):
    """Проверяет совпадение http-кода ответа с ожидаемым кодом, логирует данные запроса и ответа"""
    assert response.status_code == expected_code, (
        f"Ожидаемый код ответа равен {expected_code}, вместо него вернулся код {response.status_code}.\n"
        f"Request Method: {response.request.method}\n"
        f"Request URL: {response.request.url}\n"
        f"Request Body: {response.request.body}\n"
        f"Response Text: {response.text}\n"
    )


def check_value_in_dicts(items, key, value, comment="Assert-комментарий"):
    """
    Проверяет, что значение по ключу в каждом словаре совпадает с выбранным условием
    """
    for item in items:
        assert item[key] == value, comment


def check_dicts_are_sorted_by_key(
    items: list, key: str, reverse=False, comment="Assert-комментарий"
):
    """Проверяет, что список словарей items отсортирован по указанному ключу key"""
    assert items == sorted(items, key=lambda item: item[key], reverse=reverse), comment
