"""
Example: Reconnaissance using NoFilterGPT Red Team Assistant

This example demonstrates how to use the Red Team Assistant for
reconnaissance operations during a penetration test.

IMPORTANT: Only use this on systems you have explicit authorization to test.
"""

from pentest_redteam import RedTeamAssistant

# Replace with your actual API key
API_KEY = 'YOUR_API_KEY'

def main():
    # Initialize the Red Team Assistant
    assistant = RedTeamAssistant(API_KEY)
    
    print("=" * 80)
    print("NoFilterGPT Red Team Assistant - Reconnaissance Example")
    print("=" * 80)
    print()
    
    # Example 1: General reconnaissance
    print("Example 1: General Reconnaissance Strategy")
    print("-" * 80)
    target = "example-corporation.com"
    
    try:
        result = assistant.reconnaissance(
            target_info=target,
            recon_type="general"
        )
        print(f"\nTarget: {target}")
        print(f"\nReconnaissance Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 2: Network reconnaissance
    print("\nExample 2: Network Reconnaissance")
    print("-" * 80)
    network_target = "192.168.1.0/24 - Corporate internal network"
    
    try:
        result = assistant.reconnaissance(
            target_info=network_target,
            recon_type="network"
        )
        print(f"\nTarget: {network_target}")
        print(f"\nNetwork Reconnaissance Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 3: Web application reconnaissance
    print("\nExample 3: Web Application Reconnaissance")
    print("-" * 80)
    web_target = "Web application at https://target-app.example.com"
    
    try:
        result = assistant.reconnaissance(
            target_info=web_target,
            recon_type="web"
        )
        print(f"\nTarget: {web_target}")
        print(f"\nWeb Reconnaissance Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    
    # Example 4: OSINT reconnaissance
    print("\nExample 4: OSINT Reconnaissance")
    print("-" * 80)
    osint_target = "TechCorp Inc. - Technology company with 500+ employees"
    
    try:
        result = assistant.reconnaissance(
            target_info=osint_target,
            recon_type="osint"
        )
        print(f"\nTarget: {osint_target}")
        print(f"\nOSINT Strategy:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 80)
    print("\nReconnaissance examples completed!")
    print("Remember: Always ensure you have proper authorization before testing.")
    print("=" * 80)

if __name__ == "__main__":
    main()
