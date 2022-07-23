# Setup Steps

1. Navigate to lambda service in aws by searching for lambda in the search bar.
2. Select Functions in the left navigate bar and select Create Function.
![image](https://user-images.githubusercontent.com/46607985/180625874-5b139982-394c-42e6-9d6a-67ed4aed9a02.png)
3. Choose a function name, select python3.9 as the runtime and x86_64 as the architecture. Other settings can remain the default. Click Create.
![image](https://user-images.githubusercontent.com/46607985/180625913-4570866a-e79b-47a5-a9f1-37e691046a30.png)
4. Afterwards you should be brought to the page for the new function. Under Code select Upload from and upload the zip file provided.
![image](https://user-images.githubusercontent.com/46607985/180625928-a9f34c96-cb1f-4b56-a5da-df5c3f5efc13.png)
5. Then go to generatl configuration and select Edit. Change the timeout to 2 minutes for now. This can be increased up to 15 minutes if needed.
![image](https://user-images.githubusercontent.com/46607985/180626334-1111b04b-2958-4242-82b1-30b827927c85.png)
6. Then scroll down to Runtime Settings and select Edit. Change the Handler to `index.handler`
![image](https://user-images.githubusercontent.com/46607985/180626254-b58581d5-71e5-435c-be8f-8c94e3e7ba6b.png)
7. Then go to the Configuration tab and select Permissions. Then click on the link in the section labeled Execution role.
![image](https://user-images.githubusercontent.com/46607985/180625940-b6628c2b-dd87-42d4-a024-c669b5ef5251.png)
8. This should bring you to the IAM policy for the function. Under the section labeled Permissions policies, click Add perimssion, and then select Create inline policy
![image](https://user-images.githubusercontent.com/46607985/180625951-c3382e11-adc6-4918-bd6b-820464f92821.png)
9. Copy and paste the inline policy below in the JSON editor. This gives the function permission to list all log groups and log streams, as well as delete all log groups.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:DeleteLogGroup",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```
10. Afterwards click review Policy in the bottom right. Then on the next page select a name for the policy, then click Create Policy.
11. Finally you can test the function. Navigate back to the functions page and select the test tab. Configure a test event as shown in the picture. Most importantly the event should be a JSON object with a key `mode`, where the value is either `DISPLAY` or `DELETE`
![image](https://user-images.githubusercontent.com/46607985/180626089-57634128-ba69-4709-9770-e544f23c27eb.png)
