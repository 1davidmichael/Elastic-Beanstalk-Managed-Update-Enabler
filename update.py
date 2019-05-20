import boto3
import datetime


def update_eb_environment(app_name, env_name, env_id):
    response = client.update_environment(
        ApplicationName=app_name,
        EnvironmentId=env_id,
        EnvironmentName=env_name,
        OptionSettings=[
            {
                'Namespace': 'aws:elasticbeanstalk:managedactions',
                'OptionName': 'ManagedActionsEnabled',
                'Value': 'true'
            },
            {
                'Namespace': 'aws:elasticbeanstalk:managedactions',
                'OptionName': 'PreferredStartTime',
                'Value': 'Tue:07:00'
            },
            {
                'Namespace': 'aws:elasticbeanstalk:managedactions:platformupdate',
                'OptionName': 'UpdateLevel',
                'Value': 'minor'
            },
            {
                'Namespace': 'aws:elasticbeanstalk:managedactions:platformupdate',
                'OptionName': 'InstanceRefreshEnabled',
                'Value': 'false'
            }
        ]
    )
    print(response)


client = boto3.client('elasticbeanstalk', region_name='us-west-2')

environments = client.describe_environments()
for environment in environments['Environments']:
    if 'staging' in environment['EnvironmentName']:
        app_name = environment['ApplicationName']
        env_name = environment["EnvironmentName"]
        env_id = environment["EnvironmentId"]
        update_eb_environment(app_name, env_name, env_id)
