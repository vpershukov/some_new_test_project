import requests
import allure
import curlify


def send_request(method, resource_url, **kwargs):
    """
    Базовый метод для работы с http-запросами:
    - Отправляет http-request
    - Логирует данные запроса и ответа
    - Возвращает объект http-response
    """
    response = requests.request(
        method, resource_url, verify=False, timeout=120, **kwargs
    )
    if not isinstance(response.request.body, bytes):
        allure.attach(
            curlify.to_curl(response.request),
            "REQUEST",
            allure.attachment_type.TEXT,
        ),
    allure.attach(
        str(response.status_code), "RESPONSE CODE", allure.attachment_type.TEXT
    )
    allure.attach(response.content, "RESPONSE", allure.attachment_type.JSON)

    return response
