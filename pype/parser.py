import ply.yacc

from .lexer import tokens,reserved
from .ast import *

# Here's an example production rule which constructs an AST node
def p_program(p):
  r'program : statement_list'
  p[0] = ASTProgram(p[1])

# Here's an example production rule which simply aggregates lists of AST nodes.
def p_statement_list(p):
  r'''statement_list : statement_list component
                     | statement_list import_statement
                     | import_statement
                     | component'''
  if len(p)>2:
    p[1].append(p[2])
    p[0] = p[1]
  else:
    p[0] = [p[1]]

# TODO Implement production rules for all other grammar rules and construct a
#      full AST.

  r'import_statement : LPAREN IMPORT ID RPAREN'

  r'''component : LBRACE ID expression_list RBRACE'''

  r'''expression_list : expression_list expression
                      | expression'''

  r'''expression : LPAREN INPUT declaration_list RPAREN
                 | LPAREN INPUT RPAREN'''

  r'''expression : LPAREN OUTPUT declaration_list RPAREN
                 | LPAREN OUTPUT RPAREN'''

  r'''declaration_list : declaration_list declaration
                       | declaration'''

  r'''declaration : LPAREN type ID RPAREN
                  | ID'''

  r'''type : ID'''

  r'''expression : LPAREN ASSIGN ID expression RPAREN'''

  r'''expression : LPAREN ID parameter_list RPAREN
                 | LPAREN ID RPAREN'''

  r'''expression : LPAREN OP_ADD parameter_list RPAREN'''

  r'''expression : LPAREN OP_SUB parameter_list RPAREN'''

  r'''expression : LPAREN OP_MUL parameter_list RPAREN'''

  r'''expression : LPAREN OP_DIV parameter_list RPAREN'''

  r'''expression : ID'''

  r'''expression : NUMBER'''

  r'''expression : STRING'''

  r'''parameter_list : parameter_list expression
                     | expression'''

def p_error(p): # TODO

start = 'program'
parser = ply.yacc.yacc() # To get more information, add debug=True
