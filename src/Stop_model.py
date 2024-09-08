import boto3

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
