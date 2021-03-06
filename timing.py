import time

def calculate_time(func):
  def wrapper():
    print(time.time())
    func()
  return wrapper

@calculate_time
def time_sleep():
  time.sleep()



