import boto3
import os
bucket='530045lab'
entry='7673947687'
s3 = boto3.client('s3')
s3.download_file(bucket, '{}.txt'.format(entry), 'lab.txt')
x=open('lab.txt','r').read().split('\n')
for i in x:
    print(i)
os.remove("lab.txt")
#Write try except block for this program
