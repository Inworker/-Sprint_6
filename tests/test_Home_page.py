import allure
import pytest
import data
from pages.Home_page import HomePageScooter
from locators.Base_page_locators import BasePageLocators
from locators.Home_page_locators import HomePageLocators


class TestHomePage:
    @pytest.mark.parametrize('question_locator, answer_locator, answer',
                             [
                                 (HomePageLocators.drop_down_question_1, HomePageLocators.drop_down_answer_1,
                                  data.Answers.ANSWER[0]),
                                 (HomePageLocators.drop_down_question_2, HomePageLocators.drop_down_answer_2,
                                  data.Answers.ANSWER[1]),
                                 (HomePageLocators.drop_down_question_3, HomePageLocators.drop_down_answer_3,
                                  data.Answers.ANSWER[2]),
                                 (HomePageLocators.drop_down_question_4, HomePageLocators.drop_down_answer_4,
                                  data.Answers.ANSWER[3]),
                                 (HomePageLocators.drop_down_question_5, HomePageLocators.drop_down_answer_5,
                                  data.Answers.ANSWER[4]),
                                 (HomePageLocators.drop_down_question_6, HomePageLocators.drop_down_answer_6,
                                  data.Answers.ANSWER[5]),
                                 (HomePageLocators.drop_down_question_7, HomePageLocators.drop_down_answer_7,
                                  data.Answers.ANSWER[6]),
                                 (HomePageLocators.drop_down_question_8, HomePageLocators.drop_down_answer_8,
                                  data.Answers.ANSWER[-1])
                             ])
    @allure.description('Отображение ответа по клику на вопрос')
    def test_question_base_page(self, driver, question_locator, answer_locator, answer):
        login_page = HomePageScooter(driver)
        login_page.open_page_click_cookie(data.Urls.HOME_PAGE)
        login_page.click_question_get_answer(HomePageLocators.drop_down_question_1, question_locator, question_locator)
        assert login_page.get_answer(answer_locator) == answer

    @allure.description('Открытие страницы заказа по нажатию на кнопку "Заказать" вверху главной страницы')
    def test_click_top_button_order(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page_click_cookie(data.Urls.HOME_PAGE)
        login_page.click_top_button_order()
        current_url = driver.current_url
        assert current_url == data.Urls.ORDER_PAGE

    @allure.description('Открытие страницы заказа по нажатию на кнопку "Заказать" по середине главной страницы')
    def test_click_middle_button_order(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page_click_cookie(data.Urls.HOME_PAGE)
        login_page.click_question_get_answer(BasePageLocators.middle_button_order, BasePageLocators.middle_button_order,
                                             BasePageLocators.middle_button_order)
        current_url = driver.current_url
        assert current_url == data.Urls.ORDER_PAGE
