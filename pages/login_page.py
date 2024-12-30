from selenium.webdriver.common.by import By

login = {
    "Nombre de usuario": (By.ID, "user-name"),
    "Contraseña": (By.ID, "password"),
    "Iniciar sesion": (By.ID, "login-button")
}