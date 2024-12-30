from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from utils import errors as ERR
from selenium.webdriver.common.by import By
import time
import os

def clic(driver, web_elemento, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.element_to_be_clickable(web_elemento)
    )
    element.click()


def enviar_datos(driver, web_elemento, texto, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    element.send_keys(texto)

def limpiar(driver, web_elemento, tiempo_espera=10):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    content = element.get_attribute('value')
    content_length = len(content)
    element.send_keys(Keys.BACKSPACE * content_length)


def clic_elemento_por_texto(driver, web_elemento, texto, tiempo_espera=10):
    elements = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_all_elements_located(web_elemento)
    )
    for element in elements:
        if element.text == texto:
            element.click()
            return

def elemento_presente(driver, web_elemento, tiempo_espera=10):
    try:
        WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        return True
    except TimeoutException:
        return False

def obtener_archivo_carpeta(archivo):
    carpeta = os.path.abspath("./files/upload")
    ruta_completa = os.path.join(carpeta,archivo)
    if os.path.isfile(ruta_completa):
        return ruta_completa
    else:
        raise Exception("El archivo no existe")
    
def validar_elemento(driver,web_elemento,mensaje_error_web,tiempo_espera=3):
    try:
        elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        try:
            elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(mensaje_error_web)
            )
            if elemento.is_displayed():
                message = elemento.text
                ERR.validacion(web_elemento,message)
        except TimeoutException:
            ERR.elemento_no_encontrado(web_elemento)
    except TimeoutException:
        ERR.elemento_no_encontrado(web_elemento)
    except Exception as e:
        raise e

def seleccionar_opcion_autocompletado(driver, web_elemento, texto, tiempo_espera=10):
    try:
        input_element = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        
        input_element.clear()
        input_element.send_keys(texto)
        
        opciones = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.p-autocomplete-items li'))
        )
        
        for opcion in opciones:
            if texto in opcion.text:
                opcion.click() 
                return
        
        print(f"No se encontró la opción: {texto}")
        
    except TimeoutException:
        print(f"Se agotó el tiempo esperando el autocompletado para el texto: {texto}")
    except Exception as e:
        print(f"Error al seleccionar la opción del autocompletado: {e}")

    
def esperar(tiempo_respera):
    time.sleep(tiempo_respera)

    
def obtener_y_guardar_valor_input(driver, web_elemento, nombre_archivo, tiempo_espera=10):
    try:
        element = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )

        input_value = element.get_attribute('value')

        print(f"El valor '{input_value}' ha sido guardado en el archivo '{nombre_archivo}'")
        return input_value

    except Exception as e:
        ERR.error_ocurrido("No se pudo obtener el valor del elemento")