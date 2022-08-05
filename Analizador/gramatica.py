
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
    'as':'AS',
    'vec':'VEC',
    'Vec':'VECN',
    'fn':'FN'
}

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

def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion
                    | instruccion
    '''

def p_instruccion(t):
    '''instruccion : declaracion PYC
                    | asignacion PYC
                    | funcion
    '''

def p_declaracion(t):
    '''declaracion : LET MUT ID DOSP tipo IGUAL expresion
                    | LET MUT ID IGUAL expresion
                    | LET ID DOSP tipo IGUAL expresion
                    | LET ID IGUAL expresion
    '''
    print("Se reconocio una declaracion con el valor de: ",t[7])

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
    '''expresion : I64 DOSP DOSP POW PARA expresion COMA expresion PARC
                | F64 DOSP DOSP POW PARA expresion COMA expresion PARC
                | expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion
                | expresion MENORIGUAL expresion
                | expresion MENORQUE expresion
                | expresion MAYORIGUAL expresion
                | expresion MAYORQUE expresion
                | NOT expresion %prec NOT
                | MENOS expresion %prec UMENOS
                | expresion AND expresion
                | expresion OR expresion
                | PARA expresion AS tipo PARC
                | PARA expresion PARC
                | ID CORA expresion CORC
                | ENTERO
                | DECIMAL
                | CADENA
    '''
    if len(t) <= 2:
        t[0] = t[1]
    else:
        if t[2] == '+':
            t[0] = t[1] + t[3]
        else:
            t[0] = t[1]


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)



import Analizador.ply.yacc as yacc

parser = yacc.yacc()

def analizar_entrada(input):
    print(input)
    parser.parse(input)






