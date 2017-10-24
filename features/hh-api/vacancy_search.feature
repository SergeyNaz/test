Feature: Query for a searching of vacancies

  Background:
    Given I create initial vacancy searching request
    And I add area parameter with "2" value as GET parameter to request string
    And I add employer_id parameter with "213397" value as GET parameter to request string

    Scenario: Check QA Automation Engineer vacancy from company in SPb
      When I execute request string
      Then Returned code is 200
      Then Response contains item where "name" key has "QA Automation E‎ngineer" value

    Scenario: Check QA Automation Engineer vacancy from company in SPb when also using text parameter
      And I add text parameter with "QA Automation Engineer" value as GET parameter to request string
      When I execute request string
      Then Returned code is 200
      Then Response contains item where "name" key has "QA Automation E‎ngineer" value