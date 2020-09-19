from cloudstorage.drivers.amazon import S3Driver
storage = S3Driver(key='AKIAI43MM4QUVYVDT5WA', secret='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')

container = storage.create_container('has1234567')
print(container.cdn_url)
#'https://avatars.s3.amazonaws.com/'
'''
avatar_blob = container.upload_blob('/path/my-avatar.png')
print(avatar_blob.cdn_url)
#'https://s3.amazonaws.com/avatars/my-avatar.png'

print(avatar_blob.generate_download_url(expires=3600))
#'https://avatars.s3.amazonaws.com/my-avatar.png?'
#'AWSAccessKeyId=<my-aws-access-key-id>'
#'&Signature=<generated-signature>'
#'&Expires=1491849102'

print(container.generate_upload_url('user-1-avatar.png', expires=3600))
#{
   # 'url': 'https://avatars.s3.amazonaws.com/',
   # 'fields': {
    #    'key': 'user-1-avatar.png',
   #     'AWSAccessKeyId': '<my-aws-access-key-id>',
 #       'policy': '<generated-policy>',
  #      'signature': '<generated-signature>'
    #}
#}
'''
