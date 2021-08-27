import boto3
import logging
import json

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
    try:
        id = event['id']
        title = event['title']
        author = event['author']
        
        result = table.update_item(Key={
            'id': id,
        },
        UpdateExpression='SET title = :title, author = :author',
        ExpressionAttributeValues={
            ':title' : title,
            ':author' : author
        })
        return success_response(200, 'book edited')
    except ClientError:
        return error_response(404, 'Malformed request')
    except KeyError as err:
        return error_response(404, 'Book does not exist')
    except:
        logging.critical(event)
        return error_response(404, 'Unexpected error')

