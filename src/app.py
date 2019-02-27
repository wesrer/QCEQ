import sympy

mu = sympy.symbols('mu')
sympy.pprint((sympy.Integral(sympy.sqrt(1 / mu), mu)), use_unicode=True)

