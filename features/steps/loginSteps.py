import time

from behave import *
from features.pages.HomePage import *
from features.pages.LoginPage import *


@given('visito la pagina saucedemo')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.driver.get(login_page.baseURL)


@when('ingreso "{user}" en el campo username')
def step_impl(context, user):
    login_page = LoginPage(context.driver)
    login_page.send_user(user)
    time.sleep(1)


@step('ingreso "{password}" en el campo password')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.send_password(password)
    time.sleep(1)


@step('hago click en el boton de login')
def step_impl(context):
    login_page = LoginPage(context.driver)
    time.sleep(1)
    login_page.click_login()


@then('valido me haya logeado correactemente')
def step_impl(context):
    home_page = HomePage(context.driver)
    assert "PRODUCTS" in home_page.get_text_header_title()
    time.sleep(5)\

@then('valido mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    login_page = LoginPage(context.driver)
    assert mensaje in login_page.get_text_header_title()
    time.sleep(5)

