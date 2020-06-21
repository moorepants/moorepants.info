import os

import boto

conn = boto.connect_s3(host='objects-us-east-1.dream.io')

bucket = conn.get_bucket('moorepants')

assets_dir = 'assets'

files = os.listdir(assets_dir)

for fname in files:
    key = boto.s3.key.Key(bucket, fname)
    if key.exists():
        print('Skipping: {} (already present in the bucket)'.format(fname))
    else:
        print('Uploading: {}'.format(fname))
        key.set_contents_from_filename(os.path.join(assets_dir, fname))

for o in bucket.list():
    o.set_acl('public-read')
