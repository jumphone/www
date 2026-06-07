
## What is Multi-tasking?

### Definition
Multi-tasking allows your program to perform multiple operations concurrently, improving efficiency when dealing with I/O-bound or external processes.

### Three Approaches in Python
```python
# Threading: For I/O-bound tasks (network, disk)
import threading

# Subprocess: For running external programs
import subprocess

# Multiprocessing: For CPU-bound tasks (not covered here)
import multiprocessing
```

### When to Use Which
- **Threading**: Multiple tasks waiting for responses (web scraping, file downloads)
- **Subprocess**: Launching external applications (system commands, other programs)
- **Multiprocessing**: CPU-intensive calculations (data processing, computations)

---


---

## Threading vs Subprocess: Key Differences

### Threading
```python
# Threads share the same memory space
shared_list = []

def add_item(item):
    shared_list.append(item)  # All threads access this list

# Memory is shared, communication is easy but risky
```

### Subprocess
```python
# Subprocesses run in isolated memory spaces
# Communication requires explicit channels (pipes, files, stdout)

# No shared memory, completely isolated
```

### Comparison Table

| Feature | Threading | Subprocess |
|---------|-----------|------------|
| Memory | Shared | Isolated |
| Speed | Fast startup | Slower startup |
| Use Case | I/O-bound tasks | External programs |
| Overhead | Low | Higher |
| Communication | Direct (risky) | Pipes/files |

---

## Threading

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


