import time
""""
Uses decorator to determine current time, pause program for 2 seconds, then calculate the difference between the time before the sleep & and time after the sleep.

Parameters:
current : the time before the sleep (float)
time.time() : the time used after the sleep (float)

Example:
current = 1615015080.3982704
time.time() = 1615015082.400343
total_time = 2.0021908283233643
"""
def calculate_time(func):
  def wrapper():
    current = time.time()
    func()
    total_time = time.time() - current
    print(f'Total time {total_time}')
  return wrapper

@calculate_time
def time_sleep():
  time.sleep(2)
