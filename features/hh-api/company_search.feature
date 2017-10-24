Feature: Query for a searching of companies

    Background:
      Given I create initial employer searching request
      And I add area parameter with "113" value as GET parameter to request string
      And I add text parameter with "Новые Облачные Технологии" value as GET parameter to request string

    Scenario: Search by Russia region and company name returned one item
      When I execute request string
      Then Returned code is 200
      Then Response contains 1 count of items by "items" key
      Then Item contains "Новые Облачные Технологии" value for "name" key

    Scenario: Search by Russia region and company name returned one item when using only_with_vacancies=true
      And I add only_with_vacancies parameter with "true" value as GET parameter to request string
      When I execute request string
      Then Returned code is 200
      Then Response contains 1 count of items by "items" key
      Then Item contains "Новые Облачные Технологии" value for "name" key