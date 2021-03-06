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
  
  if principal < 0:
    return False
  if interest_rate < 0:
    return False
  if years < 0:
    return False
  
  if isinstance(interest_rate, int) or isinstance(interest_rate, float) and isinstance(principal, int) or isinstance(principal, float):
    for i in range(years):
      total = total + (principal * (1 + interest_rate))
  else:
    return False
  print(total)
  return total


calculate_apr(500, 2.5, 2)
