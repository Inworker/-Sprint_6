import allure
from pages.Base_page import BasePage


class HomePageScooter(BasePage):

    @allure.step('Скролл до локатора')
    def scroll_to_locator(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по вопросу')
    def click_question(self, locator_q):
        question_1 = self.driver.find_element(*locator_q)
        question_1.click()

    @allure.step('Получить текст ответа')
    def get_answer(self, locator_a):
        answer = self.driver.find_element(*locator_a)
        return answer.text

    @allure.step('Открыть страницу и нажать на кнопку Куки')
    def click_question_get_answer(self, locator, element_locator, locator_q):
        self.scroll_to_locator(locator)
        self.wait_and_find_element(element_locator)
        self.click_question(locator_q)
