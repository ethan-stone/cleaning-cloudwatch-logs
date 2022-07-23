# Setup Steps

1. Navigate to lamda service in aws by searching for lambda in the search bar.
2. Select Functions in the left navigate bar and select Create Function.
3. Choose a function name, select python3.9 as the runtime and x86_64 as the architecture. Other settings can remain the default. Click Create.
4. Afterwards you should be brought to the page for the new function. Under Code select Upload from and upload the zip file provided.
5. Then go to the Configuration tab and select Permissions. Then click on the link in the section labeled Execution role.
6. This should bring you to the IAM policy for the function. Under the section labeled Permissions policies, click Add perimssion, and then select Create inline policy
7. Copy and paste the inline policy below in the JSON editor

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
