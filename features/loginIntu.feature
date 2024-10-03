Feature: Login Intu Feature
    Scenario: Successful intu login with valid credentials
    Given the user is on the intu login page
    When the user logs into intu with valid credentials
    Then the user should be redirected to the dashboard page