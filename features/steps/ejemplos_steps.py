from behave import when,given
from selenium.webdriver.common.by import By
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from utils import assertions as ASS
from pages.index import selectors

@when('en la página "{page}" en el elemento "{element}" selecciono "{datos}"')
def step_impl(context,page,element,datos):
    FAW.seleccionar_opcion_autocompletado(context.driver,selectors[page][element],datos)
    RA.agregar_captura_reporte(context)

@when('en la página "{page}" busco el texto "{texto}"')
def step_impl(context,page,texto):
    ASS.verificar_texto_en_pagina(context.driver,texto)
    RA.agregar_captura_reporte(context)

@given('valido que la pagina sea "{url_esperada}"')
def step_impl(context,url_esperada):
    ASS.verificar_url(context.driver,url_esperada)
    RA.agregar_captura_reporte(context)


@when('recupero el texto de la pagina "{page}" en el elemento "{selector}"')
def step_impl(context, page, selector):
    FAW.obtener_y_guardar_valor_input(context.driver,selectors[page][selector],"Prueba")
    RA.agregar_captura_reporte(context)