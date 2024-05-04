from locators.Order_page_locators import OrderPage1Locators, OrderPage2Locators
import allure
import pytest
from pages.Home_page import HomePageScooter
import data
from pages.Order_page import OrderPage1, OrderPage2


class TestOrderPage:
    @allure.description('Заполнение 1 страницы заказа')
    def test_order_page_1(self, driver):
        login_page = OrderPage1(driver)
        login_page.set_order_page_1(data.Urls.ORDER_PAGE,
                                    data.Order_data.NAME[1], data.Order_data.FAMILY[1], data.Order_data.ADDRESS[1],
                                    data.Order_data.TELEPHONE[1], OrderPage1Locators.station_metro_2)

        title1 = driver.find_element(*OrderPage1Locators.title_order_page_1)
        assert title1.is_displayed()

    @allure.description('Заполнение 2 страницы заказа')
    @pytest.mark.parametrize('data_calendar, rental_period, color, comment',
                             [
                                 (OrderPage2Locators.calendar_1_may, OrderPage2Locators.list_rental_period_1_sutki,
                                  OrderPage2Locators.color_scooter_black, data.Order_data.COMMENT_CURRIER[0]),
                                 (OrderPage2Locators.calendar_2_may, OrderPage2Locators.list_rental_period_6_sutki,
                                  OrderPage2Locators.color_scooter_grey, data.Order_data.COMMENT_CURRIER[1])
                             ])
    def test_order_page_2(self, driver, data_calendar, rental_period, color, comment):
        login_page = OrderPage2(driver)
        login_page.set_order_page_1(data.Urls.ORDER_PAGE, data.Order_data.NAME[0], data.Order_data.FAMILY[0],
                                    data.Order_data.ADDRESS[0], data.Order_data.TELEPHONE[0],
                                    OrderPage1Locators.station_metro_1)
        login_page.set_order_page_2(data_calendar, rental_period, color, comment)
        login_page.open_window_confirm()
        title_succes_order = driver.find_element(*OrderPage2Locators.title_succes_order)
        assert title_succes_order.is_displayed() and "Заказ оформлен" in title_succes_order.text

    @allure.description('Редирект с страницы заказа на главную по нажатию на иконку самоката')
    def test_redirect_home_page(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page_click_cookie(data.Urls.ORDER_PAGE)
        login_page.click_logo_scooter()
        current_url = driver.current_url
        assert current_url == data.Urls.HOME_PAGE

    @allure.description('Редирект с страницы заказа на страницу "Яндекс Дзен" по нажатию на иконку яндекс')
    def test_redirect_ya_dzen(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page_click_cookie(data.Urls.ORDER_PAGE)
        login_page.open_new_tub_dzen(driver)
        title_dzen = driver.title
        assert title_dzen == 'Дзен'
