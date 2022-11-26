from behave import *
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given('entro a la pagina')
def ingresoWeb(context):
    context.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
    context.driver.get("https://www.saucedemo.com/")


@when('cuando hago el login con "{usuario}" y "{contraseña}"')
def ingresoDatos(context, usuario, contraseña):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(contraseña)
    context.driver.find_element(By.ID, "login-button").click()


@then('valido me haya logeado correactemente')
def validoMeHayaLogeado(context):
    try:
        titulo = context.driver.find_element(By.CLASS_NAME, "title").text
    except:
        context.driver.close();
        assert False, "Test falladao"
    if titulo == "PRODUCTS":
        context.driver.close()
        assert True, "Test pass"

# @then('cierro el browser')
# def step_impl(context):
