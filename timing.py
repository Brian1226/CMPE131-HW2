import time

def calculate_time(func):
  def wrapper():
    time.time()
    func()
    print(time.time() - time.time())
  return wrapper

@calculate_time
def time_sleep():
  time.sleep(2)


