import allure
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_ui = config.get("base_url_ui")

@allure.feature("UI тесты для функционала корзины.")
@allure.title("Тест на поиск товара и добавление его в корзину.")
@allure.description(
    "Выполняем поиск товара согласно полученным данным, проверяем, что товар был добавлен в корзину."
)
@allure.id(1)
@allure.severity("Blocker")
def test_search_product(main_page, cart_page):
    product_name = "Мумиё алтайское 50гр"
    main_page.search_product_by_search_field(product_name)
    product_name_added_to_cart = main_page.add_product_to_cart(product_name)
    with allure.step(
        "Проверяем, что переданное название товара совпадает с названием товара, который мы добавили в корзину."
    ):
        assert product_name_added_to_cart == product_name
    main_page.go_to_cart()
    result_to_add = cart_page.find_product_in_cart(product_name)
    with allure.step("Проверяем, что товар действительно находится в корзине."):
        assert result_to_add is True


@allure.feature("UI тесты для функционала корзины.")
@allure.title("Тест на удаление товара из корзины.")
@allure.description(
    "Выполняем поиск товара согласно полученным данным, переходим в корзину, удаляем товар, проверяем, что товар был удален."
)
@allure.id(2)
@allure.severity("Blocker")
def test_delete_product_from_cart(main_page, cart_page):
    product_name = "Мумиё алтайское 50гр"
    main_page.search_product_by_search_field(product_name)
    product_name_added_to_cart = main_page.add_product_to_cart(product_name)
    with allure.step(
        "Проверяем, что переданное название товара совпадает с названием товара, который мы добавили в корзину."
    ):
        assert product_name_added_to_cart == product_name
    main_page.go_to_cart()
    result_to_delete = cart_page.delete_product_in_cart(product_name)
    with allure.step("Проверяем, что товар действительно отсутствует в корзине."):
        assert result_to_delete is True
