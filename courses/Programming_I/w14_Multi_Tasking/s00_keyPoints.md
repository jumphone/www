# Python Multi-tasking: Threading and Subprocess

* Python supports three multi-tasking approaches: `threading` for I/O-bound tasks, `subprocess` for external programs, and `multiprocessing` for CPU-bound tasks.

* `threading` and `subprocess` serve different purposes: threading runs concurrent Python code, while subprocess launches isolated external programs.

* Threading shares memory space between threads, enabling direct but risky communication; subprocess uses isolated memory requiring explicit communication channels.

* Use `threading` for I/O-bound operations like network requests and file operations; use `subprocess` for running system commands or external applications.

* Create a thread with `threading.Thread(target=function, args=(...))`, start with `.start()`, and wait for completion with `.join()`.

* Threads share global variables, causing race conditions; use `threading.Lock()` to protect shared data.

* Acquire and release locks with `lock.acquire()` and `lock.release()`, or use the preferred context manager `with lock:` for automatic management.

* The Global Interpreter Lock (GIL) prevents Python threads from running truly in parallel for CPU-intensive tasks; threading does not speed up CPU-bound work.

* Deadlock risk occurs when multiple locks are acquired in different orders; always acquire locks in the same sequence across all threads.

* Execute external commands with `subprocess.run()`, passing arguments as a list `["command", "arg1"]` to avoid shell injection risks.

* Never use `shell=True` with user input; it creates serious security vulnerabilities.

* Capture command output by setting `capture_output=True` and `text=True` in `subprocess.run()` to get string output instead of bytes.

* Use `check=True` in `subprocess.run()` to raise `subprocess.CalledProcessError` when commands return non-zero exit codes.

* Pipe commands using `subprocess.Popen()` with `stdout=subprocess.PIPE` to chain multiple commands together.

* Validate external command availability with `shutil.which("command")` before execution to prevent `FileNotFoundError`.

* Debug threading issues with `threading.current_thread().name` and `threading.active_count()` to track thread activity.

* Inspect subprocess results through `result.returncode`, `result.stdout`, and `result.stderr` for complete error diagnosis.
