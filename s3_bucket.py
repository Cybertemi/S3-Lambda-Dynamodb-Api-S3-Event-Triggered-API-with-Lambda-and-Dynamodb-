import boto3

client = boto3.client('s3', region_name= 'eu-north-1')

#response = client.create_bucket(
     #Bucket= 'kodi1-boto3-bucket',
    # CreateBucketConfiguration={
   #      'LocationConstraint': 'eu-north-1'
  #  }
 #)

#print(response)

response = client.put_object(
     Body= ('IGW.png'),
     Bucket= 'kodi1-boto3-bucket',
     Key= 'IGW.png',

 )

print(response)
