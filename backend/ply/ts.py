from enum import Enum


class TIPO_DATO(Enum):
    numerito = 1
    function = 2
    bool = 3
    string = 4


class Simbolo:
    def __init__(self, id, tipo, valor, parametros=None):
        self.id = id
        self.tipo_dato = tipo
        self.valor = valor
        self.parametros = parametros if parametros is not None else []



class TablaDeSimbolos:
    "Esta clase representa la tabla de simbolos"

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print("Error: variable ", id, " no definida.")

        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos:
            print("Error: variable ", simbolo.id, " no definida.")
        else:
            self.simbolos[simbolo.id] = simbolo
    
    def borrar(self, id):
        if not id in self.simbolos:
            print("Error: variable ", id, " no definida.")
        else:
            del self.simbolos[id]


