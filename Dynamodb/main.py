import os
import boto3

from dotenv import load_dotenv

load_dotenv()

DYNAMODB_TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME')

# Create DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb'
)

# Get the table
table = dynamodb.Table(DYNAMODB_TABLE_NAME)


class DynamoDBModel:
    def __init__(self, table_name=DYNAMODB_TABLE_NAME):
        self.table = dynamodb.Table(table_name)

    def get_item(self, key):
        response = self.table.get_item(Key=key)
        return response.get('Item')

    def put_item(self, item):
        response = self.table.put_item(Item=item)
        return response

    def query_items(self, key_condition_expression):
        response = self.table.query(KeyConditionExpression=key_condition_expression)

        return response.get('Items')



