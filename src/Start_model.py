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
