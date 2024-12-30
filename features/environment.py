from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from utils import functions_auxiliar_web as FAW
import time 

def before_all(context):
    download_ruta = os.path.abspath("./files/download")
    ##################################
    chrome_options = Options()
    chrome_prefs = {
        "download.default_directory": download_ruta,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True, 
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    context.driver = webdriver.Chrome(options=chrome_options)
    ##################################

def before_feature(context, feature):
    pass
    
def before_step(context, step):
    context.current_step_name = step.name

    
def after_feature(context, feature):
    pass

def after_all(context):
    context.driver.quit()
