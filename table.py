import boto3

#create var dynamodb and assign it an AWS dynamod resource
dynamodb = boto3.resource('dynamodb')

try:
    #create the dynamodb table
    table = dynamodb.create_table(
        TableName = 'table1906568',
        KeySchema = [
                {
                    'AttributeName': 'Id',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'Id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
            }

    )
    # inform the user that table was created succesfully
    print('Table Creation Success!!')

#print any exception that arises
except Exception as e:
    print(e)