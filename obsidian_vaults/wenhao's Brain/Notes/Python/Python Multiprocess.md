# Multiprocess in Python
Created: October 21, 2021 11:40 AM

Official reference for python multiprocess: [https://docs.python.org/3/](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process) 

#### Multiprocess
Python can create process as the following:
```python
#kills function with timelimit
def process_job(arg1):
		return

from multiprocessing import Process
ps = Process(target = process_job, args = ( a1, ) )
ps.start()

# do something in the main process
ps.join(timeout = 10)

if ps.is_alive():
		ps.terminate()
elif ps.exitcode != 0:
		print("process failed")
```
Explaination:
- For each process, a function is passed as a job, along with possible parameters
- `ps.join()` wait for the process to finish
- `timeout` is the waiting time, i.e. the main process will wait for 10s from `ps.join()`. if the subprocess is not finished, the main process will stop waiting and carrier on.
- A process is stopped if it terminates, just like the main process terminates (by error or return) Process can be bought to termination by `.terminate()`

#### Multi-threads
reference: https://docs.python.org/3/library/threading.html

Multi-threading is similar to multi-process, with:
```python
from threading import Thread

thread = Thread( target = fun, args = ( ) )   # tuple
thread.start()
thread.join(timeout = 4)
```
but thread cannot be killed, and should be managed by the code

#### Timeout with Signal
reference: https://docs.python.org/3/library/signal.html#signal.signal

This small script illustrate how to use alarm signal to time a function. 
Note that we created a `TimeOutException` so that the except will catched this specific exception, not other exception
```python
import signal

class TimeOutException(Exception):
		pass

def alarm_handler(signum, frame):
		print("Time out")
		raise TimeOutException
		
signal.signal(signal.SIGALRM, alarm_handler)
# define how to handle the SIGALRM

signal.alarm(10)
# start an alarm for 10 s

try:
		long_function()
except TimeOutException:
		pass

signal.alarm(0)
# reset the alarm
```