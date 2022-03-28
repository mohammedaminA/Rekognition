#import required libraries
import boto3
import time
# os allows us to iterates through files in a directory and access them
import os

s3 = boto3.resource('s3')
directory = 'images'
"""
use the os library to iterate through the files in the images directory and upload each of the files
to the specified S3 bucket with an interval of 10 seconds. 
"""
try:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            head, tail = os.path.split(f)
            s3.meta.client.upload_file(str(f), 'bucket1906568', tail)
            print('Filename:' + " " + tail + " " + "succesfully uploaded!")
            time.sleep(10)

    #inform the user that the files have succesfully been uploaded
    print("All files succesfully uploaded!")

#print any exception that arises
except Exception as e:
    print(e)



