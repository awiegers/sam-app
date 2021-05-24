import json
import boto3

region_name = 'us-east-2'
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = 'Cache'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    print('Recieved event: ' + json.dumps(event, indent=2))
    respond(None, res='Hello World!')



def salutations(event, context):
    print("Recieved event: " + json.dumps(event, indent=2))
    scan_result = dynamo.scan(TableName=table_name)
    return respond(None, res=scan_result)