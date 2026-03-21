[Back](https://www.bioinfo-lab.com/courses/Programming_I/w13_LLM_API/)

<br>

<a id="all"></a>

### Content:

[Section 1. Getting Started with Kimi API](#s1.0)

[Section 2. Your First API Call](#s2.0)

[Section 3. Understanding Parameters](#s3.0)

[Section 4. Response Handling](#s4.0)

[Section 5. Error Handling](#s5.0)

[Section 6. Fun Project Examples](#s6.0)

[Section 7. Best Practices](#s7.0)

<br>

### Q: What can we build with Kimi API?

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Getting Started with Kimi API

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1.1. What is Kimi API?

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

---

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Obtaining Your API Key

### Step-by-Step Process

```bash
# Step 1: Visit Moonshot AI official platform
# Step 2: Register an account
# Step 3: Navigate to API Keys section
# Step 4: Generate a new key
# Step 5: Copy and secure your key
```

**Security Warning**: Never share your API key or commit it to version control.

```python
# Recommended: Store in environment variable
import os
api_key = os.getenv("KIMI_API_KEY")
```

---

<div align="left">
  <a href="#s1.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 1.3. Installation

### Required Libraries

```bash
# Install requests library for HTTP calls
pip install requests
```

### Verify Installation

```python
import requests
import json

print("Libraries loaded successfully!")
```

---

<div align="left">
  <a href="#s1.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>

# Section 2. Your First API Call

<div align="left">
  <a href="#s1.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. Basic API Structure

### Minimal Working Example

```python
import requests
import json

# Set your API key
API_KEY = "your_api_key_here"  # Replace with your actual key

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

# Print the response
print(response.json())
```

**Note**: The exact endpoint URL and model name may vary. Check official documentation for current values.

---

<div align="left">
  <a href="#s2.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. Understanding the Response

### Response Structure

```python
# Sample response (structure may vary)
{
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Hello! How can I help you today?"
            }
        }
    ]
}
```

### Extracting the Reply

```python
# Continuing from previous example
if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("Kimi says: " + reply)
else:
    print("Error: " + str(response.status_code))
```

---

<div align="left">
  <a href="#s2.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>

# Section 3. Understanding Parameters

<div align="left">
  <a href="#s2.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. Essential Parameters

### Core Parameters Table

| Parameter | Type    | Description                              | Example Value |
|-----------|---------|------------------------------------------|---------------|
| `model`   | string  | Model identifier                         | "kimi-chat"   |
| `messages`| array   | Conversation history                     | See below     |
| `temperature`| float | Creativity level (0-1)                | 0.7           |
| `max_tokens`| integer| Maximum response length                | 1000          |

### Messages Format

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "Why is it popular?"}
]
```

---

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. Temperature Parameter Demo

### Low Temperature (0.1) - Deterministic

```python
payload_low = {
    "model": "kimi-chat",
    "messages": [{"role": "user", "content": "Count to 5"}],
    "temperature": 0.1
}
# Expected: "1, 2, 3, 4, 5" (consistent)
```

### High Temperature (0.9) - Creative

```python
payload_high = {
    "model": "kimi-chat",
    "messages": [{"role": "user", "content": "Tell me a joke about cats"}],
    "temperature": 0.9
}
# Expected: Varies with each call
```

---

<div align="left">
  <a href="#s3.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>

# Section 4. Response Handling

<div align="left">
  <a href="#s3.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. Parsing JSON Responses

### Complete Parsing Function

```python
def get_kimi_response(prompt):
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

# Usage
result = get_kimi_response("Explain APIs in simple terms")
print("Answer: " + result)
```

---

<div align="left">
  <a href="#s4.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Handling Streaming Responses

### Streaming Mode Setup

```python
def stream_kimi_response(prompt):
    url = "https://api.moonshot.ai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "kimi-chat",
        "messages": [{"role": "user", "content": prompt}],
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

# Usage
stream_kimi_response("Write a short poem about coding")
```

---

<div align="left">
  <a href="#s4.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>

# Section 5. Error Handling

<div align="left">
  <a href="#s4.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Common Error Types

### Error Table

| Error Code | Meaning                 | Common Cause                     |
|------------|-------------------------|----------------------------------|
| 401        | Unauthorized            | Invalid API key                  |
| 429        | Rate Limit Exceeded     | Too many requests                |
| 400        | Bad Request             | Malformed payload                |
| 500        | Server Error            | Temporary server issue           |

### Error Handling Example

```python
def safe_kimi_call(prompt):
    try:
        result = get_kimi_response(prompt)
        return result
    except requests.exceptions.ConnectionError:
        return "Network error: Check your connection"
    except KeyError:
        return "Parse error: Unexpected response format"
    except Exception as e:
        return "Unknown error: " + str(e)

# Usage
response = safe_kimi_call("What is machine learning?")
print("Result: " + response)
```

---

<div align="left">
  <a href="#s5.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Retry Logic Implementation

### Exponential Backoff

```python
import time

def kimi_with_retry(prompt, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return get_kimi_response(prompt)
        except Exception as e:
            wait_time = 2  ** attempt  # 1, 2, 4 seconds
            print("Attempt " + str(attempt + 1) + " failed. Retrying in " + str(wait_time) + "s...")
            time.sleep(wait_time)
    return "Failed after " + str(max_attempts) + " attempts"

# Usage
result = kimi_with_retry("Explain quantum computing simply")
print("Final result: " + result)
```

---

<div align="left">
  <a href="#s5.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s6.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s6.0"></a>

# Section 6. Fun Project Examples

<div align="left">
  <a href="#s5.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s6.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s6.1"></a>

---

## 6.1. Story Generator

### Interactive Story Creator

```python
def create_story():
    character = input("Enter a character name: ")
    setting = input("Enter a setting: ")
    genre = input("Enter a genre (fantasy/sci-fi/mystery): ")
    
    prompt = "Write a " + genre + " story about " + character + " in " + setting + ". Keep it under 200 words."
    
    story = get_kimi_response(prompt)
    print("\n" + "="*50)
    print("Your Story:")
    print("="*50)
    print(story)

# Run it
create_story()
```

---

<div align="left">
  <a href="#s6.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s6.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s6.2"></a>

---

## 6.2. Code Explainer Bot

### Explain Any Code Snippet

```python
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
```

---

<div align="left">
  <a href="#s6.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s6.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s6.3"></a>

---

## 6.3. Data Analyzer

### CSV Data Insights

```python
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
```

---

<div align="left">
  <a href="#s6.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s7.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s7.0"></a>

# Section 7. Best Practices

<div align="left">
  <a href="#s6.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s7.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s7.1"></a>

---

## 7.1. API Key Security

### Never Hardcode Keys

```python
# BAD - Never do this
API_KEY = "sk-1234567890abcdef"

# GOOD - Use environment variables
import os
API_KEY = os.getenv("KIMI_API_KEY")

# BETTER - Use a config file (gitignore it)
# config.py (add to .gitignore)
# API_KEY = "your_key"

# main.py
# from config import API_KEY
```

### .gitignore Template

```bash
# Add these lines to .gitignore
config.py
.env
*.key
```

---

<div align="left">
  <a href="#s7.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s7.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s7.2"></a>

---

## 7.2. Cost and Rate Management

### Token Estimation

```python
def estimate_tokens(text):
    # Rough estimate: 1 token ≈ 4 characters
    return len(text) // 4

prompt = "Write a story about a robot learning to paint"
tokens = estimate_tokens(prompt)
print("Estimated tokens: " + str(tokens))
print("Estimated cost: $" + str(tokens * 0.00002))  # Example pricing
```

### Request Throttling

```python
import time

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

# Usage
limiter = KimiRateLimiter(max_requests=3)

for i in range(5):
    limiter.wait_if_needed()
    print("Making request " + str(i+1))
    # get_kimi_response("Test prompt")
```

---

<div align="left">
  <a href="#s7.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s7.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s7.3"></a>

---

## 7.3. Complete Project Template

### Production-Ready Structure

```python
# kimi_client.py
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
```

---

<div align="left">
  <a href="#s7.2">← Prev </a> | <a href="#all"> Home </a> 
</div>

<br>

### Q: Where to find official documentation?

**Answer**: Check Moonshot AI's official website for the most current API documentation. This tutorial provides educational examples that may need updates as the API evolves.

<br>

### Final Project Challenge

Build a personal assistant that:
1. Takes user questions in a loop
2. Remembers conversation history
3. Saves responses to a file
4. Handles errors gracefully
5. Respects rate limits

**Hint**: Combine concepts from all sections above.

<br>

End

---

**Disclaimer**: This tutorial is for educational purposes. API endpoints, parameters, and features may change. Always refer to official Moonshot AI documentation for production use. The code examples use placeholder values that must be replaced with actual API credentials.
