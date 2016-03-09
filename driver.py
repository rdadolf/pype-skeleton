#!/usr/bin/env python3

import sys
import pype

for fname in sys.argv[1:]:
  ast = pype.Pipeline(source=fname)
  ast.pprint()
