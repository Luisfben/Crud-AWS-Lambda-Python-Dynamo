import json
import boto3


def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cliente')

    id = event.get('pathParameters').get('id')

    result = table.delete_item(
        Key={
            'id': id
        }
    )
   
    body = {
        "mensaje": "Cliente eliminado"
    }
	
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response