from selenium.webdriver.common.by import By

primeng = {
    "Botón Submit": (By.XPATH,"/html/body/app-root/app-main/div/div[2]/div/ng-component/app-doc/div/div/app-docfeaturessection/div/app-docsection/section[2]/button-basic-demo/div/p-button/button/span"),
    "Input": (By.XPATH,"/html/body/app-root/app-main/div/div[2]/div/ng-component/app-doc/div/div/app-docfeaturessection/div/app-docsection/section[2]/basic-doc/div/input"),
    "input_locator": (By.XPATH, '/html/body/app-root/app-main/div/div[2]/div/ng-component/app-doc/div/div/app-docfeaturessection/div/app-docsection/section[4]/dropdown-doc/div/p-autocomplete/div/input'),
    "lista_opciones_locator": (By.CSS_SELECTOR, "ul.p-autocomplete-items li"),
}