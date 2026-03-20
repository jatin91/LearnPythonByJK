import requests

api_key = "your-api-key-here"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01"
}

body = {
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello Claude"}
    ]
}

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    json=body,
    headers=headers
)

data = response.json()
print(data["content"][0]["text"])

"""
That is it. That is Claude's API. A POST request with your key in the header and your message in the body. The `anthropic` library is just a clean wrapper around exactly this.

Now when you use the library later — you know precisely what it is doing underneath.

---

## The full picture connected to your chatbot
```
Your AIAgent object
        ↓
builds conversation list
        ↓
sends POST request to api.anthropic.com
        ↓
passes API key in headers
        ↓
passes conversation as JSON in body
        ↓
gets JSON response back
        ↓
converts to dictionary
        ↓
extracts text from content[0]["text"]
        ↓
adds to conversation history
        ↓
displays to user

"""