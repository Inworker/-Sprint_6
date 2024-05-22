from selenium.webdriver.common.by import By


class BasePageLocators:
    button_cookie = (By.ID, "rcc-confirm-button")  # Кнопка Куки
    img_scooter = (By.XPATH, "//img[@alt = 'Scooter']")  # Иконка Самоката
    img_yandex = (By.XPATH, "//img[@alt = 'Yandex']")  # Иконка Яндекса
    top_button_order = (
        By.XPATH, '//button[@class = "Button_Button__ra12g" and (text ()= "Заказать")]')  # Верхняя кнопка "Заказать"
    middle_button_order = (By.XPATH,
                           "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and (text ()= 'Заказать')]")  # Кнопка заказать по средине страницы
