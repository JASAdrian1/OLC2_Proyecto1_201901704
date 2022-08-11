from Interprete.Expresiones.Operaciones.Aritmetica import Aritmetica
from Interprete.Expresiones.Primitivo import Primitivo

#Palabras reservadas
reserved = {
    'let':'LET',
    'mut':'MUT',
    'i64':'I64',
    'f64':'F64',
    'bool':'BOOL',
    'char':'CHAR',
    'String':'STRING',
    'usize':'USIZE',
    '&str':'STR',
    'pow':'POW',
    'powf':'POWF',
    'as':'AS',
    'vec':'VEC',
    'Vec':'VECN',
    'fn':'FN'
}
#Simbolos
tokens = [
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
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'ID'
] + list(reserved.values())



#Asignacion de tokens
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


#Expresiones regulares
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
    #print("Se ha reconocido la cadena: ",t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    try:
        t.type = reserved.get(t.value,"ID")
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

#SE DECLARA LA PRECEDENCIA
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','NOT'),
    ('left','IGUALIGUAL','DIFERENTE','MENORQUE','MAYORQUE','MENORIGUAL','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV'),
    ('right','MOD'),
    ('left','UMENOS')
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
    '''
    t[0] = t[1]
    return t

def p_declaracion(t):
    '''declaracion : LET MUT ID DOSP tipo IGUAL expresion
                    | LET MUT ID IGUAL expresion
                    | LET ID DOSP tipo IGUAL expresion
                    | LET ID IGUAL expresion
    '''
    print("Se reconocio una declaracion con el valor de: ",t[7])
    t[0] = t[7]
    return t

def p_asignacion(t):
    '''asignacion : ID IGUAL expresion
                    | ID dimensiones_arreglo IGUAL expresion
    '''



def p_tipo(t):
    '''tipo : I64
            | F64
            | BOOL
            | CHAR
            | STRING
            | STR
    '''
    print("Se reconocio tipo: ",t[1])


#------------------------------FUNCIONES-----------------------------------------
def p_funcion(t):
    ''' funcion : FN ID PARA lista_parametros PARC LLAVEA instrucciones LLAVEC
                | FN ID PARA lista_parametros PARC MENOS MAYORQUE tipo LLAVEA instrucciones LLAVEC
    '''

def p_lista_parametros(t):
    '''lista_parametros : lista_parametros COMA parametro
                        | parametro
    '''

def p_parametro(t):
    '''parametro : ID
    '''

def p_dimensiones_arreglo(t):
    '''dimensiones_arreglo : CORA expresion CORC dimensiones_arreglo
                            | CORA expresion CORC
    '''
    print("Se reconocio una dimension con valor")

def p_expresion(t):
    '''expresion : PARA expresion AS tipo PARC
                | PARA expresion PARC
                | ID CORA expresion CORC
    '''
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
    if len(t) <=4:
        t[0] = Aritmetica(t[1],t[3],False,t.lexer.lineno,1,t[2])
    elif t[4] == "pow":
        t[0] = Aritmetica(t[6],t[8],False,t.lexer.lineno,1,"^")
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

def p_expresion_relacional(t):
    '''expresion : expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion
                | expresion MENORIGUAL expresion
                | expresion MENORQUE expresion
                | expresion MAYORIGUAL expresion
                | expresion MAYORQUE expresion

    '''
    return t

def p_expresion_primitivos(t):
    '''expresion : ENTERO
                | DECIMAL
                | CADENA
    '''
    if type(t[1]) == float:
        tipo = "F64"
    elif type(t[1]) == int:
        tipo = "I64"
    else:
        tipo = "ERROR"
    t[0] = Primitivo(t[1], tipo, t.lexer.lineno, 1)
    return t

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)



import Analizador.ply.yacc as yacc

parser = yacc.yacc()

def analizar_entrada(input):
    print(input)
    return parser.parse(input)







