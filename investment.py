def calculate_apr(principal, interest_rate, years):
  """
  This function calculates total money earned from investment
  using the formula principal * (1 + interest_rate)

  Parameters:
  principal : int
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
  total = 0
  for i in range(years):
    total = total + (principal * (1 + interest_rate))

  #if any of the parameters is negative return False
  if principal < 0:
    return False
  elif interest_rate < 0:
    return False
  elif years < 0 or not isinstance(years, int):
    return False
  else:
    print(total)

calculate_apr(500, 2.5, 2.5)
