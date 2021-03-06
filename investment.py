def calculate_apr():
  """
  This function calculates total money earned from investment
  using the formula principal * (1 + interest_rate)

  Parameters:
  principal : float
  interest_rate : float
  years : int

  Returns:
  total
    total =  principal * (1 + interest_rate)

  Example:
  principal = 500
  interest_rate = 0.05
  years = 10
  The total should return 5250.0

  But if any of the parameters is negative, returns False
  """
  #make sure that principal and years is input is int, and interest_rate input is float
  principal = float(input()) 
  interest_rate = float(input())
  years = int(input())
  total = 0
  for i in range(years):
    total = total + (principal * (1 + interest_rate))

  #if any of the parameters is negative return False
  if principal < 0:
    return False
  elif interest_rate < 0:
    return False
  elif years < 0:
    return False
  else:
    print(total)

