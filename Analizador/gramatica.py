from Interprete.Expresiones.Operaciones.Aritmetica import Aritmetica
from Interprete.Expresiones.Primitivo import Primitivo
from Interprete.Expresiones.Operaciones.Relacionales import Relacionales
from Interprete.Expresiones.Operaciones.Logica import Logica
from Interprete.Expresiones.identificador import Identificador
from Interprete.Instrucciones.Asignacion import Asignacion
from Interprete.Instrucciones.Declaracion import Declaracion
from Interprete.Instrucciones.Estructuras.DeclaracionArreglo import DeclaracionArreglo
from Interprete.Instrucciones.Estructuras.DeclaracionVector import DeclaracionVector
from Interprete.Expresiones.InicializacionVector import InicializacionVector
from Interprete.Expresiones.AccesoArreglo import AccesoArreglo
from Interprete.Expresiones.AccesoVector import AccesoVector
from Interprete.Instrucciones.Estructuras.AsignacionArreglo import AsignacionArreglo
from Interprete.TablaSimbolos.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion
from Interprete.Instrucciones.Println import Pritnln
from Interprete.Instrucciones.SentenciaIf import SentenciaIf
from Interprete.Instrucciones.SentenciaMatch import SentenciaMatch
from Interprete.Instrucciones.BrazoMatch import BrazoMatch
from Interprete.Instrucciones.BucleLoop import BucleLoop
from Interprete.Instrucciones.BucleWhile import BucleWhile
from Interprete.Instrucciones.BucleFor import BucleFor
from Interprete.Instrucciones.RecorridoFor import RecorridoFor
from Interprete.Instrucciones.SentenciaBreak import SentenciaBreak

# Palabras reservadas
reserved = {
    'let': 'LET',
    'mut': 'MUT',
    'i64': 'I64',
    'f64': 'F64',
    'bool': 'BOOL',
    'char': 'CHAR',
    'String': 'STRING',
    'usize': 'USIZE',
    '&str': 'STR',
    'pow': 'POW',
    'powf': 'POWF',
    'as': 'AS',
    'true': 'TRUE',
    'false': 'FALSE',
    'vec': 'VEC',
    'Vec': 'VECN',
    'new': 'NEW',
    'fn': 'FN',
    'println': 'PRINTLN',
    'if': 'IF',
    'else': 'ELSE',
    'match': 'MATCH',
    'loop': 'LOOP',
    'while': 'WHILE',
    'for': 'FOR',
    'in':'IN',
    'break': "BREAK",
    'with': 'WITH',
    'capacity':'CAPACITY',
    'to':'TO',
    'string':'STRINGE'
}
# Simbolos
tokens = list(reserved.values()) + [
    'MAS',
    'POR',
    'DIV',
    'MOD',
    'MENOS',
    'MAYORIGUAL',
    'MAYORQUE',
    'MENORIGUAL',
    'MENORQUE',
    'DIFERENTE',
    'NOT',
    'IGUALIGUAL',
    'IGUAL',
    'OR',
    'AND',
    'PARA',
    'PARC',
    'CORA',
    'CORC',
    'LLAVEA',
    'LLAVEC',
    'COMA',
    'PYC',
    'DOSP',
    'PUNTO',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',
    'ID',
    'GUIONBAJO',
    'ORMATCH',
    'DOSPUNTOSCONTINUO'
]

# Asignacion de tokens
t_MAS = r'\+'
t_POR = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_MENOS = r'-'
t_MAYORIGUAL = r'>='
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MENORQUE = r'<'
t_DIFERENTE = r'!='
t_NOT = r'!'
t_IGUALIGUAL = r'=='
t_IGUAL = r'='
t_OR = r'\|\|'
t_AND = r'&&'
t_PARA = r'\('
t_PARC = r'\)'
t_CORA = r'\['
t_CORC = r']'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_COMA = r','
t_PYC = r';'
t_DOSP = r':'
t_DOSPUNTOSCONTINUO = r'\.\.'
t_PUNTO= r'\.'
t_GUIONBAJO = r'_'
t_ORMATCH = r'\|'


# Expresiones regulares
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error al recibir un decimal %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Error al recibir un entero: ", t.value)
        t.value = 0
    return t


def t_CADENA(t):
    r'"([^"\n]|(\\"))*"'
    # print("Se ha reconocido la cadena: ",t.value)
    return t

def t_CARACTER(t):
    r'\'[a-zA-Z]\''
    print("Se ha reconocido el caracter: ", t.value)
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    try:
        t.type = reserved.get(t.value, "ID")
    except ValueError:
        print("Se esperaba un identificador")
        t.value = 'ERROR'
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Error al leer '%s'" % t.value[0])
    t.lexer.skip(1)


#################INICIAN PRODUCCIONES######################
import Analizador.ply.lex as lex

lexer = lex.lex()

# SE DECLARA LA PRECEDENCIA
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'IGUALIGUAL', 'DIFERENTE', 'MENORQUE', 'MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV'),
    ('right', 'MOD'),
    ('left', 'UMENOS')
)


def p_inicio(t):
    '''inicio : instrucciones
    '''
    t[0] = t[1]
    return t[1]


def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion
                    | instruccion
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])
    return t


def p_instruccion(t):
    '''instruccion : declaracion PYC
                    | asignacion PYC
                    | funcion
                    | impresion PYC
                    | sentencia_if
                    | sentencia_match
                    | bucle_loop
                    | bucle_while
                    | bucle_for
                    | BREAK PYC
    '''
    if t[1] == "break":
        t[0] = SentenciaBreak()
        print(type(t[0]))
    else:
        t[0] = t[1]
    return t


# ======================INSTRUCCION PARA SOLO UNA LINEA MATCH====================================
def p_instrucciones_match(t):
    '''instrucciones_match : instrucciones_match instruccion_match
                    | instruccion_match
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])
    return t


def p_instruccion_match(t):
    '''instruccion_match : declaracion
                        | asignacion
                        | impresion
                        | sentencia_if
                        | sentencia_match
                        | bucle_while
                        | bucle_for
                        | BREAK
    '''
    t[0] = t[1]
    return t


# =============================DECLARACION DE VARIABLES============================================
def p_declaracion(t):
    '''declaracion : LET MUT lista_id DOSP tipo IGUAL expresion
                    | LET MUT lista_id IGUAL expresion
                    | LET lista_id DOSP tipo IGUAL expresion
                    | LET lista_id IGUAL expresion
    '''
    if len(t) == 8:
        tipo = t[5]
    else:
        tipo = t[4]
    if len(t) == 6 and isinstance(t[5],InicializacionVector):   #PRIMERO VALIDAMOS SI LO QUE SE DECLARA ES UN VECTOR
        t[0] = DeclaracionVector(t[3],t[5],"VEC",None,True,None, t.lexer.lineno,1)            #DECLARAR VECTOR MUTABLE

    elif len(t) == 5 and isinstance(t[4],InicializacionVector):
        t[0] = DeclaracionVector(t[2],t[4],"VEC",None,False,None, t.lexer.lineno,1)            #DECLARAR VECTOR NO MUTABLE
    else:
        if len(t) == 8:
            # print("Se reconocio una declaracion con el valor de: ",t[7])
            t[0] = Declaracion(tipo, t[7], t[3], True, t.lexer.lineno, 1)
        elif len(t) == 6:
            # print("Se reconocio una declaracion con el valor de: ", t[5])
            t[0] = Declaracion(None, t[5], t[3], True, t.lexer.lineno, 1)
        elif len(t) == 7:
            # print("Se reconocio una declaracion con el valor de: ", t[6])
            t[0] = Declaracion(tipo, t[6], t[2], False, t.lexer.lineno, 1)
        elif len(t) == 5:
            # print("Se reconocio una declaracion con el valor de: ", t[4])
            t[0] = Declaracion(None, t[4], t[2], False, t.lexer.lineno, 1)
        #print(tipo)
    return t


def p_asignacion(t):
    '''asignacion : ID IGUAL expresion
                    | ID dimensiones_acceso_arreglo IGUAL expresion
    '''
    if len(t) == 4:
        t[0] = Asignacion(t[1], t[3], t.lexer.lineno, 1)
    else:
        t[0] = AsignacionArreglo(t[1],t[2],t[4],t.lexer.lineno,1)
    return t


def p_lista_id(t):
    '''lista_id : ID COMA lista_id
                | ID
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[3])
    return t


def p_tipo(t):
    '''tipo : I64
            | F64
            | BOOL
            | CHAR
            | STRING
            | STR

    '''
    # print("Se reconocio tipo: ",t[1])
    t[0] = Tipo(t[1].upper())
    return t


# ------------------------------ARREGLOS------------------------------------------
def p_declaracion_arreglo(t):
    ''' declaracion : LET MUT lista_id DOSP CORA dimension_arreglo_declaracion CORC IGUAL expresion
                    | LET lista_id DOSP CORA dimension_arreglo_declaracion CORC IGUAL expresion
    '''
    if len(t) == 10:        #t[6/5][0] = dimension del arreglo -- t[6/5] = Estructura del arreglo(tipo de elementos y longitud de los arreglos)
        t[0] = DeclaracionArreglo(t[3], t[9], "ARRAY", t[6][0], t[6],True, t.lexer.lineno, 1)
    elif len(t) == 9:
        t[0] = DeclaracionArreglo(t[2],t[8],"ARRAY",t[5][0],t[5],False ,t.lexer.lineno,1)
    return t


def p_dimension_arreglo_declaracion(t):
    ''' dimension_arreglo_declaracion : dimension_arreglo_declaracion PYC ENTERO
                                    | CORA dimension_arreglo_declaracion PYC ENTERO CORC
                                    | tipo
    '''
    if len(t) == 2:  # t[0][0] = tipo principal del arreglo
        t[0] = []
        t[0].append(t[1])  # t[0][1] = tamaño del sub arreglo
        print(t[0])
    elif len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
        print(t[0])
    else:
        t[0] = t[2]
        t[0].append(t[4])
    return t


def p_dimensiones_acceso_arreglo(t):
    '''dimensiones_acceso_arreglo : dimensiones_acceso_arreglo CORA expresion CORC
                            | CORA expresion CORC
    '''
    print("Se reconocio una dimension con valor")
    if len(t) == 4:
        t[0] = []
        t[0].append(t[2])
    else:
        t[0] = t[1]
        t[0].append(t[3])
    return t


# -------------------------------VECTORES-------------------------------------------
def p_declaracion_vector(t):
    ''' declaracion :  LET MUT lista_id DOSP VECN MENORQUE tipo MAYORQUE IGUAL VECN DOSP DOSP NEW PARA PARC
                    | LET lista_id DOSP VECN MENORQUE tipo MAYORQUE IGUAL VECN DOSP DOSP NEW PARA PARC
                    | LET MUT lista_id DOSP VECN MENORQUE tipo MAYORQUE IGUAL VECN DOSP DOSP WITH GUIONBAJO CAPACITY PARA expresion PARC
                    | LET lista_id DOSP VECN MENORQUE tipo MAYORQUE IGUAL VECN DOSP DOSP WITH GUIONBAJO CAPACITY PARA expresion PARC
    '''

    if t[2] == "mut":
        tipo = t[7]
        mut = True
    else:
        tipo = t[6]
        mut = False
    if len(t) == 19:
        t[0] = DeclaracionVector(t[2], None, "VEC", tipo, mut, t[17], t.lexer.lineno, 1)
    elif len(t) == 18:
        t[0] = DeclaracionVector(t[2], None, "VEC", tipo, mut,t[16], t.lexer.lineno, 1)
    elif len(t) == 16 or len(t) == 15:
        t[0] = DeclaracionVector(t[2], None, "VEC", tipo, mut, 0, t.lexer.lineno, 1)
    #print(tipo)
    return t



# -------------------------FUNCIONES NATIVAS--------------------------------------
def p_impresion(t):
    '''impresion : PRINTLN NOT PARA CADENA PARC
                | PRINTLN NOT PARA CADENA COMA lista_expresiones PARC
    '''
    if len(t) == 6:
        t[0] = Pritnln(t[4], None, t.lexer.lineno, 1)
    elif len(t) == 8:
        t[0] = Pritnln(t[4], t[6], t.lexer.lineno, 1)
    return t


def p_lista_expresion(t):
    '''lista_expresiones : lista_expresiones COMA expresion
                        | expresion
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[3])
    return t


# ------------------------SENTENCIAS DE CONTROL-----------------------------------
# ================================================================================
def p_sentencia_if(t):
    '''sentencia_if : IF expresion LLAVEA instrucciones LLAVEC
                    | IF expresion LLAVEA instrucciones LLAVEC ELSE  sentencia_if
                    | IF expresion LLAVEA instrucciones LLAVEC ELSE LLAVEA instrucciones LLAVEC
    '''
    if len(t) == 6:
        t[0] = SentenciaIf(t[2], t[4], None, t.lexer.lineno, 1)
    elif len(t) == 8:
        t[0] = SentenciaIf(t[2],t[4],[t[7]],t.lexer.lineno,1)
    elif len(t) == 10:
        t[0] = SentenciaIf(t[2], t[4], t[8], t.lexer.lineno, 1)
    return t

def p_sentencia_match(t):
    ''' sentencia_match : MATCH expresion LLAVEA lista_casos_match LLAVEC
                        | MATCH expresion LLAVEA lista_casos_match GUIONBAJO IGUAL MAYORQUE instrucciones_match LLAVEC
                        | MATCH expresion LLAVEA lista_casos_match GUIONBAJO IGUAL MAYORQUE instruccion_match COMA LLAVEC
    '''
    if len(t) == 6:
        t[0] = SentenciaMatch(t[2], t[4], None, t.lexer.lineno, 1)
    else:
        t[0] = SentenciaMatch(t[2], t[4], t[8], t.lexer.lineno, 1)
    return t


def p_lista_casos_match(t):
    ''' lista_casos_match : lista_casos_match caso_match
                        | caso_match
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])
    return t


def p_casos_match(t):
    ''' caso_match : opciones_match IGUAL MAYORQUE LLAVEA instrucciones LLAVEC
                    | opciones_match IGUAL MAYORQUE instruccion_match COMA
    '''
    if len(t) == 7:
        t[0] = BrazoMatch(t[1], t[5], t.lexer.lineno, 1)
    else:
        t[0] = BrazoMatch(t[1], [t[4]], t.lexer.lineno, 1)
    return t


def p_opciones_match(t):
    ''' opciones_match : opciones_match ORMATCH expresion
                        | expresion
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[3])
    return t


# -------------------------------BUCLES-------------------------------------------
# ================================================================================
#CICLO LOOP
def p_loop(t):
    ''' bucle_loop : LOOP LLAVEA instrucciones LLAVEC
    '''
    t[0] = BucleLoop(t[3])
    return t

#CICLO WHILE
def p_while(t):
    ''' bucle_while : WHILE expresion LLAVEA instrucciones LLAVEC
    '''
    t[0] = BucleWhile(t[2], t[4], t.lexer.lineno, 1)
    return t

#CICLO FOR
def p_for(t):
    ''' bucle_for : FOR recorrido_for LLAVEA instrucciones LLAVEC
    '''
    t[0] = BucleFor(t[2],t[4],t.lexer.lineno,1)
    return t

def p_recorrido_for(t):
    ''' recorrido_for : expresion IN expresion
                    | expresion IN expresion DOSPUNTOSCONTINUO expresion
    '''
    if len(t) == 4:
        t[0] = RecorridoFor(t[1],t[3],None,None)
    else:
        t[0] = RecorridoFor(t[1],None,t[3],t[5])
    return t


# ------------------------------FUNCIONES-----------------------------------------
def p_funcion(t):  # ----PENDIENTE------
    ''' funcion : FN ID PARA lista_parametros PARC LLAVEA instrucciones LLAVEC
                | FN ID PARA lista_parametros PARC MENOS MAYORQUE tipo LLAVEA instrucciones LLAVEC
    '''
    if len(t) == 9:
        t[0] = Funcion(t[2],None,t[4],t[7],t.lexer.lineno,1)
    else:
        t[0] = Funcion(t[2],t[8],t[4],t[10],t.lexer.lineno,1)
    return t

def p_lista_parametros(t):  # ----PENDIENTE------
    '''lista_parametros : lista_parametros COMA parametro
                        | parametro
    '''
    if len(t) == 2:
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[3])
    return t


def p_parametro(t):  # ----PENDIENTE------
    '''parametro : ID
    '''


# ===================PRDUCCIONES PARA EXPRESIONES==========================
# ==========================================================================
def p_expresion(t):  # ----PENDIENTE------
    '''expresion : PARA expresion AS tipo PARC
                | PARA expresion PARC
    '''
    if len(t) == 4:
        t[0] = t[2]
    return t


def p_expresion_aritmeticas(t):
    '''expresion : I64 DOSP DOSP POW PARA expresion COMA expresion PARC
                | F64 DOSP DOSP POWF PARA expresion COMA expresion PARC
                | expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | MENOS expresion %prec UMENOS
    '''
    if len(t) == 4:
        t[0] = Aritmetica(t[1], t[3], False, t.lexer.lineno, 1, t[2])
    elif len(t) == 3:
        t[0] = Aritmetica(t[2], None, True, t.lexer.lineno, 1, t[2])
    elif t[4] == "pow":
        t[0] = Aritmetica(t[6], t[8], False, t.lexer.lineno, 1, "^")
    elif t[4] == "powf":
        t[0] = Aritmetica(t[6], t[8], False, t.lexer.lineno, 1, "^^")
    else:
        t[0] = t[1]
    return t


def p_expresion_logica(t):
    '''expresion : NOT expresion %prec NOT
                | expresion AND expresion
                | expresion OR expresion

    '''
    print(len(t))
    if len(t) == 4:
        t[0] = Logica(t[1], t[3], False, t.lexer.lineno, 1, t[2])
    else:
        t[0] = Logica(t[2], None, True, t.lexer.lineno, 1, t[2])
    return t


def p_expresion_relacional(t):
    '''expresion : expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion
                | expresion MENORIGUAL expresion
                | expresion MENORQUE expresion
                | expresion MAYORIGUAL expresion
                | expresion MAYORQUE expresion

    '''
    t[0] = Relacionales(t[1], t[3], False, t.lexer.lineno, 1, t[2])
    return t


def p_expresion_primitivos(t):
    '''expresion : ENTERO
                | DECIMAL
                | CARACTER
                | CADENA
                | CADENA PUNTO TO GUIONBAJO STRINGE PARA PARC
                | TRUE
                | FALSE
    '''
    if type(t[1]) == float:
        tipo = "F64"
    elif type(t[1]) == int:
        tipo = "I64"
    elif t[1] == "true" or t[1] == "false":
        tipo = "BOOL"
    elif type(t[1]) == str:
        if t[1].find("'") != -1:
            #print("HOLLLALALAL")
            tipo = "CHAR"
        elif len(t) == 8:
            tipo = "STRING"
        else:
            tipo = "STR"
    else:
        tipo = "ERROR"
    valor = t[1]
    if tipo == "STRING" or tipo == "CHAR" or tipo == "STR":
        valor = valor[1:-1]
    t[0] = Primitivo(valor, tipo, t.lexer.lineno, 1)
    return t


def p_expresion_id(t):
    ''' expresion : ID
    '''
    t[0] = Identificador(t[1], t.lexer.lineno, 1)


def p_expresion_arreglo(t):
    ''' expresion : CORA lista_expresiones CORC
    '''
    t[0] = t[2]
    return t

def p_acceso_arreglo(t):
    ''' expresion : ID dimensiones_acceso_arreglo
    '''
    #print(t[1])
    #print(t[2])
    t[0] = AccesoArreglo(t[1],t[2],t.lexer.lineno,1)
    return t


def p_dimension_vector_declaracion(t):
    ''' expresion : VEC NOT CORA expresion PYC ENTERO CORC
                | VEC NOT CORA lista_expresiones CORC
    '''
    if len(t) == 8:  # t[0][0] = tipo principal del arreglo
        t[0] = InicializacionVector(t[4],t[6])
    else:
        t[0] = InicializacionVector(t[4],0)
    return t


def p_error(t):
    print("Error sintáctico en '%s'" % t.value, "Linea: %d" % t.lexer.lineno)


import Analizador.ply.yacc as yacc

parser = yacc.yacc()


def analizar_entrada(input):
    # print(input)
    return parser.parse(input)







