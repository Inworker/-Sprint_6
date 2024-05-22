from selenium.webdriver.common.by import By


class OrderPage1Locators:
    title_order_page_1 = (By.CLASS_NAME, "Order_Header__BZXOb")  # Заголовок "Для кого самокат"
    input_name = (By.XPATH, "//input[@placeholder = '* Имя']")  # Поле ввода "Имя"
    input_family = (By.XPATH, "//input[@placeholder = '* Фамилия']")  # Поле ввода "Фамилия"
    input_address = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")  # Поле ввода "Адрес"
    input_station_metro = (By.XPATH, "//input[@placeholder = '* Станция метро']")  # Поле ввода "Станция метро"
    station_metro_1 = (By.XPATH, "//button[@value = '1']")
    station_metro_2 = (By.XPATH, "//button[@value = '2']")  # локатор для выбора 1 станции метро
    input_telephone_number = (By.XPATH,
                              "//input[@placeholder = '* Телефон: на него позвонит курьер']")  # Поле ввода "Телефон"
    button_next = (By.XPATH, ".//button[contains (text (), 'Далее')]")  # Кнопка "Далее"


class OrderPage2Locators:
    title_about_rent = (By.CLASS_NAME, "Order_Header__BZXOb")  # Заголовок "Про аренду"
    input_when_bring_scooter = (
        By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")  # Поле ввода "Куда привезти самокат
    calendar_1_may = (By.XPATH, "//div[@aria-label = 'Choose среда, 1-е мая 2024 г.']")
    calendar_2_may = (By.XPATH, "//div[@aria-label = 'Choose четверг, 2-е мая 2024 г.']")  # Дата в календаре
    form_calendar = (By.CLASS_NAME, "react-datepicker__month-container")  # Форма календаря
    input_rental_period = (By.XPATH, "//div[@class = 'Dropdown-root']")  # Выпадающий список "Срок аренды"
    list_rental_period_1_sutki = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[1]")  # Выбор срока аренды - 1 сутки
    list_rental_period_6_sutki = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[6]")  # Выбор срока аренды - 6 сутки
    color_scooter_black = (By.XPATH, "//label[@for = 'black']")  # Чек-бокс цвета самоката = Черный
    color_scooter_grey = (By.XPATH, "//label[@for = 'grey']")  # Чек-бокс цвета самоката = Серый
    input_comment_for_currier = (
        By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")  # Поле ввода "Коммент для курьера"
    title_order_zakaz = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # Заголовок "Хотите оформить заказ"?
    button_da = (By.XPATH, "//button[contains (text (), 'Да')]")  # Кнопка "Да"
    button_net = (
        By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")  # Кнопка "Нет"
    title_succes_order = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
