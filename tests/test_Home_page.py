import allure
import pytest
from conftest import driver
import data
from pages.Base_page import BasePage
from pages.Home_page import HomePageScooter


class TestBasePage:
    @pytest.mark.parametrize('question_locator, answer_locator, answer',
                             [
                                 (HomePageScooter.drop_down_question_1, HomePageScooter.drop_down_answer_1, data.Answers.ANSWER[0]),
                                 (HomePageScooter.drop_down_question_2, HomePageScooter.drop_down_answer_2, data.Answers.ANSWER[1]),
                                 (HomePageScooter.drop_down_question_3, HomePageScooter.drop_down_answer_3, data.Answers.ANSWER[2]),
                                 (HomePageScooter.drop_down_question_4, HomePageScooter.drop_down_answer_4, data.Answers.ANSWER[3]),
                                 (HomePageScooter.drop_down_question_5, HomePageScooter.drop_down_answer_5, data.Answers.ANSWER[4]),
                                 (HomePageScooter.drop_down_question_6, HomePageScooter.drop_down_answer_6, data.Answers.ANSWER[5]),
                                 (HomePageScooter.drop_down_question_7, HomePageScooter.drop_down_answer_7, data.Answers.ANSWER[6]),
                                 (HomePageScooter.drop_down_question_8, HomePageScooter.drop_down_answer_8, data.Answers.ANSWER[-1])
                             ])
    @allure.description('Отображение ответа по клику на вопрос')
    def test_question_base_page(self, driver, question_locator, answer_locator, answer):
        login_page = HomePageScooter(driver)
        login_page.open_page(data.Urls.HOME_PAGE)
        login_page.click_cookie()
        login_page.scroll_to_locator(HomePageScooter.drop_down_question_1)
        login_page.wait_and_find_element(question_locator)
        login_page.click_question(question_locator)
        assert login_page.get_answer(answer_locator) == answer

    @allure.description('Открытие страницы заказа по нажатию на кнопку "Заказать" вверху главной страницы')
    def test_click_top_button_order(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page(data.Urls.HOME_PAGE)
        login_page.click_cookie()
        login_page.click_button_order(BasePage.top_button_order)
        current_url = driver.current_url
        excepted_url = "https://qa-scooter.praktikum-services.ru/order"
        assert current_url == excepted_url

    @allure.description('Открытие страницы заказа по нажатию на кнопку "Заказать" по середине главной страницы')
    def test_click_middle_button_order(self, driver):
        login_page = HomePageScooter(driver)
        login_page.open_page(data.Urls.HOME_PAGE)
        login_page.click_cookie()
        login_page.scroll_to_locator(BasePage.middle_button_order)
        login_page.wait_and_find_element(HomePageScooter.middle_button_order)
        login_page.click_button_order(BasePage.middle_button_order)
        current_url = driver.current_url
        excepted_url = "https://qa-scooter.praktikum-services.ru/order"
        assert current_url == excepted_url