from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_intu_page import LoginIntuPage
from pages.dashboard_intu_page import DashboardIntuPage

@given('the user is on the intu login page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_intu_page = LoginIntuPage(context.driver)

@when('the user logs into intu with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_intu_page.login("1006015532", "JuvesVirnes20!!")

@then('the user should be redirected to the dashboard page')
def step_then_user_redirected_dashboard(context):
    dashboard_intu_page = DashboardIntuPage(context.driver)
    assert dashboard_intu_page.is_dashboard_page_displayed()
