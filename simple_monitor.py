'''
Class Stats:
   def __init__(self, time_window):
       # Implement. time_window is in seconds. This is the number of seconds we care about

   def update(self, metric):
       # Implement. You'll do some housekeeping here.

   def stats(self):
       # Return the average metric value in the last time_window seconds.

Example:
time_window=3
t=0, update(3)
t=0.5, update(5)
t=1, update(7)
t=2, stats() => 5
t=3, update(9)
t=5, stats() => 9
.
.
.
.
t=10, stats() => 0 / None
'''

from collections import deque
import time
# https://docs.python.org/2/library/collections.html


class Stats:
   def __init__(self, time_window):
       # Implement. time_window is in seconds. This is the number of seconds we care about
       self.time_window = time_window
       self.moving_sum = 0
       self.dq = deque()

   def purge_dq(self, curr_time_secs):
       '''
       Removes elements from the deque outside the window of interest
       '''
       while self.dq:
           if (curr_time_secs - self.dq[0][1]) > self.time_window:
               self.moving_sum -= self.dq[0][0]
               self.dq.popleft()
           else:
               break

   def update(self, metric):
       # Implement. You'll do some housekeeping here.
       '''
       Adds the current metric and updates moving sum before purging the deque
       '''
       curr_time_secs = int(time.time())
       self.purge_dq(curr_time_secs)
       self.moving_sum += metric
       self.dq.append((metric, curr_time_secs))

   def stats(self):
       '''
       Return the average metric value in the last time_window seconds.
       '''
       curr_time_secs = int(time.time())
       self.purge_dq(curr_time_secs)
       return (self.moving_sum/len(self.dq)) if len(self.dq) != 0 else None


print('Testing...')
s = Stats(3)
st = time.time()
time.sleep(0); s.update(3)
time.sleep(0.5); s.update(5)
time.sleep(0.5); s.update(7)
time.sleep(1); assert s.stats() == 5.0  #t = 2
print(f'Avg at t = {int(time.time() - st)} : {s.stats()}')
time.sleep(1); s.update(9)
time.sleep(2); assert s.stats() == 9.0  #t = 5
print(f'Avg at t = {int(time.time() - st)} : {s.stats()}')
time.sleep(5); assert s.stats() == None #t = 10
print(f'Avg at t = {int(time.time() - st)} : {s.stats()}')
print('Test ended')
