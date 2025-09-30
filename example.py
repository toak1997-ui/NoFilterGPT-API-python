import requests
import json


api_key = 'ZTloWWR0ZnM3Nlp2RGU3cFliaXVpR1FRUHBEMw'



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


### Handling Responses

The API response will include a generated completion (i.e., a response from the assistant) and any additional data. Handle error responses with appropriate HTTP status codes.

### Error Handling

- **400 Bad Request**: One or more required parameters are missing.
- **401 Unauthorized**: Invalid or missing API key.

## Contributing

If you would like to contribute or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
