import time

current_time = time.time()

def calculate_time(func):
  def wrapper():
    
    func()
  return wrapper

@calculate_time
def time_sleep():
  print(current_time)


