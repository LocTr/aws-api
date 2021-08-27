import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')
logging.getLogger().setLevel(logging.DEBUG)


def error_response(statusCode, body):
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }
    
def success_response(statusCode, body):
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }

def lambda_handler(event, context):
    logging.debug(event)
    try:
        id = event["queryStringParameters"]['id']
        
        response = table.get_item(
          Key={
            id,
          })
        item = response['Item']
        return success_response(200, item)
    except ClientError:
        return error_response(404, 'Malformed request')
    except KeyError: 
        return error_response(404, 'Book does not exist')
    except:
        logging.critical(event)
        return error_response(404, 'Unexpected error')
    