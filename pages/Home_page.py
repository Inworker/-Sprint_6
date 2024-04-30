import allure
from selenium.webdriver.common.by import By
from pages.Base_page import BasePage


class HomePageScooter(BasePage):

    drop_down_question_1 = (By.ID, "accordion__heading-0")    #1 вопрос
    drop_down_answer_1 = (By.ID, "accordion__panel-0")        #1 ответ

    drop_down_question_2 = (By.ID, "accordion__heading-1")    #2 вопрос
    drop_down_answer_2 = (By.ID, "accordion__panel-1")        #2 ответ

    drop_down_question_3 = (By.ID, "accordion__heading-2")    #3 вопрос
    drop_down_answer_3 = (By.ID, "accordion__panel-2")        #3 ответ

    drop_down_question_4 = (By.ID, "accordion__heading-3")    #4 вопрос
    drop_down_answer_4 = (By.ID, "accordion__panel-3")        #4 ответ

    drop_down_question_5 = (By.ID, "accordion__heading-4")    #5 вопрос
    drop_down_answer_5 = (By.ID, "accordion__panel-4")        #5 ответ

    drop_down_question_6 = (By.ID, "accordion__heading-5")    #6 вопрос
    drop_down_answer_6 = (By.ID, "accordion__panel-5")        #6 ответ

    drop_down_question_7 = (By.ID, "accordion__heading-6")    #7 вопрос
    drop_down_answer_7 = (By.ID, "accordion__panel-6")        #7 ответ

    drop_down_question_8 = (By.ID, "accordion__heading-7")    #8 вопрос
    drop_down_answer_8 = (By.ID, "accordion__panel-7")        #8 ответ


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