from behave import given, when, then

from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA

from pages.index import selectors

import time


@when('en la página "{page}" en el elemento "{element}" ingreso "{value}"')
def step_impl(context, page, element, value):
    FAW.enviar_datos(context.driver, selectors[page][element], value)
    RA.agregar_captura_reporte(context)


@when('en la página "{page}" en el elemento "{element}" hago clic')
def step_impl(context, page, element):
    FAW.clic(context.driver, selectors[page][element])

    RA.agregar_captura_reporte(context)


@given('que abro la pagina "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    RA.agregar_captura_reporte(context)

