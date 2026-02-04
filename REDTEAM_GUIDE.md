# Red Team & Penetration Testing Module - Quick Reference

## Overview

The `pentest_redteam.py` module provides AI-assisted penetration testing capabilities using the NoFilterGPT API. It's designed to help security professionals during authorized security assessments.

## Quick Start

```python
from pentest_redteam import RedTeamAssistant

# Initialize
assistant = RedTeamAssistant('YOUR_API_KEY')

# Use any function
result = assistant.reconnaissance("target.com", "general")
print(result)
```

## All Functions

### 1. Reconnaissance
```python
result = assistant.reconnaissance(
    target_info="example.com",
    recon_type="general"  # Options: general, network, web, osint
)
```

### 2. Vulnerability Analysis
```python
result = assistant.vulnerability_analysis(
    service_info="Apache HTTP Server",
    version_info="2.4.41"
)
```

### 3. Exploit Development
```python
result = assistant.exploit_development(
    vulnerability_description="SQL Injection in login form",
    target_environment="MySQL, PHP application"
)
```

### 4. Privilege Escalation
```python
result = assistant.privilege_escalation(
    system_info="Ubuntu 20.04 LTS",
    current_access="www-data user"
)
```

### 5. Web Application Testing
```python
result = assistant.web_application_testing(
    application_info="E-commerce web application",
    vulnerabilities_to_test=["SQL Injection", "XSS", "CSRF"]
)
```

### 6. Password Attacks
```python
result = assistant.password_attack(
    target_type="NTLM hash cracking",
    hash_info="Multiple NTLM hashes captured"
)
```

### 7. Network Pivoting
```python
result = assistant.network_pivoting(
    network_info="Corporate network with Active Directory",
    access_point="Compromised web server"
)
```

### 8. Social Engineering
```python
result = assistant.social_engineering(
    scenario="Phishing campaign targeting employees",
    target_profile="Technology company, 500+ employees"
)
```

### 9. Report Generation
```python
result = assistant.generate_report(
    findings=[
        "SQL Injection (Critical)",
        "XSS vulnerability (High)",
        "Weak passwords (Medium)"
    ],
    engagement_info="External penetration test"
)
```

### 10. Custom Query
```python
result = assistant.custom_query(
    query="What are the best tools for Linux privilege escalation?",
    system_role="Linux security expert"
)
```

## Example Workflow

```python
from pentest_redteam import RedTeamAssistant

assistant = RedTeamAssistant('YOUR_API_KEY')

# Phase 1: Reconnaissance
recon = assistant.reconnaissance("target.com", "general")

# Phase 2: Vulnerability Analysis
vulns = assistant.vulnerability_analysis("Apache Tomcat", "9.0.30")

# Phase 3: Web Testing
web = assistant.web_application_testing(
    "Customer portal",
    ["OWASP Top 10"]
)

# Phase 4: Report
report = assistant.generate_report(
    ["Finding 1", "Finding 2", "Finding 3"],
    "Security Assessment"
)
```

## Best Practices

1. **Authorization**: Always obtain written permission before testing
2. **Scope**: Stay within the defined scope of your engagement
3. **Documentation**: Document all findings and methodologies
4. **Responsible Disclosure**: Follow proper disclosure practices
5. **Legal Compliance**: Ensure compliance with all applicable laws

## Security Considerations

- Never use on unauthorized systems
- Store API keys securely (use environment variables)
- Don't commit API keys to version control
- Follow responsible disclosure guidelines
- Comply with data protection regulations

## Error Handling

```python
try:
    result = assistant.reconnaissance("target.com", "general")
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

## Environment Variables (Recommended)

```python
import os
from pentest_redteam import RedTeamAssistant

api_key = os.environ.get('NOFILTERGPT_API_KEY')
assistant = RedTeamAssistant(api_key)
```

## Support

For issues or questions:
- Check the README.md for detailed documentation
- Review the example scripts in the repository
- Ensure you have proper API authentication

---

**Remember: This tool is for authorized security testing only!**
