import time

def current_time(func):
  def wrapper():
    print(time.time())
    func()
  return wrapper

@current_time
def time_sleep():
  time.sleep()



