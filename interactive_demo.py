#!/usr/bin/env python3
"""
Interactive Red Team Assistant Demo

This script provides an interactive menu-driven interface to test
the NoFilterGPT Red Team Assistant capabilities.

IMPORTANT: Only use this on systems you have explicit authorization to test.
"""

import os
from pentest_redteam import RedTeamAssistant


def print_banner():
    """Print the application banner."""
    print("\n" + "=" * 80)
    print("           NoFilterGPT Red Team Assistant - Interactive Demo")
    print("=" * 80)
    print("\n⚠️  WARNING: For authorized security testing only!")
    print("=" * 80 + "\n")


def print_menu():
    """Print the main menu."""
    print("\nAvailable Functions:")
    print("-" * 80)
    print("1.  Reconnaissance")
    print("2.  Vulnerability Analysis")
    print("3.  Exploit Development Guidance")
    print("4.  Privilege Escalation")
    print("5.  Web Application Testing")
    print("6.  Password Attack Strategies")
    print("7.  Network Pivoting")
    print("8.  Social Engineering")
    print("9.  Report Generation")
    print("10. Custom Query")
    print("0.  Exit")
    print("-" * 80)


def get_api_key():
    """Get API key from user or environment."""
    api_key = os.environ.get('NOFILTERGPT_API_KEY')
    
    if not api_key:
        print("\nAPI Key not found in environment variable NOFILTERGPT_API_KEY")
        api_key = input("Enter your NoFilterGPT API key: ").strip()
    else:
        print(f"\n✓ Using API key from environment variable")
    
    return api_key


def demo_reconnaissance(assistant):
    """Demo reconnaissance function."""
    print("\n" + "=" * 80)
    print("RECONNAISSANCE")
    print("=" * 80)
    
    target = input("\nEnter target (e.g., example.com): ").strip()
    print("\nReconnaissance types: general, network, web, osint")
    recon_type = input("Enter reconnaissance type [general]: ").strip() or "general"
    
    print("\n⏳ Generating reconnaissance strategy...\n")
    try:
        result = assistant.reconnaissance(target, recon_type)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_vulnerability_analysis(assistant):
    """Demo vulnerability analysis function."""
    print("\n" + "=" * 80)
    print("VULNERABILITY ANALYSIS")
    print("=" * 80)
    
    service = input("\nEnter service name (e.g., Apache HTTP Server): ").strip()
    version = input("Enter version (optional): ").strip()
    
    print("\n⏳ Analyzing vulnerabilities...\n")
    try:
        result = assistant.vulnerability_analysis(service, version)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_exploit_development(assistant):
    """Demo exploit development function."""
    print("\n" + "=" * 80)
    print("EXPLOIT DEVELOPMENT GUIDANCE")
    print("=" * 80)
    
    vuln = input("\nDescribe the vulnerability: ").strip()
    env = input("Describe target environment (optional): ").strip()
    
    print("\n⏳ Generating exploit guidance...\n")
    try:
        result = assistant.exploit_development(vuln, env)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_privilege_escalation(assistant):
    """Demo privilege escalation function."""
    print("\n" + "=" * 80)
    print("PRIVILEGE ESCALATION")
    print("=" * 80)
    
    system = input("\nDescribe the system (e.g., Ubuntu 20.04): ").strip()
    access = input("Describe current access level (optional): ").strip()
    
    print("\n⏳ Generating privilege escalation strategies...\n")
    try:
        result = assistant.privilege_escalation(system, access)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_web_testing(assistant):
    """Demo web application testing function."""
    print("\n" + "=" * 80)
    print("WEB APPLICATION TESTING")
    print("=" * 80)
    
    app = input("\nDescribe the application: ").strip()
    vulns = input("Vulnerabilities to test (comma-separated, or OWASP Top 10): ").strip()
    
    vuln_list = [v.strip() for v in vulns.split(",")] if vulns else ["OWASP Top 10"]
    
    print("\n⏳ Generating web testing strategy...\n")
    try:
        result = assistant.web_application_testing(app, vuln_list)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_password_attack(assistant):
    """Demo password attack function."""
    print("\n" + "=" * 80)
    print("PASSWORD ATTACK STRATEGIES")
    print("=" * 80)
    
    attack_type = input("\nAttack type (e.g., hash cracking, brute force): ").strip()
    hash_info = input("Hash type or policy info (optional): ").strip()
    
    print("\n⏳ Generating password attack strategy...\n")
    try:
        result = assistant.password_attack(attack_type, hash_info)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_network_pivoting(assistant):
    """Demo network pivoting function."""
    print("\n" + "=" * 80)
    print("NETWORK PIVOTING")
    print("=" * 80)
    
    network = input("\nDescribe the network: ").strip()
    access_point = input("Describe access point (optional): ").strip()
    
    print("\n⏳ Generating network pivoting strategy...\n")
    try:
        result = assistant.network_pivoting(network, access_point)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_social_engineering(assistant):
    """Demo social engineering function."""
    print("\n" + "=" * 80)
    print("SOCIAL ENGINEERING")
    print("=" * 80)
    
    scenario = input("\nDescribe the scenario: ").strip()
    profile = input("Describe target profile (optional): ").strip()
    
    print("\n⏳ Generating social engineering strategy...\n")
    try:
        result = assistant.social_engineering(scenario, profile)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_report_generation(assistant):
    """Demo report generation function."""
    print("\n" + "=" * 80)
    print("REPORT GENERATION")
    print("=" * 80)
    
    print("\nEnter findings (one per line, empty line to finish):")
    findings = []
    while True:
        finding = input(f"Finding {len(findings) + 1}: ").strip()
        if not finding:
            break
        findings.append(finding)
    
    engagement = input("\nEngagement info (optional): ").strip()
    
    print("\n⏳ Generating report structure...\n")
    try:
        result = assistant.generate_report(findings, engagement)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_custom_query(assistant):
    """Demo custom query function."""
    print("\n" + "=" * 80)
    print("CUSTOM QUERY")
    print("=" * 80)
    
    query = input("\nEnter your question: ").strip()
    role = input("Expert role [penetration testing expert]: ").strip() or "penetration testing expert"
    
    print("\n⏳ Processing query...\n")
    try:
        result = assistant.custom_query(query, role)
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Main function."""
    print_banner()
    
    # Get API key
    api_key = get_api_key()
    
    if not api_key:
        print("\n❌ API key is required. Exiting.")
        return
    
    # Initialize assistant
    try:
        assistant = RedTeamAssistant(api_key)
        print("✓ Red Team Assistant initialized successfully\n")
    except Exception as e:
        print(f"\n❌ Failed to initialize assistant: {e}")
        return
    
    # Main loop
    while True:
        print_menu()
        choice = input("\nSelect an option: ").strip()
        
        if choice == "0":
            print("\n👋 Goodbye! Remember to test responsibly.\n")
            break
        elif choice == "1":
            demo_reconnaissance(assistant)
        elif choice == "2":
            demo_vulnerability_analysis(assistant)
        elif choice == "3":
            demo_exploit_development(assistant)
        elif choice == "4":
            demo_privilege_escalation(assistant)
        elif choice == "5":
            demo_web_testing(assistant)
        elif choice == "6":
            demo_password_attack(assistant)
        elif choice == "7":
            demo_network_pivoting(assistant)
        elif choice == "8":
            demo_social_engineering(assistant)
        elif choice == "9":
            demo_report_generation(assistant)
        elif choice == "10":
            demo_custom_query(assistant)
        else:
            print("\n❌ Invalid option. Please try again.")
        
        input("\n\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
