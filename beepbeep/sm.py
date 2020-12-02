# beepbeep.sm: google secrets manager functions

import os
from google.cloud import secretmanager


def get_latest_secret_from_secret_manager(secret_name):
    try:
        # define parameters and instantiate client
        project_id = os.environ.get('GCP_PROJECT')
        secret_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"        
        SM = secretmanager.SecretManagerServiceClient()

        # get response and decode
        secret_response = SM.access_secret_version(name=secret_name)
        secret_value = secret_response.payload.data.decode("UTF-8")
    
    except Exception as e:
        print(e)
        secret_value = None
    
    return secret_value
