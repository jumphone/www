[Back](https://www.bioinfo-lab.com/courses/Programming_I/w13_LLM_API/)

<br>

---

### Important

Never share your API key or commit it to version control. Always store API keys in environment variables for security.

<br>

---

### Tips

"tab" type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

"history" You can see all the commands you have run before.

Use `echo $KIMI_API_KEY` to verify your environment variable is set.

<br>

---

### 1. Understanding Kimi API

Kimi is a large language model developed by Moonshot AI. The API allows you to integrate Kimi's capabilities into your Python programs.

**Key Features**:
- Natural language understanding
- Code generation and explanation
- Document analysis
- Multi-turn conversations

**Requirements**:
- Python 3.7 or higher
- Internet connection
- API key from Moonshot AI

<br>

---

### 2. Setting Up Your API Key

```
# Step 1: Visit Moonshot AI official platform
# Step 2: Register an account
# Step 3: Navigate to API Keys section
# Step 4: Generate a new key
# Step 5: Set it as an environment variable

# In your terminal, run (replace with your actual key):
export KIMI_API_KEY="your_api_key_here"

# Verify it's set:
echo $KIMI_API_KEY
```

<br>

---

### 3. Installing Required Libraries

```
# Install requests library for HTTP calls
pip install requests

# Create a verification script
cd ~
nano verify_install.py

# Type the following code:
import requests
import json

print("Libraries loaded successfully!")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 verify_install.py
```

<br>

---

### 4. Making Your First API Call

```
# Create a new script file
cd ~
nano first_call.py

# Type the following code:
import requests
import json
import os

# Get API key from environment variable
API_KEY = os.getenv("KIMI_API_KEY")

# API endpoint
url = "https://api.moonshot.ai/v1/chat/completions"

# Request headers
headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

# Request payload
payload = {
    "model": "kimi-chat",
    "messages": [
        {"role": "user", "content": "Hello, Kimi!"}
    ]
}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the full response
print(response.json())

# Save and exit nano
# Run the script
python3 first_call.py
```

<br>

---

### 5. Extracting the Response Content

```
# Create a new script file
cd ~
nano extract_response.py

# Type the following code:
import requests
import json
import os

API_KEY = os.getenv("KIMI_API_KEY")
url = "https://api.moonshot.ai/v1/chat/completions"

headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "model": "kimi-chat",
    "messages": [{"role": "user", "content": "Hello, Kimi!"}]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("Kimi says: " + reply)
else:
    print("Error: " + str(response.status_code))

# Save and exit nano
# Run the script
python3 extract_response.py
```

<br>

---

### 6. Understanding Parameters

```
# Create a new script file
cd ~
nano parameters.py

# Type the following code:
import requests
import json
import os

API_KEY = os.getenv("KIMI_API_KEY")
url = "https://api.moonshot.ai/v1/chat/completions"

headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

# Example with temperature parameter
payload = {
    "model": "kimi-chat",
    "messages": [{"role": "user", "content": "Tell me a joke about cats"}],
    "temperature": 0.7,  # Creativity level 0-1
    "max_tokens": 100    # Maximum response length
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("Response: " + reply)
else:
    print("Error: " + str(response.status_code))

# Save and exit nano
# Run the script
python3 parameters.py
```

<br>

---

### 7. Creating a Reusable Function

```
# Create a new script file
cd ~
nano kimi_function.py

# Type the following code:
import requests
import json
import os

def get_kimi_response(prompt):
    """Get response from Kimi API"""
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return "Error: " + str(response.status_code) + " - " + response.text

# Test the function
result = get_kimi_response("Explain APIs in simple terms")
print("Answer: " + result)

# Save and exit nano
# Run the script
python3 kimi_function.py
```

<br>

---

### 8. Handling Streaming Responses

```
# Create a new script file
cd ~
nano streaming.py

# Type the following code:
import requests
import json
import os

API_KEY = os.getenv("KIMI_API_KEY")
url = "https://api.moonshot.ai/v1/chat/completions"

headers = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "model": "kimi-chat",
    "messages": [{"role": "user", "content": "Write a short poem about coding"}],
    "stream": True  # Enable streaming
}

response = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)

print("Kimi: ", end="")
for line in response.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        if decoded_line.startswith('data: '):
            data = json.loads(decoded_line[6:])
            content = data["choices"][0]["delta"].get("content", "")
            print(content, end="")

print()  # New line at the end

# Save and exit nano
# Run the script
python3 streaming.py
```

<br>

---

### 9. Error Handling

```
# Create a new script file
cd ~
nano error_handling.py

# Type the following code:
import requests
import json
import os

def safe_kimi_call(prompt):
    try:
        API_KEY = os.getenv("KIMI_API_KEY")
        url = "https://api.moonshot.ai/v1/chat/completions"
        
        headers = {
            "Authorization": "Bearer " + API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "model": "kimi-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            return "Error: " + str(response.status_code)
            
    except requests.exceptions.ConnectionError:
        return "Network error: Check your connection"
    except KeyError:
        return "Parse error: Unexpected response format"
    except Exception as e:
        return "Unknown error: " + str(e)

# Test error handling
response = safe_kimi_call("What is machine learning?")
print("Result: " + response)

# Save and exit nano
# Run the script
python3 error_handling.py
```

<br>

---

### 10. Implementing Retry Logic

```
# Create a new script file
cd ~
nano retry_logic.py

# Type the following code:
import requests
import json
import os
import time

def get_kimi_response(prompt):
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        raise Exception("API Error: " + str(response.status_code))

def kimi_with_retry(prompt, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return get_kimi_response(prompt)
        except Exception as e:
            wait_time = 2 ** attempt  # 1, 2, 4 seconds
            print("Attempt " + str(attempt + 1) + " failed. Retrying in " + str(wait_time) + "s...")
            time.sleep(wait_time)
    return "Failed after " + str(max_attempts) + " attempts"

# Usage
result = kimi_with_retry("Explain quantum computing simply")
print("Final result: " + result)

# Save and exit nano
# Run the script
python3 retry_logic.py
```

<br>

---

### 11. Building a Story Generator

```
# Create a new script file
cd ~
nano story_generator.py

# Type the following code:
import os
import requests
import json

def get_kimi_response(prompt):
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    return data["choices"][0]["message"]["content"]

def create_story():
    character = input("Enter a character name: ")
    setting = input("Enter a setting: ")
    genre = input("Enter a genre (fantasy/sci-fi/mystery): ")
    
    prompt = f"Write a {genre} story about {character} in {setting}. Keep it under 200 words."
    
    story = get_kimi_response(prompt)
    print("\n" + "="*50)
    print("Your Story:")
    print("="*50)
    print(story)

# Run it
create_story()

# Save and exit nano
# Run the script
python3 story_generator.py
```

<br>

---

### 12. Building a Code Explainer Bot

```
# Create a new script file
cd ~
nano code_explainer.py

# Type the following code:
import os
import requests
import json

def get_kimi_response(prompt):
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    return data["choices"][0]["message"]["content"]

def explain_code():
    print("Paste your code (type 'END' on a new line when done):")
    
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    code = "\n".join(lines)
    
    prompt = "Explain this code in simple terms for a beginner:\n\n" + code
    
    explanation = get_kimi_response(prompt)
    print("\n" + "="*50)
    print("Explanation:")
    print("="*50)
    print(explanation)

# Usage
explain_code()

# Save and exit nano
# Run the script
python3 code_explainer.py
```

<br>

---

### 13. Building a Data Analyzer

```
# Create a new script file
cd ~
nano data_analyzer.py

# Type the following code:
import os
import requests
import json

def get_kimi_response(prompt):
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    return data["choices"][0]["message"]["content"]

def analyze_data(csv_data):
    prompt = "Analyze this CSV data and provide 3 key insights:\n\n" + csv_data + "\n\nFormat as bullet points."
    
    analysis = get_kimi_response(prompt)
    return analysis

# Example usage
sample_data = """Product,Sales,Month
Laptop,120,January
Mouse,450,January
Keyboard,200,January"""

insights = analyze_data(sample_data)
print("Data Insights:\n" + insights)

# Save and exit nano
# Run the script
python3 data_analyzer.py
```

<br>

---

### 14. API Key Security Best Practices

```
# Create a new script file
cd ~
nano security_demo.py

# Type the following code:
# BAD - Never do this
# API_KEY = "sk-1234567890abcdef"

# GOOD - Use environment variables
import os
API_KEY = os.getenv("KIMI_API_KEY")
print("API key loaded:", API_KEY is not None)

# BETTER - Use a config file (gitignore it)
# Create config.py (add to .gitignore)
# API_KEY = "your_key"

# main.py would be:
# from config import API_KEY

print("Security check passed!")

# Save and exit nano
# Run the script
python3 security_demo.py
```

** .gitignore Template **:
```
# Add these lines to .gitignore
config.py
.env
*.key
```

<br>

---

### 15. Rate Limit Management

```
# Create a new script file
cd ~
nano rate_limiter.py

# Type the following code:
import time
import os
import requests
import json

class KimiRateLimiter:
    def __init__(self, max_requests=3, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []
    
    def wait_if_needed(self):
        now = time.time()
        self.requests = [req for req in self.requests if now - req < self.time_window]
        
        if len(self.requests) >= self.max_requests:
            sleep_time = self.time_window - (now - self.requests[0])
            print("Rate limit reached. Waiting " + str(int(sleep_time)) + " seconds...")
            time.sleep(sleep_time)
        
        self.requests.append(time.time())

def get_kimi_response(prompt):
    API_KEY = os.getenv("KIMI_API_KEY")
    url = "https://api.moonshot.ai/v1/chat/completions"
    
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    return data["choices"][0]["message"]["content"]

# Usage
limiter = KimiRateLimiter(max_requests=3)

for i in range(3):
    limiter.wait_if_needed()
    print(f"Making request {i+1}")
    result = get_kimi_response("Say hello")
    print("Response:", result[:50] + "...")

# Save and exit nano
# Run the script
python3 rate_limiter.py
```

<br>

---

### 16. Complete Production-Ready Client

```
# Create a new script file
cd ~
nano kimi_client.py

# Type the following code:
import requests
import json
import os
import time
from typing import Dict, Any

class KimiClient:
    def __init__(self, api_key=None, model="kimi-chat"):
        self.api_key = api_key or os.getenv("KIMI_API_KEY")
        self.model = model
        self.base_url = "https://api.moonshot.ai/v1"
        self.last_request_time = 0
        self.rate_limit_delay = 1  # seconds between requests
    
    def chat(self, prompt: str, temperature=0.5) -> str:
        # Rate limiting
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)
        
        url = self.base_url + "/chat/completions"
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            self.last_request_time = time.time()
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return "Error " + str(response.status_code) + ": " + response.text
                
        except Exception as e:
            return "Exception: " + str(e)

# Usage example
if __name__ == "__main__":
    client = KimiClient()
    reply = client.chat("What is the capital of France?")
    print("Answer: " + reply)

# Save and exit nano
# Run the script
python3 kimi_client.py
```

<br>

---

### Final Project Challenge

Build a personal assistant that:
1. Takes user questions in a loop
2. Remembers conversation history
3. Saves responses to a file
4. Handles errors gracefully
5. Respects rate limits

**Hint**: Combine concepts from all sections above.

<br>

---

**Disclaimer**: This tutorial is for educational purposes. API endpoints, parameters, and features may change. Always refer to official Moonshot AI documentation for production use. The code examples use placeholder values that must be replaced with actual API credentials.

<br>

End
