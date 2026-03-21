[Back](https://www.bioinfo-lab.com/courses/Programming_I/w14_Multi_Tasking/)

<br>

---

### Important

This document contains practice exercises for Python multi-tasking concepts. Work through each section sequentially. Create all script files in your home directory (`~/`) and test them thoroughly.

<br>

---

### Tips

- **GIL Awareness**: Python threads do not run truly in parallel for CPU-bound tasks due to the Global Interpreter Lock. Use multiprocessing for CPU-intensive work.
- **Security**: Never use `shell=True` with user input in subprocess calls. Always pass commands as lists of arguments.
- **Lock Ordering**: To prevent deadlocks, always acquire multiple locks in the same order across all threads.
- **Command Validation**: Use `shutil.which()` to verify external commands exist before calling them in subprocess.
- **Thread Safety**: Shared data requires locks. Use `with lock:` context manager for automatic lock release.

<br>

---

### 1. Multi-tasking Fundamentals

Multi-tasking allows your program to perform multiple operations concurrently, improving efficiency for I/O-bound tasks or when interacting with external processes.

**Three Approaches in Python:**
- **Threading**: For I/O-bound tasks (network, disk operations)
- **Subprocess**: For running external programs
- **Multiprocessing**: For CPU-bound tasks (not covered in this document)

**When to Use Which:**
- **Threading**: Multiple tasks waiting for responses (web scraping, file downloads)
- **Subprocess**: Launching external applications (system commands, other programs)
- **Multiprocessing**: CPU-intensive calculations (data processing, computations)

<br>

---

### 2. Threading Basics

#### 2.1. Creating Your First Thread

```
# Create a new Python script file
cd ~
nano thread_demo.py

# Type the following code:
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

# Save: Ctrl + O, then Enter
# Exit: Ctrl + X

# Run the script
python3 thread_demo.py

# Note: Output may appear interleaved because threads run concurrently
```

<br>

---

#### 2.2. Thread Safety with Locks

```
# Create a new script file
cd ~
nano thread_lock.py

# Type the following code:
import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

thread1 = threading.Thread(target=safe_increment)
thread2 = threading.Thread(target=safe_increment)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Final counter: " + str(counter))  # Always 200000

# Save and exit nano
# Run the script
python3 thread_lock.py

# Expected output: Final counter: 200000
```

<br>

---

#### 2.3. Real-World Threading Example: Simulated Web Scraper

```
# Create a new script file
cd ~
nano web_scraper.py

# Type the following code:
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

# Save and exit nano
# Run the script
python3 web_scraper.py

# Compare with sequential processing by modifying the script
```

<br>

---

### 3. Subprocess Basics

#### 3.1. Running Simple Commands

```
# Create a new script file
cd ~
nano subprocess_demo.py

# Type the following code:
import subprocess

# Run a simple command
result = subprocess.run(["echo", "Hello from subprocess"], 
                       capture_output=True, text=True)

print("Return code: " + str(result.returncode))
print("Output: " + result.stdout)

# Save and exit nano
# Run the script
python3 subprocess_demo.py

# Expected output:
# Return code: 0
# Output: Hello from subprocess
```

<br>

---

#### 3.2. Capturing Output and Errors

```
# Create a new script file
cd ~
nano subprocess_capture.py

# Type the following code:
import subprocess

# Capture standard output
result = subprocess.run(["ls", "-l"], 
                       capture_output=True, text=True)

print("Command output:")
print(result.stdout)

if result.stderr:
    print("Errors: " + result.stderr)

# Check for errors
try:
    result = subprocess.run(["false"], 
                           capture_output=True, 
                           check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with code: " + str(e.returncode))

# Save and exit nano
# Run the script
python3 subprocess_capture.py

# Note: The 'false' command always fails with exit code 1
```

<br>

---

#### 3.3. Piping Between Commands

```
# Create a new script file
cd ~
nano subprocess_pipe.py

# Type the following code:
import subprocess

# Create a test file first
subprocess.run(["echo", "error: something failed\nwarning: low disk\nerror: connection lost"], 
               stdout=open("file.txt", "w"))

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

# Clean up
subprocess.run(["rm", "file.txt"])

# Save and exit nano
# Run the script
python3 subprocess_pipe.py

# Expected output: Number of error lines: 2
```

<br>

---

#### 3.4. Real-World Subprocess Example: System Monitor

```
# Create a new script file
cd ~
nano system_monitor.py

# Type the following code:
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

# Save and exit nano
# Run the script
python3 system_monitor.py

# Note: Requires Unix-like system with df, free, and uptime commands
```

<br>

---

### 4. Practical Examples & Comparison

#### 4.1. Threading Example: Parallel File Downloader

```
# Create a new script file
cd ~
nano parallel_download.py

# Type the following code:
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

# Save and exit nano
# Run the script
python3 parallel_download.py

# Observe the time difference between sequential and threaded execution
```

<br>

---

#### 4.2. Subprocess Example: Batch Image Converter

```
# Create a new script file
cd ~
nano image_converter.py

# Type the following code:
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

# Create test JPG files (if none exist)
subprocess.run(["touch", "test1.jpg", "test2.jpg"])

# Process all JPG files in current directory
jpg_files = [f for f in os.listdir(".") if f.endswith(".jpg")]

print("Found " + str(len(jpg_files)) + " JPG files to convert")

for jpg in jpg_files:
    convert_image(jpg)

# Save and exit nano
# Run the script
python3 image_converter.py

# Note: Requires ImageMagick to be installed: sudo apt-get install imagemagick
```

<br>

---

#### 4.3. Combining Threading and Subprocess

```
# Create a new script file
cd ~
nano combined_demo.py

# Type the following code:
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

# Save and exit nano
# Run the script
python3 combined_demo.py

# Observe how checks run concurrently despite using subprocess
```

<br>

---

### 5. Common Pitfalls & Debugging

#### 5.1. Threading Pitfalls

```
# Create a new script file to demonstrate GIL limitation
cd ~
nano gil_demo.py

# Type the following code:
import threading
import time

def cpu_heavy_task():
    count = 0
    for i in range(10000000):
        count += i

# This will NOT be faster with threads due to GIL
# Use multiprocessing for CPU-bound tasks instead

# Sequential execution
start = time.time()
cpu_heavy_task()
cpu_heavy_task()
print("Sequential time: " + str(time.time() - start) + "s")

# Threaded execution (will be slower due to GIL overhead)
start = time.time()
t1 = threading.Thread(target=cpu_heavy_task)
t2 = threading.Thread(target=cpu_heavy_task)
t1.start()
t2.start()
t1.join()
t2.join()
print("Threaded time: " + str(time.time() - start) + "s")

# Save and exit nano
# Run the script
python3 gil_demo.py

# Expected: Threaded version is slower than sequential
```

<br>

---

#### 5.2. Subprocess Security

```
# Create a new script file
cd ~
nano security_demo.py

# Type the following code:
import subprocess

# DANGEROUS - DO NOT USE
# user_input = "file.txt; rm -rf /"
# subprocess.run("cat " + user_input, shell=True)  # DON'T DO THIS

# SAFE implementation
user_input = "file.txt"  # Safe filename
subprocess.run(["cat", user_input])  # Safe from injection

# Validate command existence
import shutil

if shutil.which("convert") is None:
    print("Error: 'convert' command not found. Please install ImageMagick.")
else:
    # Safe to proceed
    print("Command 'convert' is available")

# Save and exit nano
# Run the script
python3 security_demo.py

# Always prefer list arguments over shell=True
```

<br>

---

#### 5.3. Debugging Techniques

```
# Create a new script file
cd ~
nano debug_demo.py

# Type the following code:
import threading
import subprocess

# Thread debugging
def debug_worker():
    print("Current thread: " + threading.current_thread().name)

thread = threading.Thread(target=debug_worker, name="Worker-1")
thread.start()
thread.join()

# Print all active threads
print("Active threads: " + str(threading.active_count()))

# Subprocess debugging
result = subprocess.run(
    ["ls", "/nonexistent"],
    capture_output=True,
    text=True
)

print("Return code: " + str(result.returncode))
print("STDOUT: " + result.stdout)
print("STDERR: " + result.stderr)

# Save and exit nano
# Run the script
python3 debug_demo.py

# Use these techniques to diagnose issues in your programs
```

<br>

---

End
