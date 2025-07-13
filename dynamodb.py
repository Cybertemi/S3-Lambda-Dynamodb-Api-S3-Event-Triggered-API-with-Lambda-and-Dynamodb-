import boto3

#dynamodb = boto3.client('dynamodb')
#response = dynamodb.create_table(
 #       TableName='Students01',
  #      AttributeDefinitions=[
   #         {
    #         'AttributeName': 'StudentID',
     #        'AttributeType': 'S'

      #  },
       # ],
        #KeySchema=[
         #   {
          #   'AttributeName': 'StudentID',
           #  'KeyType': 'HASH'
        #},
        #],
        #ProvisionedThroughput={
         #   'ReadCapacityUnits': 5,
          #  'WriteCapacityUnits': 5
        #},
       

#)

#print(response)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')
students01={
        'StudentID': 'Cloud400',
        'Name': 'JoeDan',
        'Email': 'lookout@yahoo.com'
}
response = table.put_item(
        Item = students01
            
    )


print(response)