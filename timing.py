import time

def calculate_time(func):
  def wrapper():
    current = time.time()
    func()
    print(int(time.time() - current))
  return wrapper

@calculate_time
def time_sleep():
  time.sleep(2)



