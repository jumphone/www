# Python Libraries and Modules

## Core Concepts
- **Module**: A single `.py` file containing Python code
- **Package**: A folder containing multiple modules (requires `__init__.py`)
- **Library**: A collection focusing on functionality, may include multiple packages and modules
- **Standard Library**: Pre-installed modules that come with Python, always available
- **Third-Party Libraries**: External packages available for download from PyPI (Python Package Index)

## Import Methods
Three primary ways to import libraries:

1. **Full Import**: Import the entire module
   - Syntax: `import module_name`
   - Usage: `module_name.function()`
   - Prevents name conflicts

2. **Specific Import**: Import specific functions or classes
   - Syntax: `from module_name import function_name`
   - Usage: `function_name()` directly
   - Makes code cleaner

3. **Alias Import**: Import with a shortened name
   - Syntax: `import module_name as alias`
   - Usage: `alias.function()`
   - Saves typing for long module names

4. **Combined Approach**: Import specific with alias
   - Syntax: `from module_name import function as alias`

## Python's Built-in Help
- Discover all available standard libraries: `help('modules')`
- Official documentation: docs.python.org/3/library

## pip - Python Package Manager
- Built-in tool for package management (available in Python 3.4+)
- Main commands:
  - `pip3 install package_name`
  - `pip3 uninstall package_name`
  - `pip3 list` (shows installed packages with versions)
  - `pip3 install --upgrade package_name`
  - `pip3 install package_name==version`
- Check version: `pip3 --version`

### Using Mirrors for Faster Downloads
- Temporary mirror: `pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name`
- Permanent configuration: `pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
- Creates configuration file at `~/.config/pip/pip.conf`

## Key Standard Library Modules

### math Module
- Mathematical functions and constants
- Key attributes: `math.pi`, `math.sqrt()`, `math.pow()`

### datetime Module
- Date and time handling
- `datetime.datetime.now()`: Returns current local time (year, month, day, hour, minute, second, microsecond)
- `datetime.timedelta()`: Represents time intervals for calculations
  - Parameters: `days`, `hours`, `minutes`
- Formatting: `strftime("%H:%M")` creates custom time strings

### random Module
- Random number generation
- `random.choice(sequence)`: Selects random element
- `random.randint(a, b)`: Returns random integer between a and b (inclusive)

### os Module
- Operating system interface for path and directory operations
- `os.path.exists(path)`: Checks if path exists
- `os.makedirs(path)`: Creates directory (including parent directories)
- `os.listdir(folder)`: Lists all files in directory
- `os.path.join(path, file)`: Safely joins path components

### shutil Module
- High-level file operations
- `shutil.copy2(src, dst)`: Copies file while preserving metadata

## Third-Party Libraries: requests
- HTTP library for web communication
- Basic usage pattern:
  ```python
  response = requests.get("URL")
  response.status_code  # HTTP status code
  response.text  # Response content as string
  ```
- Supports query parameters via f-strings: `f"http://wttr.in/{city}?format=3"`

## Practical Patterns

### Combining Multiple Modules
- Import and use different modules in a single script
- Common combination: `datetime` for timestamps with `requests` for data fetching

### Timezone Considerations
- `datetime.datetime.now()` returns local system time
- Applications requiring consistent timestamps must handle timezone awareness explicitly

### File Operations Workflow
1. Verify paths with `os.path.exists()`
2. Create directories with `os.makedirs()` if needed
3. List files using `os.listdir()`
4. Perform operations with `shutil.copy2()` or similar functions
