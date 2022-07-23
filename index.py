import boto3
import time
import json

cloudwatch_logs = boto3.client('logs')

CURRENT_TIME_IN_MILLIS = int(round(time.time() * 1000))
MAX_DAYS = 30 

def delete_logs_groups(log_groups):
    for log_group in log_groups:
        cloudwatch_logs.delete_log_group(
            logGroupName=log_group['logGroupName']
        )
        time.sleep(0.2) # artificial sleep to prevent throttling

def display_log_groups(log_groups):
    json_formatted_str = json.dumps(log_groups, indent=2)
    print(json_formatted_str) # print logs to be deleted in easy to read JSON


def handler(event, _):
    log_groups = []

    paginator = cloudwatch_logs.get_paginator('describe_log_groups')
    for response in paginator.paginate(logGroupNamePrefix='/'):
        for log_group in response['logGroups']:
            log_groups.append(log_group)
        time.sleep(0.2) # artificial sleep to prevent throttling

    old_log_groups = []
    empty_log_groups = []

    for log_group in log_groups:
        response = cloudwatch_logs.describe_log_streams(
            logGroupName=log_group['logGroupName'],
            orderBy='LastEventTime',
            descending=True,
            limit=1
        )
        time.sleep(0.2) # artificial sleep to prevent throttling

        if len(response['logStreams']) > 0:
           if response['logStreams'][0]['lastEventTimestamp'] < CURRENT_TIME_IN_MILLIS - (MAX_DAYS * 24 * 60 * 60 * 1000):
             old_log_groups.append(log_group)
        else:
            empty_log_groups.append(log_group) 

    mode = event['mode']

    if mode == 'DISPLAY':
        display_log_groups([*old_log_groups, *empty_log_groups])
    elif mode == 'DELETE':
        delete_logs_groups([*old_log_groups, *empty_log_groups])
    else:
        print(f'UNSUPPORTED MODE: {mode}')