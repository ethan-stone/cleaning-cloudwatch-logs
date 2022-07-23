import boto3
import time

logs = boto3.client('logs')

def lambda_handler(event, context):
   
    logGroups = logs.describe_log_groups()['logGroups']
    for group in logGroups:
       if 'keyword' not in group['logGroupName']: continue

       daysRetention = group.get('retentionInDays', 0)
       if daysRetention != 7:
           logs.put_retention_policy(logGroupName=group['logGroupName'], retentionInDays=7)
           continue

       maxRetention = time.time()-(daysRetention*86400)

       logStream = logs.describe_log_streams(logGroupName=group['logGroupName'])['logStreams']
       for stream in logStream:
           if (stream['creationTime']/1000) < maxRetention:
               print(f'Deleting: {region} {group["logGroupName"]} {stream["logStreamName"]}')
               logs.delete_log_stream(logGroupName=group['logGroupName'], logStreamName=stream['logStreamName'])
               time.sleep(0.2)





https://books.google.com/books?id=ZNOGDwAAQBAJ&pg=PA310&lpg=PA310&dq=how+to+find+orphaned+cloudwatch+logs&source=bl&ots=6hVAXOQ1Ex&sig=ACfU3U0tjClAORTRUfWILDYBR2VH1s7l7Q&hl=en&sa=X&ved=2ahUKEwi2no-w5I35AhVwLFkFHZ8vDiEQ6AF6BAg0EAM#v=onepage&q=how%20to%20find%20orphaned%20cloudwatch%20logs&f=false


-----------------
display log():


delete_log():


1.This will be scheduled events
2.get all logs group 
3. create a list of all logs group object which are not accessed for last 90 days 

4. create two functions
5. send the log group list which has not been accessed for last DAYS to display fuction 
6. call the delete function with same input but it deletes 



#has have to have a log group and log stream

import boto3
client = boto3.client('logs')
response = client.describe_log_groups()
newlist=[] 
for logs in response['logGroups']:
 newlist.append(logs['logGroupName'])

for i in newlist:
 log=client.put_retention_policy(
     logGroupName=i,
     retentionInDays=30
 )
 print(log)


===================
#!/usr/bin/python3

# describe log groups
# describe log streams
# get log groups with the lastEventTimestamp after some time
# delete those log groups
# have a dry run option
# support profile

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group

import boto3
import time
millis = int(round(time.time() * 1000))

delete = False
debug = False
log_group_prefix='/' # NEED TO CHANGE THESE

days = 30
# Create CloudWatchLogs client
cloudwatch_logs = boto3.client('logs')

log_groups=[]
# List log groups through the pagination interface
paginator = cloudwatch_logs.get_paginator('describe_log_groups')
for response in paginator.paginate(logGroupNamePrefix=log_group_prefix):
    for log_group in response['logGroups']:
        log_groups.append(log_group['logGroupName'])

if debug:
    print(log_groups)

old_log_groups=[]
empty_log_groups=[]
for log_group in log_groups:
    response = cloudwatch_logs.describe_log_streams(
        logGroupName=log_group, #logStreamNamePrefix='',
        orderBy='LastEventTime',
        descending=True,
        limit=1
    )
    # The time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
    if len(response['logStreams']) > 0:
        if debug:
            print("full response is:")
            print(response)
            print("Last event is:")
            print(response['logStreams'][0]['lastEventTimestamp'])
            print("current millis is:")
            print(millis)
        if response['logStreams'][0]['lastEventTimestamp'] < millis - (days * 24 * 60 * 60 * 1000):
            old_log_groups.append(log_group)
    else:
        empty_log_groups.append(log_group)

#fun1 ():

if delete:
    for log_group in old_log_groups:
        response = cloudwatch_logs.delete_log_group(logGroupName=log_group)
    #for log_group in empty_log_groups:
    #    response = cloudwatch_logs.delete_log_group(logGroupName=log_group)
else:
    print("old log groups are:")
    print(old_log_groups)
    print("Number of log groups:")
    print(len(old_log_groups))
    print("empty log groups are:")
    print(empty_log_groups) 


#fun2()



# display 
# delete log group

# log group 

















==========
https://hands-on.cloud/working-with-ecs-in-python-using-boto3/










===========
https://github.com/jomyg/ApplicationLoadBalancer-using-terraform/blob/main/main.tf
https://github.com/emory-libraries/terraform-aws-internal-alb-acm/blob/main/alb.tf
