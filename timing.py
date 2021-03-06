import time

def calculate_time(func):
  def wrapper():
    print(time.time())
    func()
    print(time.time())
  return wrapper

@calculate_time
def time_sleep():
  print(time.sleep(2))

