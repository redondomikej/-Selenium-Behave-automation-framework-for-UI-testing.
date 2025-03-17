Feature: Login and Navigate to Pages
    Scenario: Successful login
    Given I open the browser
    When I enter the username "student"
    And I enter the password "Password123"
    And I click the login button
    Then I should see the success message "Logged In Successfully"

    Scenario: Invalid login
    Given I open the browser
    When I enter the username "student"
    And I enter the password "Password123"
    And I click the login button
    Then I should see the success message "Invalid login"