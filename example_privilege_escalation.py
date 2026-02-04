"""
Example: Privilege Escalation using NoFilterGPT Red Team Assistant

This example demonstrates how to use the Red Team Assistant for
privilege escalation techniques during a penetration test.

IMPORTANT: Only use this on systems you have explicit authorization to test.
"""

from pentest_redteam import RedTeamAssistant

# IMPORTANT: Replace with your actual API key from https://nofiltergpt.com
# This placeholder will not work - you must use your own API key
API_KEY = 'YOUR_API_KEY'

def main():
    # Validate API key before proceeding
    if API_KEY == 'YOUR_API_KEY' or not API_KEY or len(API_KEY) < 10:
        print("=" * 80)
        print("ERROR: Invalid API Key")
        print("=" * 80)
        print("\nYou must replace 'YOUR_API_KEY' with your actual NoFilterGPT API key.")
        print("\nTo get your API key:")
        print("1. Visit https://nofiltergpt.com")
        print("2. Log in to your account")
        print("3. Go to Settings > Developers")
        print("4. Generate your API key")
        print("5. Replace 'YOUR_API_KEY' in this file with your actual key")
        print("\n" + "=" * 80)
        return
    
    # Initialize the Red Team Assistant
    assistant = RedTeamAssistant(API_KEY)
    
    print("=" * 80)
    print("NoFilterGPT Red Team Assistant - Privilege Escalation Example")
    print("=" * 80)
    print()
    
    # Example 1: Linux privilege escalation
    print("Example 1: Linux Privilege Escalation")
    print("-" * 80)
    
    try:
        result = assistant.privilege_escalation(
            system_info="Ubuntu 18.04 LTS Linux server",
            current_access="Standard user account with SSH access"
        )
        print(f"\nPrivilege Escalation Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 2: Windows privilege escalation
    print("\nExample 2: Windows Privilege Escalation")
    print("-" * 80)
    
    try:
        result = assistant.privilege_escalation(
            system_info="Windows Server 2016",
            current_access="Domain user with RDP access"
        )
        print(f"\nPrivilege Escalation Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 3: Container escape
    print("\nExample 3: Container Privilege Escalation")
    print("-" * 80)
    
    try:
        result = assistant.privilege_escalation(
            system_info="Docker container with limited capabilities",
            current_access="Non-root user inside container"
        )
        print(f"\nContainer Escape Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 4: Network pivoting after initial access
    print("\nExample 4: Network Pivoting")
    print("-" * 80)
    
    try:
        result = assistant.network_pivoting(
            network_info="Corporate network with multiple VLANs and internal services",
            access_point="Compromised web server in DMZ"
        )
        print(f"\nNetwork Pivoting Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    print("\nPrivilege escalation examples completed!")
    print("Remember: Always ensure you have proper authorization before testing.")
    print("=" * 80)

if __name__ == "__main__":
    main()
