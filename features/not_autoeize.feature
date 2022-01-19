@regress
Feature: Проверка функционала неавторизованым пользователем
  """ Групировать можно по разному. Я групировал по "Авторизован"/"Не авторизован".
  Можно например по функционалу: отдельный feature файлик на кнопки в меню, отдельный на поиск и.т.д"""

  # Стандартный тест
  @fixture.browser.chrome
  Scenario: Редирект на страницу атворизации
    Given Открыта главная страница YouTube
    When Нажимаем на кнопку "Войти"
    Then Происходит редирект на страницу авторизации гугла

  # Пример параметризации в behave
  @fixture.browser.chrome
  Scenario Template: Проверка кнопок навигации
    Given Открыта главная страница YouTube
    When Нажимаем на кнопку с текстом "<text>"
    Then Происходит переход на страницу c урлом "<url>"
    And Присутствует текст на странице со значением "<value>"
    Examples:
      | text       | url           | value                                                                         |
      | Подписки   | subscriptions | Тогда в этом разделе появятся новые видео с каналов, на которые вы подписаны. |
      | Библиотека | library       | Здесь вы увидите сохраненные видео и те, которые вам понравились.             |

  @search
  @fixture.browser.chrome
  Scenario: beg
    Given Открыта главная страница YouTube
    When Вводим в поле поиска "АстралОтчет"
    And Нажимаем "Поиск"
    Then В адресной строке содержится урл поиска со значением "АстралОтчет"
    And Для прикола счиатем количество кнопок "Войти" их должно быть "3"

