import json
import urllib.request

def lambda_handler(event, context):
    url = "https://jsonplaceholder.typicode.com/users"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    
    print(data)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
