#import boto3 library which manages AWS services
import boto3

#create a local var s3 and assign it an AWS S3 resource
s3 = boto3.resource('s3')

try:
    #create a new bucket and specify its name and location attributes
    s3.create_bucket(Bucket = 'bucket1906568', CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})

    #inform user bucket creation was succesful
    print('Bucket Created Succesfully')

#print any exception that arises
except Exception as e:
    print(e)

