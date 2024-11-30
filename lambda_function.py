import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('smartbands_data')

def lambda_handler(event, context):
    """
    Lambda function to save smartband data to DynamoDB.
    """
    try:
        iivtem = {
            'serial_number': event.get('serial_number'),
            'timestamp': event.get('timestamp', 0),  
            'actity_type': event.get('activity_type', 'unknown'),
            'environment_temperature': event.get('environment_temperature', 0),  
            'heart_rate': event.get('heart_rate', 0),
            'SpO2': event.get('SpO2', 0),
            'steps': event.get('steps', 0),
        }

        response = table.put_item(Item=item)
        print(f"Data saved successfully to DynamoDB: {item}")

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data saved successfully', 'item': item})
        }
    
    except Exception as e:
        error_message = f"Error processing the event: {str(e)}"
        print(error_message)

        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error saving data', 'error': str(e)})
        }
