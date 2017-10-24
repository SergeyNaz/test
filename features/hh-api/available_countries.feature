Feature: Query of available countries

    Background:
      Given I request available countries

    Scenario: Request of available countries returned correct response
      Then Returned code is 200
      Then Returned items have url, id, name fields
      Then Each country url follows to the area with the same name and id


