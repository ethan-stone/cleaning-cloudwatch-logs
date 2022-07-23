# Setup Steps

1. Navigate to lambda service in aws by searching for lambda in the search bar.
2. Select Functions in the left navigate bar and select Create Function.
![image](https://user-images.githubusercontent.com/46607985/180625874-5b139982-394c-42e6-9d6a-67ed4aed9a02.png)
4. Choose a function name, select python3.9 as the runtime and x86_64 as the architecture. Other settings can remain the default. Click Create.
5. Afterwards you should be brought to the page for the new function. Under Code select Upload from and upload the zip file provided.
6. Then go to the Configuration tab and select Permissions. Then click on the link in the section labeled Execution role.
7. This should bring you to the IAM policy for the function. Under the section labeled Permissions policies, click Add perimssion, and then select Create inline policy
8. Copy and paste the inline policy below in the JSON editor

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
