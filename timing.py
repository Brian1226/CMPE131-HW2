
import time
""""
Uses decorator to determine current time, pause program for 2 seconds, then calculate the difference between the time before the sleep & and time after the sleep.

Parameters:
initial_time : the time before the sleep (float)
final_time : the time used after the sleep (float)

Example:
inital_time = 1615015080.3982704
final_time = 1615015082.400343
total_time = 2.0021908283233643
"""
def calculate_time(func):
  def wrapper():
    inital_time = time.time()
    func()
    final_time = time.time()
    total_time = final_time - inital_time
    print(f'Total time {total_time}')
  return wrapper

@calculate_time
def time_sleep():
  time.sleep(2)
