import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *

def procesar_aver(instr, ts) :
    print('> ', resolver_cadena(instr.cad, ts))

def procesar_definicion(instr, ts) :
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.numerito, 0)      # inicializamos con 0 como valor por defecto
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts) :
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.numerito, val)
    ts.actualizar(simbolo)

def procesar_mentre(instr, ts) :
    while resolver_expreision_logica(instr.expLogica, ts) :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_chi(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_chi_chinop(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local)
    else :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfFalso, ts_local)

def procesar_untuk(instr, ts) :
    inicio = resolver_expresion_aritmetica(instr.inicio, ts)
    fin = resolver_expresion_aritmetica(instr.fin, ts)

    for i in range(inicio, fin + 1):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        ts_local.agregar(TS.Simbolo(instr.variable, TS.TIPO_DATO.numerito, i))
        procesar_instrucciones(instr.instrucciones, ts_local)


def resolver_cadena(expCad, ts) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')


def resolver_expreision_logica(expLog, ts) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, Expresionnumerito) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor


def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, aver) : procesar_aver(instr, ts)
        elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
        elif isinstance(instr, mentre) : procesar_mentre(instr, ts)
        elif isinstance(instr, chi) : procesar_chi(instr, ts)
        elif isinstance(instr, ChiChinop) : procesar_chi_chinop(instr, ts)
        elif isinstance(instr, untuk) : procesar_untuk(instr, ts)
        else : print('Error: instrucción no válida')




f = open("static/scripts/ply/entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global)
