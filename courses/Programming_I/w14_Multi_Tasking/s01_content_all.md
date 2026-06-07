[Back](https://www.bioinfo-lab.com/courses/Programming_I/w14_Multi_Tasking/)

<br>

<a id="all"></a>

### Content:

[Section 1. Multi-tasking Fundamentals](#s1.0)

[Section 2. Threading Basics](#s2.0)

[Section 3. Subprocess Basics](#s3.0)

[Section 4. Practical Examples & Comparison](#s4.0)

[Section 5. Common Pitfalls & Debugging](#s5.0)

<br>

### Q: Why do we need multi-tasking in Python?

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Multi-tasking Fundamentals

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>


<a id="s1.1"></a>

---

## 1.1. What is Multi-tasking?

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

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Threading vs Subprocess: Key Differences

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

<div align="left">
  <a href="#s1.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>



# Section 2. Threading Basics


<div align="left">
  <a href="#s1.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. Creating Your First Thread

### Basic Thread Creation
```python
import threading
import time

def worker(task_id):
    print("Starting task " + str(task_id))
    time.sleep(2)  # Simulate work
    print("Finished task " + str(task_id))

# Create threads
thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker, args=(2,))

# Start threads
thread1.start()
thread2.start()

# Wait for completion
thread1.join()
thread2.join()

print("All tasks completed")
```

### Output Order Note
Output may appear interleaved because threads run concurrently.

---

<div align="left">
  <a href="#s2.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. Thread Safety with Locks

### The Problem: Race Conditions
```python
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Not thread-safe!

# Two threads may overwrite each other's changes
```

### Solution: Using Lock
```python
import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

# Or use context manager (preferred)
def safe_increment_better():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

thread1 = threading.Thread(target=safe_increment_better)
thread2 = threading.Thread(target=safe_increment_better)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Final counter: " + str(counter))  # Always 200000
```

---

<div align="left">
  <a href="#s2.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.3"></a>

---

## 2.3. Real-World Threading Example: Simulated Web Scraper

```python
import threading
import time
import random

def fetch_url(url):
    print("Fetching: " + url)
    time.sleep(random.randint(1, 3))  # Simulate network delay
    print("Completed: " + url)

urls = [
    "https://site1.com/data",
    "https://site2.com/data",
    "https://site3.com/data",
    "https://site4.com/data"
]

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print("Total time: " + str(end_time - start_time) + " seconds")
# Much faster than sequential processing
```

---

<div align="left">
  <a href="#s2.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>



# Section 3. Subprocess Basics



<div align="left">
  <a href="#s2.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. Running Simple Commands

### Basic Command Execution
```python
import subprocess

# Run a simple command
result = subprocess.run(["echo", "Hello from subprocess"], 
                       capture_output=True, text=True)

print("Return code: " + str(result.returncode))
print("Output: " + result.stdout)
```

### Shell=True Caution
```python
# Not recommended (security risk)
# subprocess.run("echo hello", shell=True)

# Recommended (list of arguments)
subprocess.run(["echo", "hello"])
```

---

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. Capturing Output and Errors

### Capture Standard Output
```python
import subprocess

result = subprocess.run(["ls", "-l"], 
                       capture_output=True, text=True)

print("Command output:")
print(result.stdout)

if result.stderr:
    print("Errors: " + result.stderr)
```

### Check for Errors
```python
# Will raise CalledProcessError if command fails
try:
    result = subprocess.run(["false"], 
                           capture_output=True, 
                           check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with code: " + str(e.returncode))
```

---

<div align="left">
  <a href="#s3.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 3.3. Piping Between Commands

### Using Pipes
```python
import subprocess

# Equivalent to: cat file.txt | grep "error" | wc -l
p1 = subprocess.Popen(["cat", "file.txt"], 
                      stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "error"], 
                      stdin=p1.stdout,
                      stdout=subprocess.PIPE)
p1.stdout.close()

p3 = subprocess.Popen(["wc", "-l"], 
                      stdin=p2.stdout,
                      stdout=subprocess.PIPE)
p2.stdout.close()

output = p3.communicate()[0]
print("Number of error lines: " + output.decode().strip())
```

### Simpler Alternative
```python
# For simple cases, use shell piping in a single command
result = subprocess.run("cat file.txt | grep error | wc -l", 
                       shell=True, capture_output=True, text=True)
print("Count: " + result.stdout.strip())
```

---

<div align="left">
  <a href="#s3.2">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 3.4. Real-World Subprocess Example: System Monitor

```python
import subprocess
import time

def get_disk_usage():
    """Get disk usage percentage"""
    result = subprocess.run(["df", "-h", "/"], 
                           capture_output=True, text=True)
    lines = result.stdout.split("\n")
    # Parse the percentage from second line
    usage = lines[1].split()[4]  # e.g., "45%"
    return usage

def get_memory_info():
    """Get memory usage"""
    result = subprocess.run(["free", "-m"], 
                           capture_output=True, text=True)
    return result.stdout.split("\n")[1]

def get_cpu_load():
    """Get CPU load average"""
    result = subprocess.run(["uptime"], 
                           capture_output=True, text=True)
    return result.stdout.strip()

# Monitor every 5 seconds
for i in range(3):
    print("=== System Check " + str(i+1) + " ===")
    print("Disk usage: " + get_disk_usage())
    print("Memory: " + get_memory_info())
    print("CPU: " + get_cpu_load())
    print("")
    time.sleep(5)
```

---

<div align="left">
  <a href="#s3.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>



# Section 4. Practical Examples & Comparison



<div align="left">
  <a href="#s3.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. Threading Example: Parallel File Downloader

```python
import threading
import time
import random

def download_file(filename):
    print("Starting download: " + filename)
    download_time = random.randint(2, 5)
    time.sleep(download_time)
    print("Finished: " + filename + " in " + str(download_time) + "s")

files = ["report.pdf", "data.csv", "image.jpg", "video.mp4"]

# Sequential (slow)
print("=== Sequential Download ===")
start = time.time()
for f in files:
    download_file(f)
print("Total time: " + str(time.time() - start) + "s\n")

# Threaded (fast)
print("=== Threaded Download ===")
start = time.time()
threads = []
for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("Total time: " + str(time.time() - start) + "s")
```

---

<div align="left">
  <a href="#s4.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Subprocess Example: Batch Image Converter

```python
import subprocess
import os

def convert_image(input_file):
    """Convert JPG to PNG using external tool"""
    if not input_file.endswith(".jpg"):
        return
    
    output_file = input_file.replace(".jpg", ".png")
    
    # Using ImageMagick's convert command
    try:
        result = subprocess.run(
            ["convert", input_file, output_file],
            capture_output=True,
            check=True,
            text=True
        )
        print("Converted: " + input_file + " -> " + output_file)
    except subprocess.CalledProcessError as e:
        print("Failed to convert " + input_file + ": " + e.stderr)
    except FileNotFoundError:
        print("Error: ImageMagick 'convert' command not found")

# Process all JPG files in current directory
jpg_files = [f for f in os.listdir(".") if f.endswith(".jpg")]

print("Found " + str(len(jpg_files)) + " JPG files to convert")

for jpg in jpg_files:
    convert_image(jpg)
```

---

<div align="left">
  <a href="#s4.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.3"></a>

---

## 4.3. Combining Threading and Subprocess

```python
import threading
import subprocess
import time

def run_system_check(check_name):
    print("Starting check: " + check_name)
    
    if check_name == "disk":
        cmd = ["df", "-h"]
    elif check_name == "memory":
        cmd = ["free", "-h"]
    elif check_name == "processes":
        cmd = ["ps", "aux"]
    else:
        return
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("=== " + check_name.upper() + " CHECK ===")
    print(result.stdout[:200])  # Show first 200 chars
    print("")

# Run multiple system checks concurrently
checks = ["disk", "memory", "processes"]
threads = []

for check in checks:
    t = threading.Thread(target=run_system_check, args=(check,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All system checks completed")
```

---

<div align="left">
  <a href="#s4.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>



# Section 5. Common Pitfalls & Debugging



<div align="left">
  <a href="#s4.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Threading Pitfalls

### Global Interpreter Lock (GIL)
```python
# Python threads don't run truly in parallel for CPU tasks
import threading
import time

def cpu_heavy_task():
    count = 0
    for i in range(10000000):
        count += i

# This will NOT be faster with threads due to GIL
# Use multiprocessing for CPU-bound tasks instead
```

### Deadlock Risk
```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        time.sleep(0.1)
        with lock2:  # May cause deadlock
            print("Task 1")

def task2():
    with lock2:
        time.sleep(0.1)
        with lock1:  # May cause deadlock
            print("Task 2")

# Solution: Always acquire locks in same order
```

---

<div align="left">
  <a href="#s5.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Subprocess Security

### Never Use shell=True with User Input
```python
# DANGEROUS
user_input = "file.txt; rm -rf /"
# subprocess.run("cat " + user_input, shell=True)  # DON'T DO THIS

# SAFE
user_input = "file.txt"
subprocess.run(["cat", user_input])  # Safe from injection
```

### Validate Command Existence
```python
import shutil

if shutil.which("convert") is None:
    print("Error: 'convert' command not found. Please install ImageMagick.")
else:
    # Safe to proceed
    subprocess.run(["convert", "input.jpg", "output.png"])
```

---

<div align="left">
  <a href="#s5.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 5.3. Debugging Techniques

### Thread Debugging
```python
import threading

def debug_worker():
    print("Current thread: " + threading.current_thread().name)

thread = threading.Thread(target=debug_worker, name="Worker-1")
thread.start()
thread.join()

# Print all active threads
print("Active threads: " + str(threading.active_count()))
```

### Subprocess Debugging
```python
import subprocess

# Enable full error reporting
result = subprocess.run(
    ["ls", "/nonexistent"],
    capture_output=True,
    text=True
)

print("Return code: " + str(result.returncode))
print("STDOUT: " + result.stdout)
print("STDERR: " + result.stderr)
```

### AI Assistant Tip
"Ask Kimi/DouBao to explain why your threaded program is slower than expected and whether it's I/O-bound or CPU-bound."

---

<div align="left">
  <a href="#s5.2">← Prev </a> |  <a href="#all"> Home </a> 
</div>

<br>

End
