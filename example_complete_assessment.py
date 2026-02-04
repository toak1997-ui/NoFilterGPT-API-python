"""
Complete Red Team Assessment Example

This example demonstrates a complete workflow using the NoFilterGPT Red Team Assistant
for a penetration testing engagement, from reconnaissance to reporting.

IMPORTANT: Only use this on systems you have explicit authorization to test.
"""

from pentest_redteam import RedTeamAssistant

# Replace with your actual API key
API_KEY = 'YOUR_API_KEY'

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"{title}")
    print("=" * 80 + "\n")

def main():
    # Initialize the Red Team Assistant
    assistant = RedTeamAssistant(API_KEY)
    
    print_section("NoFilterGPT Red Team Assistant - Complete Assessment Example")
    
    # Phase 1: Reconnaissance
    print_section("PHASE 1: RECONNAISSANCE")
    print("Gathering information about the target...")
    
    try:
        recon_result = assistant.reconnaissance(
            target_info="target-company.com - Financial services company",
            recon_type="general"
        )
        print(recon_result)
    except Exception as e:
        print(f"Error during reconnaissance: {e}")
    
    # Phase 2: Vulnerability Analysis
    print_section("PHASE 2: VULNERABILITY ANALYSIS")
    print("Analyzing discovered services for vulnerabilities...")
    
    try:
        vuln_result = assistant.vulnerability_analysis(
            service_info="Apache Tomcat web application server",
            version_info="9.0.30"
        )
        print(vuln_result)
    except Exception as e:
        print(f"Error during vulnerability analysis: {e}")
    
    # Phase 3: Web Application Testing
    print_section("PHASE 3: WEB APPLICATION TESTING")
    print("Testing web application for common vulnerabilities...")
    
    try:
        web_result = assistant.web_application_testing(
            application_info="Customer portal with authentication and data management",
            vulnerabilities_to_test=["OWASP Top 10", "Business Logic Flaws"]
        )
        print(web_result)
    except Exception as e:
        print(f"Error during web application testing: {e}")
    
    # Phase 4: Exploitation
    print_section("PHASE 4: EXPLOITATION GUIDANCE")
    print("Getting guidance on exploiting identified vulnerabilities...")
    
    try:
        exploit_result = assistant.exploit_development(
            vulnerability_description="SQL Injection in login form",
            target_environment="MySQL database backend, PHP application"
        )
        print(exploit_result)
    except Exception as e:
        print(f"Error during exploitation guidance: {e}")
    
    # Phase 5: Privilege Escalation
    print_section("PHASE 5: PRIVILEGE ESCALATION")
    print("Strategizing privilege escalation after initial access...")
    
    try:
        privesc_result = assistant.privilege_escalation(
            system_info="Ubuntu 20.04 LTS web server",
            current_access="www-data user (web server process)"
        )
        print(privesc_result)
    except Exception as e:
        print(f"Error during privilege escalation: {e}")
    
    # Phase 6: Network Pivoting
    print_section("PHASE 6: LATERAL MOVEMENT")
    print("Planning lateral movement through the network...")
    
    try:
        pivot_result = assistant.network_pivoting(
            network_info="Internal corporate network with Active Directory",
            access_point="Compromised web server with dual network interfaces"
        )
        print(pivot_result)
    except Exception as e:
        print(f"Error during network pivoting: {e}")
    
    # Phase 7: Password Attacks
    print_section("PHASE 7: PASSWORD ATTACKS")
    print("Strategizing password attacks on captured credentials...")
    
    try:
        password_result = assistant.password_attack(
            target_type="NTLM hash cracking",
            hash_info="Multiple NTLM hashes captured from memory"
        )
        print(password_result)
    except Exception as e:
        print(f"Error during password attack planning: {e}")
    
    # Phase 8: Report Generation
    print_section("PHASE 8: REPORT GENERATION")
    print("Generating report structure...")
    
    findings = [
        "SQL Injection vulnerability in login form (Critical)",
        "Weak password policy allowing brute force attacks (High)",
        "Outdated Apache Tomcat version with known CVEs (High)",
        "Missing security headers (Medium)",
        "Information disclosure in error messages (Low)"
    ]
    
    try:
        report_result = assistant.generate_report(
            findings=findings,
            engagement_info="External penetration test of target-company.com"
        )
        print(report_result)
    except Exception as e:
        print(f"Error during report generation: {e}")
    
    print_section("ASSESSMENT COMPLETE")
    print("Remember: Always ensure you have proper authorization before testing.")
    print("This example demonstrates the workflow - actual testing requires manual verification.")

if __name__ == "__main__":
    main()
