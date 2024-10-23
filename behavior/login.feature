# login feature test
Feature: login Capability Test

    Scenario: Successful Login with Phone Number
        Given I am on the national window login page.
        When  I enter the correct phone number in the format +98-09-33-688.
        And   I enter the correct 5-digit security code.
        And   I click the "Login" button.
        And   I enter the correct dynamic password.
        Then  I am successfully logged in to the national window site.

    Scenario: Failed Login without security code
        Given I am on the national window login page.
        When  I enter the correct phone number and i did not enter security code.
        Then  I see Submit button is disabled  
        
    Scenario: Failed Login without enter the phone
        Given I am on the national window login page.
        When  I did not enter the phone number and i did enter the correct security code
        Then  I see an error message indicating that No number entered and the Submit button is disabled .

    Scenario: Failed Login without enter the phone and security code
        Given I am on the national window login page.
        When  I did not enter the phone number and i did enter security code
        Then  I see Submit button is disabled      

    Scenario: Failed Login with  enter Incorrect  phone
        Given I am on the national window login page.
        When  I enter the wrong phone number in the format +98-33-688.
        Then  I see an error message indicating that the Entered mobile number must be 11 digits and start with 09 and Submit button is disabled  
    
    Scenario: Failed Login with enter wrong the security code and phone
        Given I am on the national window login page.
        When  I enter the wrong phone number in the format +98-33-688.
        Then  I see an error message indicating that the Entered mobile number must be 11 digits and start with 09 and Submit button is disabled
    
    Scenario: Faild Login with Incorrect dynamic password 
        Given I am on the national window login page.
        When  I enter the correct phone number in the format +98-09-33-688.
        And   I enter the correct 5-digit security code.
        And   I click the "Login" button.
        And   I enter the wrong dynamic password.
        Then  I see back to first steps and I see an error message indicating that The one-time password is incorrect

    Scenario: Faild Login without dynamic password 
        Given I am on the national window login page.
        When  I enter the correct phone number in the format +98-09-33-688.
        And   I enter the correct 5-digit security code.
        And   I click the "Login" button.
        And   I enter the wrong dynamic password.
        Then  I see Submit button is disabled 
