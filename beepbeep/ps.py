# beepbeep.ps: google pubsub functions

import os
import base64
from google.cloud import pubsub_v1


def publish_message_to_pubsub_topic(topic_name:str, attributes_dict: dict) -> dict:
    try:
        project_id = os.environ.get('GCP_PROJECT')
        PS = pubsub_v1.PublisherClient()
        topic_path = f"projects/{project_id}/topics/{topic_name}"
        
        PS.publish(topic_path, b'pipeline_config in attributes', **attributes_dict)
        
        message_status = {"status": "success", "message": f"pubsub message posted to {topic_path}"}

    except Exception as e:
        message_status = {"status": "fail", "message": e}
    
    return message_status


def publish_message_to_pubsub_topic_with_text_payload(topic_name:str, text_payload: str) -> dict:
    try:
        project_id = os.environ.get('GCP_PROJECT')
        PS = pubsub_v1.PublisherClient()
        topic_path = f"projects/{project_id}/topics/{topic_name}"
        
        text_payload_encoded = base64.b64encode(text_payload.encode("utf-8"))

        PS.publish(topic_path, text_payload_encoded)
        
        message_status = {"status": "success", "message": f"pubsub message posted to {topic_path}"}

    except Exception as e:
        message_status = {"status": "fail", "message": e}
    
    return message_status


def build_pubsub_event_payload(text_payload: str, attribute_dict: dict=None) -> dict:

    try:
        # base64 encode text payload
        text_payload_encoded = base64.b64encode(text_payload.encode("utf-8"))

        # construct event dict
        event = {}
        event['data'] = text_payload_encoded
        event['attributes'] = attribute_dict
    
    except Exception as e:
        event = None

    return event


def get_test_event_payload() -> dict:
    
    # construct event dict with default dummy data
    test_payload = build_pubsub_event_payload("payload in attributes", {"key": "test_value"})
    return test_payload

