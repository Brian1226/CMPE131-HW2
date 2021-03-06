def calculate_apr(principal, interest_rate, years):
  """
  This function calculates total money earned from investment
  using the formula principal * (1 + interest_rate)

  Parameters:
  principal : int or float
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

  If any of the parameters is negative, returns False
  """

  total = 0
  
  if principal < 0:
    return False
  if interest_rate <= 0:
    return False
  if years < 0:
    return False
  
  if ((isinstance(principal, int) or isinstance(principal, float)) and isinstance(years, int) and isinstance(interest_rate, float)):
    for i in range(years):
      total = total + (principal * (1 + interest_rate))
  else:
    return False
  print(total)
  return total


calculate_apr(500, 0.03, 65)
