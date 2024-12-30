# language: es
@selectores
Característica: selectores
    
  @Clic
  Escenario: Función para hacer clic
    Dado que abro la pagina "https://primeng.org/button"
    Cuando en la página "Primeng" en el elemento "Botón Submit" hago clic

  @IngresarTexto
  Escenario: Función para ingresar texto
    Dado que abro la pagina "https://primeng.org/inputtext"
    Cuando en la página "Primeng" en el elemento "Input" ingreso "Hola Mundo"


  @VerificarTexto
  Escenario: Verificar texto existente
    Dado que abro la pagina "https://primeng.org/autocomplete"
    Cuando en la página "Primeng" busco el texto "backspace"

  @ValidarURL
  Escenario: Validar URL
    Dado que abro la pagina "https://primeng.org/autocomplete"
    Y valido que la pagina sea "https://primeng.org/autocomplete"


  @RecuperarTexto
  Escenario: Recuperar texto de input
    Dado que abro la pagina "https://primeng.org/inputtext"
    Cuando en la página "Primeng" en el elemento "Input" ingreso "Hola Mundo"
    Y recupero el texto de la pagina "Primeng" en el elemento "Input"

    