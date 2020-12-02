# beepbeep.fb: facebook graph api functions

import requests
from datetime import datetime


def debug_access_token(access_token):
    """
    API Endpoint: https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}
    """
    debug_url = f"https://graph.facebook.com/debug_token?input_token={access_token}&access_token={access_token}"
    response = requests.get(debug_url)

    return response.json()


def get_token_expiry_dates(debug_response):
    token_dates = {}
    token_dates['issued_at'] = datetime.fromtimestamp(debug_response['data']['issued_at']).strftime("%m/%d/%Y, %H:%M:%S")
    token_dates['data_access_expires_at'] = datetime.fromtimestamp(debug_response['data']['data_access_expires_at']).strftime("%m/%d/%Y, %H:%M:%S")
    token_dates['expires_at'] = datetime.fromtimestamp(debug_response['data']['expires_at']).strftime("%m/%d/%Y, %H:%M:%S")
    
    return token_dates


def exchange_token(api_version, client_id, client_secret, access_token):
    """
    API Endpoint =  https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    """
    exchange_url =  f"https://graph.facebook.com/{api_version}/oauth/access_token?grant_type=fb_exchange_token&client_id={client_id}&client_secret={client_secret}&fb_exchange_token={access_token}"
    response = requests.get(exchange_url)
    
    return response.json()


def get_valid_insights_metrics(media_type):
    all_field_parameters = {"IMAGE": ['engagement', 'impressions', 'reach', 'saved'],
                            "VIDEO": ['engagement', 'impressions', 'reach', 'saved', 'video_views'],
                            "CAROUSEL_ALBUM": ['carousel_album_engagement', 'carousel_album_impressions', 'carousel_album_reach', 'carousel_album_saved'],
                            "STORY": ['exits', 'impressions', 'reach', 'replies', 'taps_forward', 'taps_back']
                            }
    valid_metrics = all_field_parameters[media_type]
    
    return valid_metrics


def get_media_objects(api_version, ig_user_id, fields, access_token):
    """
    API Endpoint = https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}
    """
    if type(fields) == list:
        fields = ','.join(fields)
    
    media_objects_url = f"https://graph.facebook.com/{api_version}/{ig_user_id}/media?fields={fields}&access_token={access_token}"
    #print('media_objects request:', media_objects_url)

    response = requests.get(media_objects_url)
    
    return response.json()


def get_media_insights (api_version, ig_media_id, metrics, access_token):
    """
    API Endpoint = https://graph.facebook.com/v9.0/{ig-media-id}/insights?metric={metrics}&access_token={access-token}
    """
    if type(metrics) == list:
        metrics = ','.join(metrics)

    media_insights_url = f"https://graph.facebook.com/{api_version}/{ig_media_id}/insights?metric={metrics}&access_token={access_token}"
    #print('media_insights request:', media_insights_url)
    response = requests.get(media_insights_url)
    
    return response.json()


def get_user_insights (api_version, ig_user_id, metrics, period, since, until, access_token):
    """
    API Endpoint = https://graph.facebook.com/v9.0/{ig-user-id}/insights?metric={metric}&period={period}&since={since}&until={until}&access_token={access-token}
    """
    if type(metrics) == list:
        metrics = ','.join(metrics)

    user_insights_url = f"https://graph.facebook.com/v9.0/{ig_user_id}/insights?metric={metrics}&period={period}&since={since}&until={until}&access_token={access_token}"
    #print('user_insights_url request:', user_insights_url)
    response = requests.get(user_insights_url)
    
    return response.json()
