from clients.rest.base_http import send_request
from storage.urls import ReferenceUrls


def retrieve_reference_data(start_date, finish_date, limit=50, **kwargs):
    """Функция отправляет запрос данных справочника за указанный период"""
    request_body = {"start_date": start_date, "finish_date": finish_date}
    query_params = {"limit": limit, **kwargs}

    return send_request(
        method="POST",
        resource_url=ReferenceUrls.DICT_URL,
        json=request_body,
        params=query_params,
    )
