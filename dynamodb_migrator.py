import boto3
from myproject.settings import DB_ENDPOINT, DB_TABLE


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=DB_ENDPOINT)

    table = dynamodb.create_table(
        TableName=DB_TABLE,
        KeySchema=[
            {
                'AttributeName': 'created_on',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'created_on',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 2
        }
    )
    return table


if __name__ == '__main__':
    my_table = create_table()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=DB_TABLE)
    print("Table status:", my_table.table_status)
    print(my_table.item_count)

