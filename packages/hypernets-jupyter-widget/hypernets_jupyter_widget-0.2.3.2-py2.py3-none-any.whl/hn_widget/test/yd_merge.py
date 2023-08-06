import json
import os.path
import sys
import uuid
import base64
from os import path as P
datasets_meta_file = '/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/a.mov.json'


def get_md5(content):
    import hashlib
    return hashlib.md5(content).hexdigest()


with open(datasets_meta_file, 'r') as f:
    datasets_meta = json.load(f)

download_dir = '/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/download'
pkl_dir = '/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/pkls'


for dataset_meta in datasets_meta:
    result = b''
    for segment in dataset_meta['segments']:
        seg_file = os.path.join(download_dir, segment['file'])
        with open(seg_file, 'rb') as f:
            result = result + f.read()
    dataset_file = P.join(pkl_dir, P.basename(dataset_meta['file']))
    dataset_md5 = dataset_meta['md5']
    download_bytes = base64.b64decode(result)
    download_file_md5 = get_md5(download_bytes)
    with open(dataset_file, 'wb') as f:
        f.write(download_bytes)
    if dataset_md5 != download_file_md5:
        sys.stderr.write(f"ERROR: {dataset_file}  md5 does not match,dataset_md5={dataset_md5}, download_file_md5={download_file_md5}")
    else:
        print(f"INFO: mergged {dataset_file}")
