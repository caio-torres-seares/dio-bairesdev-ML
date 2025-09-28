# funcoes.py

def somar(a, b):
  """
  Esta função recebe dois números e retorna a soma deles.
  """
  return a + b

def dividir(a, b):
  """
  Esta função recebe dois números e retorna a divisão do primeiro pelo segundo.
  Gera uma exceção se o divisor for zero.
  """
  if b == 0:
    raise ValueError("Divisor não pode ser zero.")
  return a / b