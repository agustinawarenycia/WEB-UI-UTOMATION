from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()

    print("Creo el webDriver correctamente\n")


def after_scenario(context, scenario):
    context.driver.close()
    print("Cierro el webDriver correctamente\n")


