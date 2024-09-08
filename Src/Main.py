# Start the DL Model

import boto3
def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:us-east-2:002743134469:project/plant-leaf-disease-detection/1710264747512'
    model_arn='arn:aws:rekognition:us-east-2:002743134469:project/plant-leaf-disease-detection/version/plant-leaf-disease-detection.2024-03-12T23.30.49/1710266449012'
    min_inference_units=1 
    version_name='plant-leaf-disease-detection.2024-03-12T23.30.49'
    start_model(project_arn, model_arn, version_name, min_inference_units)

if __name__ == "__main__":
    main()

# Detect the disease
import boto3
import io
from PIL import Image, ImageDraw, ImageFont

def display_image(bucket, photo, response):
    # Load image from S3 bucket
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=photo)
    stream = io.BytesIO(obj['Body'].read())
    image = Image.open(stream)

    # Ready image to draw bounding boxes on it.
    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    # calculate and display bounding boxes for each detected custom label
    print('Detected custom labels for ' + photo)
    for customLabel in response['CustomLabels']:
        print('Label: ' + str(customLabel['Name']))
        print('Confidence: ' + str(customLabel['Confidence']))
        if 'Geometry' in customLabel:
            box = customLabel['Geometry']['BoundingBox']
            left = imgWidth * box['Left']
            top = imgHeight * box['Top']
            width = imgWidth * box['Width']
            height = imgHeight * box['Height']

            fnt = ImageFont.truetype('arial.ttf', 50)
            draw.text((left, top), customLabel['Name'], fill='#00d400', font=fnt)

            print('Left: ' + '{0:.0f}'.format(left))
            print('Top: ' + '{0:.0f}'.format(top))
            print('Label Width: ' + "{0:.0f}".format(width))
            print('Label Height: ' + "{0:.0f}".format(height))

            points = (
                (left, top),
                (left + width, top),
                (left + width, top + height),
                (left, top + height),
                (left, top))
            draw.line(points, fill='#00d400', width=5)
        else:
            print("No geometry for this label")

    image.show()

def detect_custom_labels(model_arn, bucket, photo, min_confidence):
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_custom_labels(
        ProjectVersionArn=model_arn,
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MinConfidence=min_confidence
    )
    display_image(bucket, photo, response)
    return len(response['CustomLabels'])

def main():
    bucket = 'custom-labels-console-us-east-2-174350573c'
    photo = 'Image4.jpg'
    model_arn = 'arn:aws:rekognition:us-east-2:002743134469:project/plant-leaf-disease-detection/version/plant-leaf-disease-detection.2024-03-12T23.30.49/1710266449012'
    min_confidence = 95  # Adjust confidence threshold as needed

    label_count = detect_custom_labels(model_arn, bucket, photo, min_confidence)
    print("Custom labels detected:", label_count)

if __name__ == "__main__":
    main()

# Stop the Dl Model
import boto3
import time

def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:us-east-2:002743134469:project/plant-leaf-disease-detection/version/plant-leaf-disease-detection.2024-03-12T23.30.49/1710266449012'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 
