import json
import boto3


def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cliente')

    id = event.get('pathParameters').get('id')

    result = table.get_item(
        Key={
            'id': id
        }
    )
   
    result = result.get('Item')

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response