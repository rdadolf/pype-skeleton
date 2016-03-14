from lexer import lexer
from parser import parser
#from ast import *
from semantic_analysis import CheckSingleAssignment
#from .translate import SymbolTableVisitor

class Pipeline(object):
  def __init__(self, f):
    with open(f) as source:
      self.compile(source)

  def compile(self, file):
    input = file.read()
    # Lexing, parsing, AST construction
    ast = parser.parse(input, lexer=lexer)
    # Semantic analysis
    ast.pprint()
    ast.walk( CheckSingleAssignment() )
    # Translation
    #syms = ast.walk( SymbolTableVisitor() )
    #return syms

t=Pipeline('/Users/MikeZhang/Documents/mike_zcc/Graduate/2016 Spring/CS207/pype-skeleton/samples/example1.ppl')
