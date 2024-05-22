import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.Base_page_locators import BasePageLocators


class BasePage:

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
        button_cookie = self.driver.find_element(*BasePageLocators.button_cookie)

        button_cookie.click()

    @allure.step('Нажать на иконку "Самокат"')
    def click_logo_scooter(self):
        click_scooter = self.driver.find_element(*BasePageLocators.img_scooter)
        click_scooter.click()

    @allure.step('Нажать на логотип Яндекс')
    def click_logo_ya_dzen(self):
        click_ya_dzen = self.driver.find_element(*BasePageLocators.img_yandex)
        click_ya_dzen.click()

    @allure.step('Переключение на новую вкладку')
    def switch_to_next_tub(self, driver, new_tab_index):
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[new_tab_index])

    @allure.step('Ожидание отображения заголвка страницы')
    def wait_title(self, driver, title):
        WebDriverWait(driver, 5).until(expected_conditions.title_is(title))

    @allure.step('Нажать на кнопку "Заказать" вверху страницы')
    def click_top_button_order(self):
        button = self.driver.find_element(*BasePageLocators.top_button_order)
        button.click()

    @allure.step('Нажать на кнопку "Заказать" по середине страницы')
    def click_middle_button_order(self):
        button = self.driver.find_element(*BasePageLocators.middle_button_order)
        button.click()

    @allure.step('Открыть страницу и нажать на кнопку "Куки"')
    def open_page_click_cookie(self, url):
        self.open_page(url)
        self.click_cookie()

    @allure.step('Открыть новую вкладку "Дзен"')
    def open_new_tub_dzen(self, driver):
        self.click_logo_ya_dzen()
        self.switch_to_next_tub(driver, -1)
        self.wait_title(driver, "Дзен")
