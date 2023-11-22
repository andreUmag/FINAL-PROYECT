reservadas = {
    "numerito": "NUMERITO",
    "aver": "AVER",
    "mentre": "MENTRE",
    "acto": "ACTO",
    "si": "SI",
    "sinop": "SINOP",
    "untuk": "UNTUK",
    "hasta": "HASTA",
    "funcao": "FUNCAO",
    "coma": "COMA",
    "bool": "BOOL",
    "sisas": "SISAS",
    "nonas": "NONAS",
    "string": "STRING",
}

tokens = [
    "PTCOMA",
    "LLAVIZQ",
    "LLAVDER",
    "PARIZQ",
    "PARDER",
    "IGUAL",
    "MAS",
    "MENOS",
    "POR",
    "DIVIDIDO",
    "CONCAT",
    "MENQUE",
    "MAYQUE",
    "IGUALQUE",
    "NIGUALQUE",
    "DECIMAL",
    "ENTERO",
    "CADENA",
    "ID",
    "TRUE",
    "FALSE",
] + list(reservadas.values())

# Tokens
t_PTCOMA = r";"
t_LLAVIZQ = r"{"
t_LLAVDER = r"}"
t_PARIZQ = r"\("
t_PARDER = r"\)"
t_IGUAL = r"="
t_MAS = r"\+"
t_MENOS = r"-"
t_POR = r"\*"
t_DIVIDIDO = r"/"
t_CONCAT = r"&"
t_MENQUE = r"<"
t_MAYQUE = r">"
t_IGUALQUE = r"=="
t_NIGUALQUE = r"!="
t_COMA = r","

lexical_errors = False


def t_DECIMAL(t):
    r"\d+\.\d+"
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r"\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reservadas.get(t.value.lower(), "ID")
    return t


def t_CADENA(t):
    r"\".*?\" "
    t.value = t.value[1:-1]
    return t


def t_COMENTARIO_MULTILINEA(t):
    r"/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count("\n")


def t_COMENTARIO_SIMPLE(t):
    r"//.*\n"
    t.lexer.lineno += 1


t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



import ply.lex as lex

lexer = lex.lex()



precedence = (
    ("left", "CONCAT"),
    ("left", "MAS", "MENOS"),
    ("left", "POR", "DIVIDIDO"),
    ("right", "UMENOS"),
)

from expresiones import *
from instrucciones import *


def p_init(t):
    "init            : instrucciones"
    t[0] = t[1]


def p_instrucciones_lista(t):
    "instrucciones    : instrucciones instruccion"
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    "instrucciones    : instruccion"
    t[0] = [t[1]]


def p_instruccion(t):
    """instruccion      : aver_instr
    | definicion_instr
    | asignacion_instr
    | mentre_instr
    | si_instr
    | si_sinop_instr
    | untuk_instr
    | acto_mentre_instr
    | call_funcao_instr"""
    t[0] = t[1]


def p_instruccion_aver(t):
    "aver_instr     : AVER PARIZQ expresion PARDER PTCOMA"
    t[0] = aver(t[3])


def p_instruccion_definicion(t):
    "definicion_instr   : NUMERITO ID PTCOMA"
    t[0] = Definicion(t[2])

def p_definition_bool(t):
    """definicion_instr   : BOOL ID PTCOMA
    """
    t[0] = DefinicionBool(t[2])

def p_definition_string(t):
    """definicion_instr   : STRING ID PTCOMA
    """
    t[0] = DefinicionString(t[2])

def p_asignacion_string(t):
    """asignacion_instr   : ID IGUAL expresion_cadena PTCOMA
    """
    t[0] = AsignacionString(t[1], t[3])

def p_asignacion_instr(t):
    """
    asignacion_instr   : ID IGUAL expresion_numerica PTCOMA
                        | ID IGUAL SISAS PTCOMA
                        | ID IGUAL NONAS PTCOMA
    """
    if t[3] == "sisas":
        t[0] = AsignacionBool(t[1], True)
    elif t[3] == "nonas":
        t[0] = AsignacionBool(t[1], False)
    else:
        t[0] = Asignacion(t[1], t[3])


def p_mentre_instr(t):
    "mentre_instr     : MENTRE PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER"
    t[0] = mentre(t[3], t[6])


def p_si_instr(t):
    "si_instr           : SI PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER"
    t[0] = si(t[3], t[6])


def p_si_sinop_instr(t):
    "si_sinop_instr      : SI PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER SINOP LLAVIZQ instrucciones LLAVDER"
    t[0] = sisinop(t[3], t[6], t[10])


def p_untuk_instr(t):
    "untuk_instr : UNTUK ID IGUAL expresion_numerica HASTA expresion_numerica LLAVIZQ instrucciones LLAVDER"
    t[0] = untuk(t[2], t[4], t[6], t[8])


def p_acto_mentre_instr(t):
    "acto_mentre_instr : ACTO LLAVIZQ instrucciones LLAVDER MENTRE PARIZQ expresion_logica PARDER PTCOMA"
    t[0] = ActoMentre(t[3], t[7])

def p_definicion_funcao(t):
    """
    definicion_instr : FUNCAO ID PARIZQ parametros PARDER LLAVIZQ instrucciones LLAVDER
                     | FUNCAO ID PARIZQ PARDER LLAVIZQ instrucciones LLAVDER
    """
    if t[4] == ")":
        t[0] = DefinicionFuncao(t[2], [], t[6])
    else:
        t[0] = DefinicionFuncao(t[2], t[4], t[7])

def p_parametros(t):
    """
    parametros : parametros COMA ID
               | parametros COMA expresion
    
    """
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_single(t):
    """
    parametros : ID
               | expresion
    
    """
    t[0] = [t[1]]

def p_call_funcao(t):
    """
    call_funcao_instr : ID PARIZQ PARDER PTCOMA
                      | ID PARIZQ parametros PARDER PTCOMA
    """
    t[0] = CallFuncao(t[1], t[3] if len(t) > 4 else [])

def p_expresion(t):
    """expresion : expresion_numerica
    | expresion_cadena
    | expresion_booleana"""
    t[0] = t[1]


def p_expresion_booleana(t):
    """expresion_booleana : TRUE
    | FALSE"""
    t[0] = ExpresionBooleana(t[1])


def p_expresion_binaria(t):
    """expresion_numerica : expresion_numerica MAS expresion_numerica
    | expresion_numerica MENOS expresion_numerica
    | expresion_numerica POR expresion_numerica
    | expresion_numerica DIVIDIDO expresion_numerica"""
    if t[2] == "+":
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == "-":
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == "*":
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == "/":
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)


def p_expresion_unaria(t):
    "expresion_numerica : MENOS expresion_numerica %prec UMENOS"
    t[0] = ExpresionNegativo(t[2])


def p_expresion_agrupacion(t):
    "expresion_numerica : PARIZQ expresion_numerica PARDER"
    t[0] = t[2]


def p_expresion_number(t):
    """expresion_numerica : ENTERO
    | DECIMAL"""
    t[0] = Expresionnumerito(t[1])


def p_expresion_id(t):
    "expresion_numerica   : ID"
    t[0] = ExpresionIdentificador(t[1])


def p_expresion_concatenacion(t):
    "expresion_cadena     : expresion_cadena CONCAT expresion_cadena"
    t[0] = ExpresionConcatenar(t[1], t[3])


def p_expresion_cadena(t):
    "expresion_cadena     : CADENA"
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_cadena_numerico(t):
    "expresion_cadena     : expresion_numerica"
    t[0] = ExpresionCadenaNumerico(t[1])


def p_expresion_logica(t):
    """expresion_logica : expresion_numerica MAYQUE expresion_numerica
    | expresion_numerica MENQUE expresion_numerica
    | expresion_numerica IGUALQUE expresion_numerica
    | expresion_numerica NIGUALQUE expresion_numerica"""
    if t[2] == ">":
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == "<":
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == "==":
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == "!=":
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)



import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)

def check_lexical(input_text):
    lexer.input(input_text)
    tok = lexer.token()

            

        



