import json
import boto3

def lambda_handler(event, context):
    """
    AWS Lambda function to process API requests
    """
    try:
        # Process incoming event data
        body = {
            "message": "Hello from AWS Lambda!",
            "input_event": event,
            "timestamp": context.get_remaining_time_in_millis()
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(body)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
