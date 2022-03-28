#import the required libraries
import urllib.parse
import boto3
import json

# assign the necessary AWS resources
rekognition = boto3.client('rekognition', region_name='eu-west-2')
client = boto3.client('sns')
s3 = boto3.resource('s3')
table = boto3.resource('dynamodb').Table('table1906568')


#function which uses recognition detect text in images. returns a response from recognition
def detect_text(bucket, photo):
    response = rekognition.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})
    return response

#extracts the necessary details from the response above
def extract_details(response, photo):
    for text in response['TextDetections']:
        Id = text["Id"]
        detected_word = text['DetectedText']
        confidence = text["Confidence"]

        print('The word detected is ' + detected_word + ' with a confidence level of: ' + str(confidence))
        table.put_item(Item= {
            'Id': str(Id),
            'image_name': photo,
            'Text_Detected': detected_word,
            'Confidence': str(confidence)
        })
    #use sns to send text to user
    if detected_word.lower() == 'danger' or detected_word.lower() == 'hazard':
        sms = client.publish(
            PhoneNumber = '+251929232033',
            Message = 'harmful text detected in ' + photo + ' and the word was ' + detected_word,
            Subject = 'Alert Triggered!'
        )
        print(sms)
    else:
        print('No harmful text Detected!')

#main lambda handler! iterates the events in the sns topic and runs the functions created above
def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    message = json.loads(message)
    bucket = message['Records'][0]['s3']['bucket']['name']
    image = urllib.parse.unquote_plus(message['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        detected_texts = detect_text(bucket, image)
        extract_details(detected_texts, image)

    except Exception as e:
        print(e)