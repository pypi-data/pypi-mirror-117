import os
import json
import requests as http
import sys
p = '/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/a.mov.json'


def make_url(file_name):
    # '5g_RRC_EA5EAA705108BDA0.pkl'
    return f'https://jiutiandl-ingress-wuxi.cmecloud.cn:30443/CIDC-U-dbc004bd39024f308169a33caa206175-dl-1127497952-pod/api/contents/wuhf/converted/{file_name}?format=text&type=file&content=1&1629873972057'


headers = {
    'authority': 'jiutiandl-ingress-wuxi.cmecloud.cn:30443',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'authorization': 'token mwcex4',
    'x-xsrftoken': '2|e363e14d|6985c40d5a8e0c0c9e3082fe5e9333cf|1629873329',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://jiutiandl-ingress-wuxi.cmecloud.cn:30443/CIDC-U-dbc004bd39024f308169a33caa206175-dl-1127497952-pod/lab',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'username-jiutiandl-ingress-wuxi-cmecloud-cn-30443="2|1:0|10:1629873967|49:username-jiutiandl-ingress-wuxi-cmecloud-cn-30443|44:ZDRiNjZhMGY1NWJhNDkwODk5NzczYzJmZTQ3NzQyYTQ=|62a1314e74732b5d6f7dad6e6187bdbf56faa514651f03f04aeeb4671c6030bc"; _xsrf=2|e363e14d|6985c40d5a8e0c0c9e3082fe5e9333cf|1629873329',
}

with open(p, 'r') as f:
    datasets_meta = json.load(f)


def get_md5(content):
    import hashlib
    return hashlib.md5(content).hexdigest()


def download_dataset(dataset_meta):
    for segment in dataset_meta['segments']:
        file_name = segment['file']
        print(f"INFO: download file{file_name}")
        resp = http.get(make_url(file_name), headers=headers, verify=False)
        resp_dict = json.loads(resp.text)
        file_content = resp_dict['content'].encode('utf-8')
        download_dir = '/Users/wuhf/PycharmProjects/Hypernets/hypernets/hn_widget/hn_widget/test/download'
        with open(os.path.join(download_dir, file_name), 'wb') as f:
            f.write(file_content)
        md5 = segment['md5']
        resp_file_md5 = get_md5(file_content)
        if md5 != resp_file_md5:
            sys.stderr.write(f'ERROR: file {file_name} md5 does not match, md5={md5}, resp_file_md5={resp_file_md5}')


with open(p, 'r') as f:
    datasets_meta = json.load(f)


for i in sys.argv[1].split(","):
    dataset_meta = datasets_meta[int(i)]
    download_dataset(dataset_meta)
    print(f"INFO: downloaded id {i}")
