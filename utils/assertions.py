import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils import errors as ERR

def asercion_titulo_pagina(context, titulo):
    titulo_actual = context.title
    assert titulo == titulo_actual, f"El titulo esperado era '{titulo}', pero el titulo de la pagina es '{titulo_actual}'"

def asercion_dato_no_vacio(dato):
    assert dato != "", f"El dato introducido esta vacío"

def verificar_url(context,url):
    url_actual = context.current_url
    assert url_actual == url, f"La URL esperada era '{url}', pero la URL actual es '{url_actual}'"

def verificar_archivo_descargado(nombre_archivo):
    time.sleep(5)
    ruta_descarga = r"./files/download"
    ruta_completa = os.path.join(ruta_descarga, nombre_archivo)
    if os.path.isfile(ruta_completa):
        print("archivo descargado")
    else:
        raise AssertionError (f"No se pudo descargar el archivo '{nombre_archivo}'")
    
def verificar_exitencia_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        raise AssertionError (f"El archivo '{archivo}' no existe")
    
def verificar_texto_en_pagina(driver, texto, tiempo_espera=10):
    try:
        WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        body_text = driver.find_element(By.TAG_NAME, "body").text
        
        if texto in body_text:
            print(f"El texto '{texto}' se encontró en la página.")
            return True
        else:
            ERR.validacion(f"El texto '{texto}' NO se encontró en la página.")
            raise AssertionError(f"El texto '{texto}' no se encontró en la página.")
    except Exception as e:
        print(f"Error al verificar el texto en la página: {e}")
        raise e      


