
## Concurrency (logic) and Parallel computing (Parallelism) (physical)

### What is Concurrency?

### Doing multiple tasks seemingly "at the same time"


```python
# Simple sequential vs concurrent comparison
import time

def task(name, duration):
    print(f"Task {name} started")
    time.sleep(duration)
    print(f"Task {name} completed")

# Sequential execution
task("A", 2)
task("B", 1)
```


### Blocking vs Non-blocking
**Blocking**:
- Wait until resource becomes available
- Nothing else can happen meanwhile

**Non-blocking**:
- Try to use resource, move on if busy
- Check back later or get notified

```python
from threading import Thread
import time

def blocking_task():
    print("Blocking task started")
    time.sleep(5)
    print("Blocking task finished")

# Blocking

blocking_task()

this_thread=Thread(target=blocking_task)
this_thread.start()
this_thread.isAlive()
this_thread.join()
this_thread.isAlive()

# Non-blocking

this_thread=Thread(target=blocking_task)
this_thread.start()
print("Main thread continues working")
this_thread.isAlive()

this_thread.isAlive()


## Give arguments
from threading import Thread
import time

def blocking_task(sleepTime=5):
    print("Blocking task started")
    print("Sleep time is:"+str(sleepTime))
    time.sleep(sleepTime)
    print("Blocking task finished")


this_thread=Thread(target=blocking_task,args=(15,))
this_thread.start()
this_thread.isAlive()

this_thread.join()

this_thread.isAlive()



## Get Results
from threading import Thread
import queue
import time

def blocking_task(q, sleepTime=5):
    print("Blocking task started")
    print("Sleep time is:"+str(sleepTime))
    time.sleep(sleepTime)
    print("Blocking task finished")
    result=sleepTime*2
    q.put(result)

q=queue.Queue()
this_thread=Thread(target=blocking_task,args=(q,3))
this_thread.start()
this_thread.isAlive()

this_thread.join()

this_thread.isAlive()

result=q.get()
print(result)


```

<br>
<br>
<br>

## Self-study: "subprocess" library in Python3 (real parallel computing)

<br>
<br>
<br>

## Main Question: How can we add a “loading animation” when AI is thinking ?

<br>
<br>
<br>






