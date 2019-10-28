import json
import boto3


def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cliente')

    id = event.get('pathParameters').get('id')
    body = json.loads(event.get('body'))
    nombre = body.get('nombre')
    apellido = body.get('apellido')
    telefono = body.get('telefono')

    result = table.update_item(
        Key={
            'id': id
        },
       ExpressionAttributeNames={
          '#todo_nombre': 'nombre',
        },
       ExpressionAttributeValues={
          ':nombre': nombre,
          ':apellido': apellido,
          ':telefono': telefono
		  },
       UpdateExpression='SET #todo_nombre = :nombre,'
						'apellido = :apellido, '
						'telefono = :telefono',
       ReturnValues='ALL_NEW'
    )
   
    body = {
        "mensaje": "Cliente actualizado"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response