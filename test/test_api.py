import allure


@allure.feature("API тесты для функционала корзины.")
@allure.title("Тест на добавление товара в корзину.")
@allure.description("Добавляем количество товаров согласно переданному значению.")
@allure.id(1)
@allure.severity("Blocker")
def test_add_product_to_cart_from_preview(api):
    amount = "10"
    result_add_product, status_code = api.add_product_to_cart_from_preview(amount)
    with allure.step(
        "Проверяем, что статус код, ключи ответа в JSONе соответствуют успешной операции."
    ):
        assert status_code == 200
        assert result_add_product["status"] == "ok"
        assert result_add_product["btn_text"] == "Добавлено"
        assert result_add_product["sum_quantity"] == amount
    api.delete_product_from_cart()


@allure.feature("API тесты для функционала корзины.")
@allure.title("Тест на удаление товара из корзины.")
@allure.description(
    "Добавляем количество товаров, затем удаляем категорию товара из корзины, проверяем, что корзина пуста."
)
@allure.id(2)
@allure.severity("Blocker")
def test_delete_product_from_cart(api):
    amount = "10"
    result_add_product, status_code = api.add_product_to_cart_from_preview(amount)
    with allure.step(
        "Проверяем, что статус код, ключи ответа в JSONе соответствуют успешной операции."
    ):
        assert status_code == 200
        assert result_add_product["status"] == "ok"
        assert result_add_product["btn_text"] == "Добавлено"
    amount_before_delete = result_add_product["sum_quantity"]
    result_delete_product, _ = api.delete_product_from_cart()
    amount_after_delete = result_delete_product["sum_quantity"]
    with allure.step("Проверяем, что категория товара была удалена из корзины."):
        assert _ == 200
        assert result_delete_product["status"] == "ok"
        assert result_delete_product["sum_quantity"] == "0"
        assert int(amount_before_delete) > int(amount_after_delete)
