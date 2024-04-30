import allure
from selenium.webdriver.common.by import By
import data
from pages.Base_page import BasePage


class OrderPage1(BasePage):
    title_order_page_1 = (By.CLASS_NAME, "Order_Header__BZXOb")                                 # Заголовок "Для кого самокат"
    input_name = (By.XPATH, "//input[@placeholder = '* Имя']")                                  # Поле ввода "Имя"
    input_family = (By.XPATH, "//input[@placeholder = '* Фамилия']")                            #Поле ввода "Фамилия"
    input_address = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")        #Поле ввода "Адрес"
    input_station_metro = (By.XPATH, "//input[@placeholder = '* Станция метро']")               #Поле ввода "Станция метро"
    station_metro_1 = (By.XPATH, "//button[@value = '1']")
    station_metro_2 = (By.XPATH, "//button[@value = '2']")                                      # локатор для выбора 1 станции метро
    input_telephone_number = (By.XPATH,
                              "//input[@placeholder = '* Телефон: на него позвонит курьер']")   # Поле ввода "Телефон"
    button_next = (By.XPATH, ".//button[contains (text (), 'Далее')]")  # Кнопка "Далее"

    @allure.step('Заполнить поле "Имя"')
    def enter_data_field_name(self, name):
        enter_name = self.driver.find_element(*self.input_name)
        enter_name.send_keys(name)
    @allure.step('Заполнить поле "Фамилия"')
    def enter_data_field_family(self, family):
        enter_family = self.driver.find_element(*self.input_family)
        enter_family.send_keys(family)
    @allure.step('Заполнить поле "Адресс"')
    def enter_data_field_address(self, adress):
        enter_address = self.driver.find_element(*self.input_address)
        enter_address.send_keys(adress)

    @allure.step('Нажать на поле "Метро"')
    def click_field_metro(self):
        station_metro = self.driver.find_element(*self.input_station_metro)
        station_metro.click()

    @allure.step('Выбрать станцию метро')
    def set_station_metro(self, name_station):
        set_station = self.driver.find_element(*name_station)
        set_station.click()

    @allure.step('Заполнить поле "Номер телефона"')
    def enter_data_field_telephone(self, telephone):
        enter_telephone = self.driver.find_element(*self.input_telephone_number)
        enter_telephone.send_keys(telephone)

    @allure.step('Нажать на кнопку "Далее"')
    def click_button_next(self):
        button_next = self.driver.find_element(*self.button_next)
        button_next.click()

    @allure.step('Заполнить 1-ю страницу заказа')
    def set_order_page_1(self):

        self.open_page(data.Urls.ORDER_PAGE)
        self.click_cookie()
        self.enter_data_field_name(data.Order_data.NAME[0])
        self.enter_data_field_family(data.Order_data.FAMILY[0])
        self.enter_data_field_address(data.Order_data.ADDRESS[0])
        self.enter_data_field_telephone(data.Order_data.TELEPHONE[0])
        self.click_field_metro()
        self.set_station_metro(OrderPage1.station_metro_1)
        self.click_button_next()


class OrderPage2(OrderPage1):


    title_about_rent = (By.CLASS_NAME, "Order_Header__BZXOb")                                   #Заголовок "Про аренду"
    input_when_bring_scooter = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']") #Поле ввода "Куда привезти самокат
    calendar_1_may = (By.XPATH, "//div[@aria-label = 'Choose среда, 1-е мая 2024 г.']")
    calendar_2_may = (By.XPATH, "//div[@aria-label = 'Choose четверг, 2-е мая 2024 г.']")       # Дата в календаре
    form_calendar = (By.CLASS_NAME, "react-datepicker__month-container")                        # Форма календаря
    input_rental_period = (By.XPATH, "//div[@class = 'Dropdown-root']")                         # Выпадающий список "Срок аренды"
    list_rental_period_1_sutki = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[1]")           # Выбор срока аренды - 1 сутки
    list_rental_period_6_sutki = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[6]")           # Выбор срока аренды - 6 сутки
    color_scooter_black = (By.XPATH, "//label[@for = 'black']")                                 # Чек-бокс цвета самоката = Черный
    color_scooter_grey = (By.XPATH, "//label[@for = 'grey']")                                   # Чек-бокс цвета самоката = Серый
    input_comment_for_currier = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']") #Поле ввода "Коммент для курьера"
    title_order_zakaz = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")                             #Заголовок "Хотите оформить заказ"?
    button_da = (By.XPATH, "//button[contains (text (), 'Да')]")                                #Кнопка "Да"
    button_net = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")  #Кнопка "Нет"
    title_succes_order = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")                            # Заголовок "Заказ оформлен"

    @allure.step('Клик на поле "когда привезти самокат" ')
    def click_when_bring_scooter(self):
        when_bring_scooter = self.driver.find_element(*self.input_when_bring_scooter)
        when_bring_scooter.click()

    @allure.step('Выбрать дату из календаря')
    def chose_date_from_calendar(self, date_calendar):
        data_from_calendar = self.driver.find_element(*date_calendar)
        data_from_calendar.click()

    @allure.step('Клик на поле "Срок аренды"')
    def click_rental_period(self):
        rental_period = self.driver.find_element(*self.input_rental_period)
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
        set_comment = self.driver.find_element(*self.input_comment_for_currier)
        set_comment.send_keys(comment_currier)

    @allure.step('Клик на кнопку "Да"')
    def click_button_DA(self):
        button_da1 = self.driver.find_element(*self.button_da)
        button_da1.click()