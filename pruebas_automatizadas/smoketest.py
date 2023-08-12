from unittest import TestLoader, TestSuite
from searchtest import SearchTests
from pyunitreport import HTMLTestRunner
from assertion import AssertionsTest


#Variables para cargar los casos de prueba
assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

#Construyendo la suit de pruebas
smoke_test = TestSuite([assertion_test, search_test])

#Parámetros para generar el reporte
kwargs = {
    "output": "reportes/smoke-report"
}

runner = HTMLTestRunner(**kwargs) #Pasando los argumentos para la generación del reporte
runner.run(smoke_test) #Llamar a la suit de prueba