import json
def handler(event,context):
    message = "Hello World from lambda function with python!"
    return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": message}),
        };
