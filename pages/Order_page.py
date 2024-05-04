import allure
from locators.Order_page_locators import OrderPage1Locators, OrderPage2Locators
from pages.Base_page import BasePage


class OrderPage1(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def enter_data_field_name(self, name):
        enter_name = self.driver.find_element(*OrderPage1Locators.input_name)
        enter_name.send_keys(name)

    @allure.step('Заполнить поле "Фамилия"')
    def enter_data_field_family(self, family):
        enter_family = self.driver.find_element(*OrderPage1Locators.input_family)
        enter_family.send_keys(family)

    @allure.step('Заполнить поле "Адресс"')
    def enter_data_field_address(self, adress):
        enter_address = self.driver.find_element(*OrderPage1Locators.input_address)
        enter_address.send_keys(adress)

    @allure.step('Нажать на поле "Метро"')
    def click_field_metro(self):
        station_metro = self.driver.find_element(*OrderPage1Locators.input_station_metro)
        station_metro.click()

    @allure.step('Выбрать станцию метро')
    def set_station_metro(self, name_station):
        set_station = self.driver.find_element(*name_station)
        set_station.click()

    @allure.step('Заполнить поле "Номер телефона"')
    def enter_data_field_telephone(self, telephone):
        enter_telephone = self.driver.find_element(*OrderPage1Locators.input_telephone_number)
        enter_telephone.send_keys(telephone)

    @allure.step('Нажать на кнопку "Далее"')
    def click_button_next(self):
        button_next = self.driver.find_element(*OrderPage1Locators.button_next)
        button_next.click()

    @allure.step('Заполнить 1-ю страницу заказа')
    def set_order_page_1(self, url, name, family, adress, tephone, station):
        self.open_page_click_cookie(url)
        self.enter_data_field_name(name)
        self.enter_data_field_family(family)
        self.enter_data_field_address(adress)
        self.enter_data_field_telephone(tephone)
        self.click_field_metro()
        self.set_station_metro(station)
        self.click_button_next()


class OrderPage2(OrderPage1):

    @allure.step('Клик на поле "когда привезти самокат" ')
    def click_when_bring_scooter(self):
        when_bring_scooter = self.driver.find_element(*OrderPage2Locators.input_when_bring_scooter)
        when_bring_scooter.click()

    @allure.step('Выбрать дату из календаря')
    def chose_date_from_calendar(self, date_calendar):
        data_from_calendar = self.driver.find_element(*date_calendar)
        data_from_calendar.click()

    @allure.step('Клик на поле "Срок аренды"')
    def click_rental_period(self):
        rental_period = self.driver.find_element(*OrderPage2Locators.input_rental_period)
        rental_period.click()

    @allure.step('Выбор срока аренды')
    def choose_rental_period(self, rental_period):
        rental_period = self.driver.find_element(*rental_period)
        rental_period.click()

    @allure.step('Выбор цвета самоката')
    def choose_color(self, color):
        set_color = self.driver.find_element(*color)
        set_color.click()

    @allure.step('Нажать на поле "Комментарий для курьера"')
    def set_comment_for_currier(self, comment_currier):
        set_comment = self.driver.find_element(*OrderPage2Locators.input_comment_for_currier)
        set_comment.send_keys(comment_currier)

    @allure.step('Клик на кнопку "Да"')
    def click_button_DA(self):
        button_da1 = self.driver.find_element(*OrderPage2Locators.button_da)
        button_da1.click()

    @allure.step('Заполнить 2 страницу заказа')
    def set_order_page_2(self, data_calendar, rental_period, color, comment):
        self.click_when_bring_scooter()
        self.chose_date_from_calendar(data_calendar)
        self.click_rental_period()
        self.choose_rental_period(rental_period)
        self.choose_color(color)
        self.set_comment_for_currier(comment)

    @allure.step('Открыть окно "Заказ успешно создан"')
    def open_window_confirm(self):
        self.click_middle_button_order()
        self.click_button_DA()
