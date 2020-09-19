import boto3
s3=boto3.resource('s3')
my_b=s3.Bucket('530045lab')
'''for obj in my_b.objects.filter(Prefix="reciption/"):
    print(obj.key)'''
for obj in my_b.objects.all():
    print(obj.key)
