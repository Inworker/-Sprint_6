import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    button_cookie = (By.ID, "rcc-confirm-button")       # Кнопка Куки
    img_scooter = (By.XPATH, "//img[@alt = 'Scooter']") #Иконка Самоката
    img_yandex = (By.XPATH, "//img[@alt = 'Yandex']")   #Иконка Яндекса
    top_button_order = (By.XPATH, '//button[@class = "Button_Button__ra12g" and (text ()= "Заказать")]') #Верхняя кнопка "Заказать"
    middle_button_order = (By.XPATH,
                            "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and (text ()= 'Заказать')]") #Кнопка заказать по средине страницы


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание отображения элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание активность документа')
    def wait_active_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Нажать на кнпоку "куки" ')
    def click_cookie(self):
        button_cookie = self.driver.find_element(*self.button_cookie)
        button_cookie.click()

    @allure.step('Нажать на иконку "Самокат"')
    def click_logo_scooter(self):
        click_scooter = self.driver.find_element(*self.img_scooter)
        click_scooter.click()

    @allure.step('Нажать на логотип Яндекс')
    def click_logo_ya_dzen(self):
        click_ya_dzen = self.driver.find_element(*self.img_yandex)
        click_ya_dzen.click()

    @allure.step('Переключение на новую вкладку')
    def switch_to_next_tub(self, driver, new_tab_index):
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[new_tab_index])

    @allure.step('Ожидание отображения заголвка страницы')
    def wait_title(self, driver, title):
        WebDriverWait(driver, 5).until(expected_conditions.title_is(title))

    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order(self, button):
        button = self.driver.find_element(*button)
        button.click()