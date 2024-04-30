#Проект автоматизации тестирования https://qa-scooter.praktikum-services.ru
1. Основа для написания автотестов - фреймворк pytest. 
2. В Base_page.py - Лежат общие локаторы и функции
3. В Home_page.py - Лежат локаторы и функции для главной страницы
4. В Order_page.py - Лежат локаторы и функции для страницы заказа

5. В папке tests - лежат автотесты разбитые по функционалу 
	test_Home_page.py - Тесты для главной страницы
	tests_Order_page.py - Тесты для страницы заказа
6.	.gitignore - Добавлены файлы для игнорирования PR	
7. В conftest.py - добавлены фикстуры 
8. В data.py - тестовые данные содержат 3 класса:
	Urls - адрес главной страницы и страницы заказа
	Order_data - Лежат тестовые имена, фамилии, телефоны и комментарии для курьера
	Answer - Лежат ответы для каждого вопроса
9. В requirements.txt добавлены все установленные пакеты
10. Команда для запуска - pytest -v 
11. Запуск из IDE Pycharm - необходимо указать для каждого теста область проекта = корневой папке