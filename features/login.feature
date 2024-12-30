# language: es
@inicio_sesion
Característica: Inicio sesion

  Antecedentes:
    Dado que abro la pagina "https://www.saucedemo.com/v1/"

  @inicio_sesion_correcto
  Escenario: Inicio sesion correcto
    Cuando en la página "Inicio de sesion" en el elemento "Nombre de usuario" ingreso "standard_user"
    Cuando en la página "Inicio de sesion" en el elemento "Contraseña" ingreso "secret_sauce"
    Cuando en la página "Inicio de sesion" en el elemento "Iniciar sesion" hago clic

    