import time

def calculate_time(func):
  def wrapper():
    current_time = time.time()
    func()
    print(current_time)
  return wrapper

@calculate_time
def sleep():
  time.sleep(2)
  print(time) 
