import json
import boto3


def handler(event, context):
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cliente')
   
    item = json.loads(event.get('body'))
    #test
    #item = event
   
    table.put_item(Item=item)

    body = {
        "mensaje": "Cliente creado",
        "datos": item
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
