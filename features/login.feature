# ---------------------------------------------------------------------------
# Created By  : Guillermo Navarro
# Created Date: 13/06/2022
# version ='1.0'
# Comment: Definition of the tests for login feature
# ---------------------------------------------------------------------------

Feature: Sysdig login page

Scenario Outline: Verify if a user cannot login with invalid credentials.
  Given I am on "<url>"
  When I set email to "<email>"
  And  I set password to "<password>"
  And I click login button
  Then I get message denying the access

  Examples:
      | url                          | email                 | password        |
      | https://eu1.app.sysdig.com/  | gnavarrop86@gmail.com | asdf |


Scenario Outline: Verify if a user can login with valid credentials.
  Given I am on "<url>"
  When I set email to "<email>"
  And  I set password to "<password>"
  And I click login button
  Then I can login

  Examples:
      | url                          | email                 | password        |
      | https://eu1.app.sysdig.com/ | frikiflipi@gmail.com  | ASDF1234asdf! |


  Scenario: Verify forgot your password functionality
    Given I am on "https://eu1.app.sysdig.com/"
    When I click on forgot your password
    And I set recovery email to "test@gmail.com"
    And I click on password reset button
    Then I get message saying the password has been sent