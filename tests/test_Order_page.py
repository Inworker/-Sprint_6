import allure
import pytest
from pages.Base_page import BasePage
from pages.Home_page import HomePageScooter
import data
from pages.Order_page import OrderPage1, OrderPage2
from conftest import driver

class TestOrderPage:
    @allure.description('Заполнение 1 страницы заказа')
    def test_order_page_1(self, driver):
        login_page = OrderPage1(driver)
        login_page.open_page(data.Urls.ORDER_PAGE)
        login_page.click_cookie()

        login_page.enter_data_field_name(data.Order_data.NAME[1])
        login_page.enter_data_field_family(data.Order_data.FAMILY[1])
        login_page.enter_data_field_address(data.Order_data.ADDRESS[1])
        login_page.enter_data_field_telephone(data.Order_data.TELEPHONE[1])

        login_page.click_field_metro()
        login_page.set_station_metro(OrderPage1.station_metro_2)
        login_page .click_button_next()

        title1 = driver.find_element(*OrderPage1.title_order_page_1)
        assert title1.is_displayed()


    @allure.description('Заполнение 2 страницы заказа')
    @pytest.mark.parametrize('data_calendar, rental_period, color, comment',
                             [
                                 (OrderPage2.calendar_1_may, OrderPage2.list_rental_period_1_sutki, OrderPage2.color_scooter_black, data.Order_data.COMMENT_CURRIER[0]),
                                 (OrderPage2.calendar_2_may, OrderPage2.list_rental_period_6_sutki, OrderPage2.color_scooter_grey, data.Order_data.COMMENT_CURRIER[1])
                             ])
    def test_order_page_2(self, driver, data_calendar, rental_period, color, comment):
        login_page = OrderPage2(driver)
        login_page.set_order_page_1()

        login_page.click_when_bring_scooter()
        login_page.chose_date_from_calendar(data_calendar)
        login_page.click_rental_period()
        login_page.choose_rental_period(rental_period)

        login_page.choose_color(color)
        login_page.set_comment_for_currier(comment)
        login_page.click_button_order(BasePage.middle_button_order)

        login_page.click_button_DA()
        title_succes_order = driver.find_element(*OrderPage2.title_succes_order)
        assert title_succes_order.is_displayed() and "Заказ оформлен" in title_succes_order.text

    @allure.description('Редирект с страницы заказа на главную по нажатию на иконку самоката')
    def test_redirect_home_page(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page(data.Urls.ORDER_PAGE)
        login_page.click_cookie()
        login_page.click_logo_scooter()
        current_url = driver.current_url
        assert current_url == data.Urls.HOME_PAGE

    @allure.description('Редирект с страницы заказа на страницу "Яндекс Дзен" по нажатию на иконку яндекс')
    def test_redirect_ya_dzen(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page(data.Urls.ORDER_PAGE)
        login_page.click_cookie()
        login_page.click_logo_ya_dzen()
        login_page.switch_to_next_tub(driver, -1)
        login_page.wait_title(driver, "Дзен")
        title_dzen = driver.title
        assert title_dzen == 'Дзен'
