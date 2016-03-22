from lexer import lexer
from parser import parser
#from ast import *
from semantic_analysis import CheckSingleAssignment
from translate import SymbolTableVisitor

class Pipeline(object):
  def __init__(self, f):
    with open(f) as source:
      self.compile(source)

  def compile(self, file):
    input = file.read()
    # Lexing, parsing, AST construction
    ast = parser.parse(input, lexer=lexer)
    # Semantic analysis
    ast.walk( CheckSingleAssignment() )
    # Translation
    syms = ast.walk( SymbolTableVisitor())
    syms.pprint()
    return syms

t=Pipeline('./samples/example1.ppl')
