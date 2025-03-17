from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import given, when, then

@given('I open the browser')
def step_open_browser(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    context.driver.maximize_window()
    sleep(2)

@when('I enter the username "{username}"')
def step_enter_username(context, username):
    username_input = context.driver.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(username)

@when('I enter the password "{password}"')
def step_enter_password(context, password):
    password_input = context.driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

@when('I click the login button')
def step_click_login(context):
    login_button = context.driver.find_element(By.ID, "submit")
    login_button.click()
    sleep(2)

@then('I should see the success message "{message}"')
def step_verify_login(context, message):
    success_message = context.driver.find_element(By.XPATH, "//h1")
    assert success_message.text == message, f"Expected '{message}' but got '{success_message.text}'"
