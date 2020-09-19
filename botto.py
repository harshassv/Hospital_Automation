import boto3
s3 = boto3.resource('s3')
object = s3.Bucket('ben-bucket').Object('db.sqlite')
object.Acl().put(ACL='public-read')
