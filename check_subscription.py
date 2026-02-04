import requests
import json


# CHANGE THIS VALUE HERE
api_key = 'YOUR_API_KEY'


# Subscription check endpoint
url = f'https://api.nofiltergpt.com/v1/subscription/status?api_key={api_key}'

headers = {
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")
else:
    subscription_data = response.json()
    print("Subscription Status:")
    print(json.dumps(subscription_data, indent=2))
    
    # Check if user has an active subscription
    if subscription_data.get('has_subscription', False):
        print("\n✓ You have an active subscription!")
        if 'expires_at' in subscription_data:
            print(f"  Expires at: {subscription_data['expires_at']}")
        if 'plan' in subscription_data:
            print(f"  Plan: {subscription_data['plan']}")
    else:
        print("\n✗ You do not have an active subscription.")
        print("  Visit https://nofiltergpt.com to subscribe.")
