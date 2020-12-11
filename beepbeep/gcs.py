# TODO add to beepbeep.gcs
import os
from google.cloud import storage


def get_list_of_objects_in_bucket(source_bucket_name: str):
    try:
        project_id = os.environ.get('GCP_PROJECT')
        GCS = storage.Client(project=project_id)
        
        source_bucket = GCS.get_bucket(source_bucket_name)
        bucket_objects = source_bucket.list_blobs()

        bucket_object_list = [bucket_object.name for bucket_object in bucket_objects]

    except Exception as e:
        print(e)
        bucket_object_list = None
    
    return bucket_object_list


def download_object_from_gcs_to_local_path(source_bucket_name, input_filename, file_path="/tmp/"):
    try:
        project_id = os.environ.get('GCP_PROJECT')
        GCS = storage.Client(project=project_id)                

        # ge bucket and object
        origin_bucket = GCS.get_bucket(source_bucket_name)
        blob = origin_bucket.get_blob(input_filename)

        # set path and download        
        local_filepath = file_path + input_filename
        blob.download_to_filename(local_filepath)
        print(f"file {input_filename} downloaded from gs://{source_bucket_name} to {local_filepath}")

    except Exception as e:
        print (e)
        local_filepath = None


    return local_filepath 



def load_file_to_gcs(file: str, destination_bucket_name: str, destination_filename: str):
    try:
        project_id = os.environ.get('GCP_PROJECT')
        GCS = storage.Client(project=project_id)
        bucket = GCS.get_bucket(destination_bucket_name)
        blob = bucket.blob(destination_filename)
        status = blob.upload_from_filename(file)

    except Exception as e:
        print(e)
        status = None

    return status


