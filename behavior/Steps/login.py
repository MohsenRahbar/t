"""
    test login feature 
"""
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Scenario: Successful Login with Phone Number
@given(u'I am on the national window login page.')
def goToLoginPage(context):
   context.driver = webdriver.Chrome()
   context.driver.get("https://https://sso.my.gov.ir/login")

@when(u'I enter the correct phone number in the format +98-09-33-688.')
def enterPhoneNumber(context):
    context.phone_number_input = context.driver.find_element(By.ID,"username")  
    context.phone_number_input.send_keys("+98-09-33-688")

@when(u'I enter the correct 5-digit security code.')
def enterSecurityCode(context):
    context.security_code_input = context.driver.find_element(By.ID, "security_code_input")  # example for security code
    context.security_code_input.send_keys("12345") # That is forexample security code
    
@when(u'I click the login button')
def clickLoginButton(context):
    context.login_button = context.driver.find_element(By.ID, "send-otp-form-btn")  
    context.login_button.click()

@when(u'I enter the dynamic password')
def enterDynamicPassword(context):
    context.dynamic_password_input = context.driver.find_element(By.ID, "dynamic_password_input") 
    context.dynamic_password_input.send_keys("correct_password")  

@then(u'I am successfully logged in')
def verifySuccessfulLogin(context):
    # Check for successful login indicator (e.g., presence of specific element)
    # assert url= https://my.gov.ir/profile/user
    pass

# ... (similar implementations for other scenarios)

@when(u'I enter the wrong dynamic password.')
def enterWrongDynamicPassword(context):
    context.dynamic_password_input = context.driver.find_element(By.ID, "dynamic_password_input")  
    context.dynamic_password_input.send_keys("wrong_password")

@then(u'I see an error message indicating that The one-time password is incorrect')
def verifyIncorrectPasswordErrorMessage(context):
    context.error_message = context.driver.find_element('xpath',"//*[@class()='text-warning']").getText();  
    assert "The one-time password is incorrect" in context.error_message.text
    # close browser 
    context.driver.quit()
