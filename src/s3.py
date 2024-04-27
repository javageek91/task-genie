import boto3 as bo3
print(bo3.__version__)
aws_management_console_default = bo3.Session(profile_name="default")
iam_console = aws_management_console_default.resource('iam')
for each_user in iam_console.users.all():
    print(each_user.name)

