# beepbeep.utilities: utility functions

import os
import json

def open_json_from_local_path(filename):

    current_directory = os.environ.get('LOCAL_FOLDER_PATH')
    if current_directory is not None:
        filename_with_path = current_directory + "/" + filename
    else:
        filename_with_path = filename
    
    try:
        open_file = open(filename_with_path, 'r')
        file_contents = json.loads(open_file.read())
    except Exception as e:
        print(e)
        file_contents = None
    
    return file_contents
