class Instruccion:
    """This is an abstract class"""


class aver(Instruccion):
    """
    Esta clase representa la instrucción aver.
    La instrucción aver únicamente tiene como parámetro una cadena
    """

    def __init__(self, cad):
        self.cad = cad


class mentre(Instruccion):
    """
    Esta clase representa la instrucción mentre.
    La instrucción mentre recibe como parámetro una expresión lógica y la lista
    de instrucciones a ejecutar si la expresión lógica es verdadera.
    """

    def __init__(self, expLogica, instrucciones=[]):
        self.expLogica = expLogica
        self.instrucciones = instrucciones


class untuk(Instruccion):
    def __init__(self, variable, inicio, fin, instrucciones):
        self.variable = variable
        self.inicio = inicio
        self.fin = fin
        self.instrucciones = instrucciones


class Definicion(Instruccion):
    """
    Esta clase representa la instrucción de definición de variables.
    Recibe como parámetro el nombre del identificador a definir
    """

    def __init__(self, id):
        self.id = id

class DefinicionBool(Instruccion):
    """
    Esta clase representa la instrucción de definición de variables.
    Recibe como parámetro el nombre del identificador a definir
    """

    def __init__(self, id):
        self.id = id

class CallFuncao(Instruccion):
    """
    Esta clase representa la instrucción de llamada a funciones.
    Recibe como parámetro el nombre del identificador a definir
    """

    def __init__(self, id, parametros):
        self.id = id
        if isinstance(parametros, str):
            self.parametros = parametros.split(",")
        else:
            self.parametros = parametros
        

class DefinicionFuncao(Instruccion):
    def __init__(self, id, parametros, instrucciones):
        self.id = id
        if isinstance(parametros, str):
            self.parametros = parametros.split(",")
        else:
            # Si parametros no es una cadena, podría manejarlo de otra manera según tus necesidades.
            self.parametros = parametros
        self.instrucciones = instrucciones

class DefinicionString(Instruccion):
    def __init__(self, id):
        self.id = id

class Asignacion(Instruccion):
    """
    Esta clase representa la instrucción de asignación de variables
    Recibe como parámetro el identificador a asignar y el valor que será asignado.
    """

    def __init__(self, id, expNumerica):
        self.id = id
        self.expNumerica = expNumerica

class AsignacionBool(Instruccion):

    def __init__(self, id, bool):
        self.id = id
        self.bool = bool

class AsignacionString(Instruccion):
    def __init__(self, id, expCadena):
        self.id = id
        self.expCadena = expCadena

class si(Instruccion):
    """
    Esta clase representa la instrucción if.
    La instrucción if recibe como parámetro una expresión lógica y la lista
    de instrucciones a ejecutar si la expresión lógica es verdadera.
    """

    def __init__(self, expLogica, instrucciones=[]):
        self.expLogica = expLogica
        self.instrucciones = instrucciones


class sisinop(Instruccion):
    """
    Esta clase representa la instrucción if-else.
    La instrucción if-else recibe como parámetro una expresión lógica y la lista
    de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
    a ejecutar si la expresión lógica es falsa.
    """

    def __init__(self, expLogica, instrIfVerdadero=[], instrIfFalso=[]):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class ActoMentre(Instruccion):
    """
    Esta clase representa la instrucción do-while (acto mentre).

    Parámetros:
        - instrucciones: Lista de instrucciones a ejecutar al menos una vez y luego repetir mientras la expresión lógica sea verdadera.
        - exp_logica: Expresión lógica que se evalúa después de ejecutar las instrucciones. El bucle se repite mientras esta expresión sea verdadera.
    """

    def __init__(self, instrucciones, exp_logica):
        self.instrucciones = instrucciones
        self.exp_logica = exp_logica
