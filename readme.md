


Para instalar scoop (esto pide allure)
https://github.com/ScoopInstaller/Install#advanced-installation

Para instalar allure 
https://docs.qameta.io/allure/#_how_to_proceed

Para correr el código y generar el reporte:

###########################################################################
_behave -f allure_behave.formatter:AllureFormatter -o report ./features_
###########################################################################

Para pasar el reporte a HTML:

###########################################################################
 allure serve report
###########################################################################



Correr con comando para el runner:

py features/runner.py --testdir=features


Para correr con Junit:
behave --junit 

Para obtener un reporte en HTML corriendo desde el runner:
py features/runner.py --testdir=features
