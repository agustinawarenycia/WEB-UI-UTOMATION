Feature: Login

  Scenario Outline: Como usuario deseo poder logearme correctamente
    Given entro a la pagina
    When cuando hago el login con "<usuario>" y "<contraseña>"
    Then valido me haya logeado correactemente
    #And cierro el browser
    Examples:
      | usuario       | contraseña   |
      | standard_user | secret_sauce |