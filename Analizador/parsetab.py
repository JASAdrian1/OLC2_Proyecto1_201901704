
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftIGUALIGUALDIFERENTEMENORQUEMAYORQUEMENORIGUALMAYORIGUALleftMASMENOSleftPORDIVrightMODleftUMENOSAND AS BOOL CADENA CHAR COMA CORA CORC DECIMAL DIFERENTE DIV DOSP ENTERO F64 FALSE FN I64 ID IGUAL IGUALIGUAL LET LLAVEA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MOD MUT NOT OR PARA PARC POR POW POWF PYC STR STRING TRUE USIZE VEC VECNinicio : instrucciones\n    instrucciones : instrucciones instruccion\n                    | instruccion\n    instruccion : declaracion PYC\n                    | asignacion PYC\n                    | funcion\n    declaracion : LET MUT ID DOSP tipo IGUAL expresion\n                    | LET MUT ID IGUAL expresion\n                    | LET ID DOSP tipo IGUAL expresion\n                    | LET ID IGUAL expresion\n    asignacion : ID IGUAL expresion\n                    | ID dimensiones_arreglo IGUAL expresion\n    tipo : I64\n            | F64\n            | BOOL\n            | CHAR\n            | STRING\n            | STR\n     funcion : FN ID PARA lista_parametros PARC LLAVEA instrucciones LLAVEC\n                | FN ID PARA lista_parametros PARC MENOS MAYORQUE tipo LLAVEA instrucciones LLAVEC\n    lista_parametros : lista_parametros COMA parametro\n                        | parametro\n    parametro : ID\n    dimensiones_arreglo : CORA expresion CORC dimensiones_arreglo\n                            | CORA expresion CORC\n    expresion : PARA expresion AS tipo PARC\n                | PARA expresion PARC\n                | ID CORA expresion CORC\n    expresion : I64 DOSP DOSP POW PARA expresion COMA expresion PARC\n                | F64 DOSP DOSP POWF PARA expresion COMA expresion PARC\n                | expresion MAS expresion\n                | expresion MENOS expresion\n                | expresion POR expresion\n                | expresion DIV expresion\n                | expresion MOD expresion\n                | MENOS expresion %prec UMENOS\n    expresion : NOT expresion %prec NOT\n                | expresion AND expresion\n                | expresion OR expresion\n\n    expresion : expresion IGUALIGUAL expresion\n                | expresion DIFERENTE expresion\n                | expresion MENORIGUAL expresion\n                | expresion MENORQUE expresion\n                | expresion MAYORIGUAL expresion\n                | expresion MAYORQUE expresion\n\n    expresion : ENTERO\n                | DECIMAL\n                | CADENA\n                | TRUE\n                | FALSE\n    '
    
_lr_action_items = {'LET':([0,2,3,6,10,11,12,101,108,112,116,119,122,],[7,7,-3,-6,-2,-4,-5,7,7,-19,7,7,-20,]),'ID':([0,2,3,6,7,9,10,11,12,13,15,17,21,24,27,28,34,36,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,94,95,101,106,107,108,112,114,115,116,119,122,],[8,8,-3,-6,14,18,-2,-4,-5,19,22,22,22,22,22,22,22,68,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,68,22,8,22,22,8,-19,22,22,8,8,-20,]),'FN':([0,2,3,6,10,11,12,101,108,112,116,119,122,],[9,9,-3,-6,-2,-4,-5,9,9,-19,9,9,-20,]),'$end':([1,2,3,6,10,11,12,112,122,],[0,-1,-3,-6,-2,-4,-5,-19,-20,]),'LLAVEC':([3,6,10,11,12,108,112,119,122,],[-3,-6,-2,-4,-5,112,-19,122,-20,]),'PYC':([4,5,23,29,30,31,32,33,46,64,65,66,72,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,120,121,],[11,12,-11,-46,-47,-48,-49,-50,-10,-36,-37,-12,-8,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,-9,-28,-7,-26,-29,-30,]),'MUT':([7,],[13,]),'IGUAL':([8,14,16,19,39,40,41,42,43,44,45,67,71,92,],[15,21,34,38,73,-13,-14,-15,-16,-17,-18,-25,95,-24,]),'CORA':([8,22,67,],[17,47,17,]),'DOSP':([14,19,25,26,62,63,],[20,37,62,63,90,91,]),'PARA':([15,17,18,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,99,100,106,107,114,115,],[24,24,36,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,106,107,24,24,24,24,]),'I64':([15,17,20,21,24,27,28,34,37,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,88,95,106,107,109,114,115,],[25,25,40,25,25,25,25,25,40,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,40,25,25,25,40,25,25,]),'F64':([15,17,20,21,24,27,28,34,37,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,88,95,106,107,109,114,115,],[26,26,41,26,26,26,26,26,41,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,41,26,26,26,41,26,26,]),'MENOS':([15,17,21,23,24,27,28,29,30,31,32,33,34,35,38,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,93,95,96,97,104,105,106,107,110,111,114,115,117,118,120,121,],[27,27,27,49,27,27,27,-46,-47,-48,-49,-50,27,49,27,49,27,27,27,27,27,27,27,27,27,27,27,27,27,27,49,-36,49,49,49,27,49,-31,-32,-33,-34,-35,49,49,49,49,49,49,49,49,-27,102,27,49,-28,49,-26,27,27,49,49,27,27,49,49,-29,-30,]),'NOT':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ENTERO':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DECIMAL':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CADENA':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TRUE':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FALSE':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'BOOL':([20,37,88,109,],[42,42,42,42,]),'CHAR':([20,37,88,109,],[43,43,43,43,]),'STRING':([20,37,88,109,],[44,44,44,44,]),'STR':([20,37,88,109,],[45,45,45,45,]),'MAS':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[48,-46,-47,-48,-49,-50,48,48,48,-36,48,48,48,48,-31,-32,-33,-34,-35,48,48,48,48,48,48,48,48,-27,48,-28,48,-26,48,48,48,48,-29,-30,]),'POR':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[50,-46,-47,-48,-49,-50,50,50,50,-36,50,50,50,50,50,50,-33,-34,-35,50,50,50,50,50,50,50,50,-27,50,-28,50,-26,50,50,50,50,-29,-30,]),'DIV':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[51,-46,-47,-48,-49,-50,51,51,51,-36,51,51,51,51,51,51,-33,-34,-35,51,51,51,51,51,51,51,51,-27,51,-28,51,-26,51,51,51,51,-29,-30,]),'MOD':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[52,-46,-47,-48,-49,-50,52,52,52,-36,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-27,52,-28,52,-26,52,52,52,52,-29,-30,]),'AND':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[53,-46,-47,-48,-49,-50,53,53,53,-36,-37,53,53,53,-31,-32,-33,-34,-35,-38,53,-40,-41,-42,-43,-44,-45,-27,53,-28,53,-26,53,53,53,53,-29,-30,]),'OR':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[54,-46,-47,-48,-49,-50,54,54,54,-36,-37,54,54,54,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,54,-28,54,-26,54,54,54,54,-29,-30,]),'IGUALIGUAL':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[55,-46,-47,-48,-49,-50,55,55,55,-36,55,55,55,55,-31,-32,-33,-34,-35,55,55,-40,-41,-42,-43,-44,-45,-27,55,-28,55,-26,55,55,55,55,-29,-30,]),'DIFERENTE':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[56,-46,-47,-48,-49,-50,56,56,56,-36,56,56,56,56,-31,-32,-33,-34,-35,56,56,-40,-41,-42,-43,-44,-45,-27,56,-28,56,-26,56,56,56,56,-29,-30,]),'MENORIGUAL':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[57,-46,-47,-48,-49,-50,57,57,57,-36,57,57,57,57,-31,-32,-33,-34,-35,57,57,-40,-41,-42,-43,-44,-45,-27,57,-28,57,-26,57,57,57,57,-29,-30,]),'MENORQUE':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[58,-46,-47,-48,-49,-50,58,58,58,-36,58,58,58,58,-31,-32,-33,-34,-35,58,58,-40,-41,-42,-43,-44,-45,-27,58,-28,58,-26,58,58,58,58,-29,-30,]),'MAYORIGUAL':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,104,105,110,111,117,118,120,121,],[59,-46,-47,-48,-49,-50,59,59,59,-36,59,59,59,59,-31,-32,-33,-34,-35,59,59,-40,-41,-42,-43,-44,-45,-27,59,-28,59,-26,59,59,59,59,-29,-30,]),'MAYORQUE':([23,29,30,31,32,33,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,96,97,102,104,105,110,111,117,118,120,121,],[60,-46,-47,-48,-49,-50,60,60,60,-36,60,60,60,60,-31,-32,-33,-34,-35,60,60,-40,-41,-42,-43,-44,-45,-27,60,-28,109,60,-26,60,60,60,60,-29,-30,]),'CORC':([29,30,31,32,33,35,64,65,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,97,105,120,121,],[-46,-47,-48,-49,-50,67,-36,-37,97,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,-28,-26,-29,-30,]),'AS':([29,30,31,32,33,61,64,65,75,76,77,78,79,80,81,82,83,84,85,86,87,89,97,105,120,121,],[-46,-47,-48,-49,-50,88,-36,-37,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,-28,-26,-29,-30,]),'PARC':([29,30,31,32,33,40,41,42,43,44,45,61,64,65,68,69,70,75,76,77,78,79,80,81,82,83,84,85,86,87,89,97,98,103,105,117,118,120,121,],[-46,-47,-48,-49,-50,-13,-14,-15,-16,-17,-18,89,-36,-37,-23,93,-22,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,-28,105,-21,-26,120,121,-29,-30,]),'COMA':([29,30,31,32,33,64,65,68,69,70,75,76,77,78,79,80,81,82,83,84,85,86,87,89,97,103,105,110,111,120,121,],[-46,-47,-48,-49,-50,-36,-37,-23,94,-22,-31,-32,-33,-34,-35,-38,-39,-40,-41,-42,-43,-44,-45,-27,-28,-21,-26,114,115,-29,-30,]),'LLAVEA':([40,41,42,43,44,45,93,113,],[-13,-14,-15,-16,-17,-18,101,116,]),'POW':([90,],[99,]),'POWF':([91,],[100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,101,116,],[2,108,119,]),'instruccion':([0,2,101,108,116,119,],[3,10,3,10,3,10,]),'declaracion':([0,2,101,108,116,119,],[4,4,4,4,4,4,]),'asignacion':([0,2,101,108,116,119,],[5,5,5,5,5,5,]),'funcion':([0,2,101,108,116,119,],[6,6,6,6,6,6,]),'dimensiones_arreglo':([8,67,],[16,92,]),'expresion':([15,17,21,24,27,28,34,38,47,48,49,50,51,52,53,54,55,56,57,58,59,60,73,95,106,107,114,115,],[23,35,46,61,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,96,104,110,111,117,118,]),'tipo':([20,37,88,109,],[39,71,98,113,]),'lista_parametros':([36,],[69,]),'parametro':([36,94,],[70,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','gramatica.py',155),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',161),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','gramatica.py',162),
  ('instruccion -> declaracion PYC','instruccion',2,'p_instruccion','gramatica.py',173),
  ('instruccion -> asignacion PYC','instruccion',2,'p_instruccion','gramatica.py',174),
  ('instruccion -> funcion','instruccion',1,'p_instruccion','gramatica.py',175),
  ('declaracion -> LET MUT ID DOSP tipo IGUAL expresion','declaracion',7,'p_declaracion','gramatica.py',181),
  ('declaracion -> LET MUT ID IGUAL expresion','declaracion',5,'p_declaracion','gramatica.py',182),
  ('declaracion -> LET ID DOSP tipo IGUAL expresion','declaracion',6,'p_declaracion','gramatica.py',183),
  ('declaracion -> LET ID IGUAL expresion','declaracion',4,'p_declaracion','gramatica.py',184),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_asignacion','gramatica.py',191),
  ('asignacion -> ID dimensiones_arreglo IGUAL expresion','asignacion',4,'p_asignacion','gramatica.py',192),
  ('tipo -> I64','tipo',1,'p_tipo','gramatica.py',198),
  ('tipo -> F64','tipo',1,'p_tipo','gramatica.py',199),
  ('tipo -> BOOL','tipo',1,'p_tipo','gramatica.py',200),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica.py',201),
  ('tipo -> STRING','tipo',1,'p_tipo','gramatica.py',202),
  ('tipo -> STR','tipo',1,'p_tipo','gramatica.py',203),
  ('funcion -> FN ID PARA lista_parametros PARC LLAVEA instrucciones LLAVEC','funcion',8,'p_funcion','gramatica.py',210),
  ('funcion -> FN ID PARA lista_parametros PARC MENOS MAYORQUE tipo LLAVEA instrucciones LLAVEC','funcion',11,'p_funcion','gramatica.py',211),
  ('lista_parametros -> lista_parametros COMA parametro','lista_parametros',3,'p_lista_parametros','gramatica.py',215),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','gramatica.py',216),
  ('parametro -> ID','parametro',1,'p_parametro','gramatica.py',220),
  ('dimensiones_arreglo -> CORA expresion CORC dimensiones_arreglo','dimensiones_arreglo',4,'p_dimensiones_arreglo','gramatica.py',224),
  ('dimensiones_arreglo -> CORA expresion CORC','dimensiones_arreglo',3,'p_dimensiones_arreglo','gramatica.py',225),
  ('expresion -> PARA expresion AS tipo PARC','expresion',5,'p_expresion','gramatica.py',230),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion','gramatica.py',231),
  ('expresion -> ID CORA expresion CORC','expresion',4,'p_expresion','gramatica.py',232),
  ('expresion -> I64 DOSP DOSP POW PARA expresion COMA expresion PARC','expresion',9,'p_expresion_aritmeticas','gramatica.py',237),
  ('expresion -> F64 DOSP DOSP POWF PARA expresion COMA expresion PARC','expresion',9,'p_expresion_aritmeticas','gramatica.py',238),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmeticas','gramatica.py',239),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmeticas','gramatica.py',240),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_aritmeticas','gramatica.py',241),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_aritmeticas','gramatica.py',242),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_aritmeticas','gramatica.py',243),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmeticas','gramatica.py',244),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',257),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',258),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',259),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',266),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_relacional','gramatica.py',267),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',268),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_relacional','gramatica.py',269),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',270),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_relacional','gramatica.py',271),
  ('expresion -> ENTERO','expresion',1,'p_expresion_primitivos','gramatica.py',278),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_primitivos','gramatica.py',279),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitivos','gramatica.py',280),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitivos','gramatica.py',281),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitivos','gramatica.py',282),
]
