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
    principal =  principal * (1 + interest_rate)

  Example:
  principal = 500
  interest_rate = 0.05
  years = 10
  The total should return 814.4473133887211

  If any of the parameters is negative, returns False
  """
  if principal < 0:
    return False
  if interest_rate < 0:
    return False
  if years < 0:
    return False
  
  if isinstance(years, int) and isinstance(interest_rate, float):
    for i in range(years):
      principal = principal * (1 + interest_rate)
  return principal
  
