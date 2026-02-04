
# NoFilterGPT API for Python

The NoFilterGPT API for Python allows developers to easily integrate the power of the NoFilterGPT AI model into their Python applications. With a simple POST request, you can generate dynamic responses from the AI, fine-tuning parameters such as temperature, token limit, and more.

## 🔴 Red Team & Penetration Testing Module

This repository now includes a specialized module for **penetration testing and red team operations**. The `pentest_redteam.py` module provides AI-assisted capabilities for security assessments, including:

- 🔍 **Reconnaissance**: OSINT, network discovery, and information gathering
- 🛡️ **Vulnerability Analysis**: Service analysis, CVE research, and security assessment
- 💥 **Exploit Development**: PoC creation and exploitation guidance
- 🔐 **Privilege Escalation**: System-specific escalation techniques
- 🌐 **Web Application Testing**: OWASP Top 10 and beyond
- 🔑 **Password Attacks**: Hash cracking and credential testing strategies
- 🔄 **Network Pivoting**: Lateral movement and post-exploitation
- 📊 **Report Generation**: Professional penetration testing reports

### ⚠️ IMPORTANT SECURITY DISCLAIMER

**This tool is intended for AUTHORIZED security testing ONLY.** 

- ✅ Only use on systems you have explicit written permission to test
- ✅ Follow responsible disclosure practices
- ✅ Comply with all applicable laws and regulations
- ❌ Unauthorized access to computer systems is illegal
- ❌ Misuse of these tools can result in criminal prosecution

By using this module, you agree to use it ethically and legally.

## Getting Your API Key

To start using the NoFilterGPT API, you will need an API key. Simply log into your account at [nofiltergpt.com](https://nofiltergpt.com), navigate to the **"Settings"** page, click on the **"Developers"** tab, and generate your API key. It's simple and fast!

Once you have your API key, you're ready to make requests to the NoFilterGPT API and build engaging applications.

## Quick Start - Red Team Module

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from pentest_redteam import RedTeamAssistant

# Initialize with your API key
assistant = RedTeamAssistant('YOUR_API_KEY')

# Perform reconnaissance
result = assistant.reconnaissance(
    target_info="example.com",
    recon_type="general"
)
print(result)

# Analyze vulnerabilities
result = assistant.vulnerability_analysis(
    service_info="Apache HTTP Server",
    version_info="2.4.41"
)
print(result)

# Get web application testing guidance
result = assistant.web_application_testing(
    application_info="E-commerce web application",
    vulnerabilities_to_test=["SQL Injection", "XSS", "CSRF"]
)
print(result)
```

### Example Scripts

The repository includes several example scripts:

- **`example_reconnaissance.py`**: Demonstrates various reconnaissance techniques
- **`example_vulnerability_analysis.py`**: Shows vulnerability analysis workflows
- **`example_privilege_escalation.py`**: Covers privilege escalation strategies
- **`example_complete_assessment.py`**: Complete penetration testing workflow

To run an example:

```bash
# Edit the file to add your API key
nano example_reconnaissance.py

# Run the example
python example_reconnaissance.py
```

## Available Red Team Functions

### `reconnaissance(target_info, recon_type="general")`
Get AI-assisted reconnaissance strategies for your target.

**Parameters:**
- `target_info` (str): Target information (domain, IP, organization)
- `recon_type` (str): Type of recon - "general", "network", "web", or "osint"

### `vulnerability_analysis(service_info, version_info="")`
Analyze services and applications for potential vulnerabilities.

**Parameters:**
- `service_info` (str): Service or application description
- `version_info` (str): Version information if available

### `exploit_development(vulnerability_description, target_environment="")`
Get guidance on developing exploits and proof-of-concepts.

**Parameters:**
- `vulnerability_description` (str): Description of the vulnerability
- `target_environment` (str): Target environment details

### `privilege_escalation(system_info, current_access="")`
Get privilege escalation techniques for various systems.

**Parameters:**
- `system_info` (str): Target system information
- `current_access` (str): Current access level description

### `web_application_testing(application_info, vulnerabilities_to_test=None)`
Get web application testing strategies and methodologies.

**Parameters:**
- `application_info` (str): Application description
- `vulnerabilities_to_test` (List[str]): Specific vulnerabilities to test for

### `password_attack(target_type, hash_info="")`
Get password attack strategies and recommendations.

**Parameters:**
- `target_type` (str): Type of password attack
- `hash_info` (str): Hash type or password policy information

### `network_pivoting(network_info, access_point="")`
Get network pivoting and lateral movement strategies.

**Parameters:**
- `network_info` (str): Target network information
- `access_point` (str): Initial access point description

### `social_engineering(scenario, target_profile="")`
Generate social engineering scenarios and strategies.

**Parameters:**
- `scenario` (str): Social engineering scenario description
- `target_profile` (str): Target organization/individual information

### `generate_report(findings, engagement_info="")`
Generate penetration testing report structure and content.

**Parameters:**
- `findings` (List[str]): List of security findings
- `engagement_info` (str): Engagement description

### `custom_query(query, system_role="penetration testing expert")`
Make custom queries with specified AI expertise.

**Parameters:**
- `query` (str): Your question or request
- `system_role` (str): The expertise role for the AI

## How to Use the NoFilterGPT API (Direct API Calls)

For those who want to make direct API calls without using the Red Team module, here's how to use the base API.

### Endpoint: `/v1/chat/completions`

The NoFilterGPT API's primary endpoint for generating AI-based chat completions is:

```
https://api.nofiltergpt.com/v1/chat/completions
```

This endpoint expects a **POST** request with the following required and optional parameters in the body, in JSON format.

### Required Parameters:

- **messages**: An array of message objects that represent the conversation. Each message object must have the following structure:
  - **role**: Either `"system"`, `"user"`, or `"assistant"`.
  - **content**: The message content. This is the text that the model will process or generate.
  
  Example:

  ```json
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! Can you help me with something?"}
  ]
  ```

### Optional Parameters:

- **temperature**: Controls the creativity of the output. Lower values make the output more deterministic, while higher values increase randomness. Default: `0.7`.
- **max_tokens**: The maximum number of tokens (words/subwords) to generate. Default depends on the model.
- **top_p**: For nucleus sampling. This controls diversity by cutting off the less likely responses. Default: `1`.

### Authentication

To authenticate, you need to append your API key in the query string of the request URL like this:

```
https://api.nofiltergpt.com/v1/chat/completions?api_key=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with the actual API key obtained from your NoFilterGPT account.

## Example Usage with `example.py`

The file `example.py` in the root of this project provides a working example of how to interact with the `/v1/chat/completions` endpoint using Python.

### Setup

You will need to install the `requests` library if you haven't already:

```bash
pip install requests
```

1. **Replace the API Key**:
   Open the `example.py` file and replace `'YOUR_API_KEY'` with your actual API key obtained from [nofiltergpt.com](https://nofiltergpt.com).

   ```python
   api_key = 'YOUR_API_KEY'
   ```

2. **Modify the Parameters** (optional):
   You can modify the request parameters, such as `messages`, `temperature`, `max_tokens`, and `top_p`, in the file to fit your specific needs. For example, you can change the user input like this:

   ```python
   data = {
       "messages": [
           {"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": "How do I integrate this API?"}
       ],
       "temperature": 0.7,
       "max_tokens": 150,
       "top_p": 1
   }
   ```

3. **Run the Script**:
   To execute the script and make a request to the `/v1/chat/completions` endpoint, simply run the Python file on your server or local environment:

   ```bash
   python example.py
   ```

   This will output the response generated by the API based on the provided input.

### Full `example.py` Code

Here is the content of `example.py` for your reference:

```python
import requests
import json

# CHANGE THIS VALUE HERE
api_key = 'YOUR_API_KEY'

url = f'https://api.nofiltergpt.com/v1/chat/completions?api_key={api_key}'

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you help me with something?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150,
    "top_p": 1
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
    print(f"Error: {response.status_code}")
else:
    print(response.json())
```

### Handling Responses

The API response will include a generated completion (i.e., a response from the assistant) and any additional data. Handle error responses with appropriate HTTP status codes.

### Error Handling

- **400 Bad Request**: One or more required parameters are missing.
- **401 Unauthorized**: Invalid or missing API key.

## Contributing

If you would like to contribute or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
