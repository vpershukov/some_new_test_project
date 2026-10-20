from clients.rest.references_service import retrieve_reference_data
from clients.rest.base_validation import check_response_code, check_dicts_are_sorted_by_key
import pytest
import allure


@pytest.mark.post_api_v1_dict
@allure.feature("POST /api/v1/dict")
class TestPostApiV1Dict:
    @allure.testcase("TC1")
    @allure.title("Получение данных за корректный период")
    def test_post_valid_period(self):
        with allure.step(
                "Шаг: Отправить запрос с start_date='2026-07-30' и finish_date='2026-10-19'"
        ):
            response = retrieve_reference_data(start_date="2026-07-30", finish_date="2026-10-19")
        with allure.step("Проверка: код ответа = 201"):
            check_response_code(response, 201)

    @allure.testcase("TC2")
    @allure.testcase("TC3")
    @allure.title("Сортировка данных по полю 'name'")
    @pytest.mark.parametrize("sort, reverse", [("asc", False), ("desc", True)])
    def test_post_sort_by_name(self, sort, reverse):
        with allure.step(
                "Шаг: Отправить запрос с start_date='2026-07-30' и finish_date='2026-10-19', "
                "а также параметроми orderBy и orderDir"
        ):
            response = retrieve_reference_data(
                start_date="2026-07-30",
                finish_date="2026-10-19",
                orderBy="name",
                orderDir=sort,
            )
        with allure.step("Проверка: код ответа = 201"):
            check_response_code(response, 201)
        with allure.step("Проверка: сортировка выполнена успешно"):
            check_dicts_are_sorted_by_key(response.json(), key="name", reverse=reverse)
