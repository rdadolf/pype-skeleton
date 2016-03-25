from .ast import *
from .error import *

class PrettyPrint(ASTVisitor):
  def __init__(self):
    pass
  def visit(self, node):
    pass # TODO

class CheckSingleAssignment(ASTVisitor):
  def __init__(self):
    pass # TODO
  def visit(self, node):
    pass # TODO

ass CheckSingleIOExpression(ASTVisitor):
  def __init__(self):
    self.component = None
    self.component_has_input = False
    self.component_has_output = False

  def visit(self, node):
    if isinstance(node, ASTComponent):
      self.component = node.name.name
      self.component_has_input = False
      self.component_has_output = False
    elif isinstance(node, ASTInputExpr):
      if self.component_has_input:
        raise PypeSyntaxError('Component '+str(self.component)+' has multiple input expressions')
      self.component_has_input = True
    elif isinstance(node, ASTOutputExpr):
      if self.component_has_output:
        raise PypeSyntaxError('Component '+str(self.component)+' has multiple output expressions')
      self.component_has_output = True

class CheckUndefinedVariables(ASTVisitor):
  def __init__(self, symtab):
    self.symtab = symtab
    self.scope=None

  def visit(self, node):
    if isinstance(node, ASTComponent):
      self.scope = node.name.name
    elif isinstance(node, ASTID):
      if self.symtab.lookupsym(node.name, scope=self.scope) is None:
        raise PypeSyntaxError('Undefined variable: '+str(node.name))
