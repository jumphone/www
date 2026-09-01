# Python File Operations

* Files are data containers on disk, with text files (`.txt`, `.csv`) being human-readable and binary files (`.jpg`, `.docx`) having special formats.

* File paths can be absolute (`"/home/student/documents/diary.txt"`) or relative (`"../pictures/vacation.jpg"`).

* `open("file", "r")` opens for reading, `"w"` for writing (overwrite), `"a"` for appending, `"a+"` for append (create if not exist), `"r+"` for read+write.

* `file.read()` reads entire file, `file.readline()` reads one line, `file.readlines()` reads all lines as list.

* `file.write("string")` writes a string, `file.writelines(list)` writes lines from a list.

* Always use `file.close()` to close files and free resources.

* `with open('file.txt', 'r') as f:` automatically closes file after code block execution.

* Nested `with` handles multiple files: `with open('src.txt', 'r') as src: with open('dst.txt', 'w') as dst: dst.write(src.read())`.

* `import os` for file system operations. `os.path.exists("path")` checks path existence.

* `os.path.isfile("path")` checks if path is a file. `os.path.isdir("path")` checks if path is a directory.

* `os.path.getsize("file.txt")` returns file size in bytes.

* `os.mkdir("dirname")` creates a directory. `os.makedirs("path")` creates nested directories.

* `os.listdir("directory/")` returns list of names in that directory.

* `os.rename("old.txt", "new.txt")` renames files or directories.

* Encoding converts text to numbers. ASCII supports 128 English characters. UTF-8 supports all languages (1-4 bytes, Python 3 default). GBK is Chinese legacy encoding (2 bytes per Chinese character).

* Specify encoding when opening files: `open('file.txt', 'r', encoding='utf-8')`.

* Handle encoding errors with `errors='ignore'` to skip characters or `errors='replace'` to replace with `?`.

* `ord('A')` returns 65, `chr(65)` returns 'A'.

* `"string".replace('old', 'new')` replaces substrings.

* Caesar cipher encrypts by shifting: `chr(ord(char) + shift)`.

* Caesar cipher decrypts by shifting back: `chr(ord(char) - shift)`.

