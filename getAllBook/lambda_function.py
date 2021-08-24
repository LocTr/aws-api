import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')

def lambda_handler(event, context):
    try:
        result = table.update_item(Key={
            'id': event['id'],
        },
        UpdateExpression='SET title = :title, author = :author',
        ExpressionAttributeValues={
            ':title' : event['title'],
            ':author' : event['author']
        }
        )
        return {
            'statusCode': 200,
            'body': 'book updated'
        }
    except KeyError as err:
        return{
            'statusCode': 400,
            'body': 'book does not exist'
        }
    return {
        'statusCode': 404,
        'body': 'Unexpected error'
    }
