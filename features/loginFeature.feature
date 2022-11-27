#language: en
Feature: Login
  Como usuario deseo poder logearme en la pagina saucedemo.

  Scenario Outline: Login exitoso
    Given visito la pagina saucedemo
    When ingreso "<user>" en el campo username
    And  ingreso "<password>" en el campo password
    And  hago click en el boton de login
    Then valido me haya logeado correactemente
    Examples:
      | user          | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Login fallido
    Given visito la pagina saucedemo
    When ingreso "<user>" en el campo username
    And  ingreso "<password>" en el campo password
    And  hago click en el boton de login
    Then valido mensaje de error "<mensaje>"
    Examples:
      | user          | password     | mensaje   |
      | usuario_error | secret_sauce | not match |