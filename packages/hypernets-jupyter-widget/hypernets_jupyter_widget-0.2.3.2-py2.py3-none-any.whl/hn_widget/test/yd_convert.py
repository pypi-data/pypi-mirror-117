import math
import base64
import uuid
import hashlib
import json
import os



def get_md5(content):
    import hashlib
    return hashlib.md5(content).hexdigest()


def make_segment(index, file, md5, data_len):
    return {
        'index': index,
        'file': file,
        'md5': md5,
        'length': data_len
    }


def convert_file(p):
    print(f"Input file: {p}")
    with open(p, 'rb') as f:
        data = f.read()
    origin_file_md5 = hashlib.md5(data).hexdigest()
    res = base64.b64encode(data)
    print(f"File len: {len(res)}, md5: {origin_file_md5}" )
    segment_size = 16000000
    num_files = int(len(res) / segment_size) + 1
    segments = []
    for i in range(num_files):
        if i == num_files - 1:
            segment_data = res[i * segment_size: ]
        else:
            segment_data = res[i * segment_size: ((i+1)*segment_size)]
        segment_file = '%s.txt' % str(uuid.uuid4())
        with open(segment_file, 'wb') as f:
            f.write(segment_data)
        md5 = hashlib.md5(segment_data).hexdigest()
        segment_meta = make_segment(i, segment_file, md5 , len(segment_data))
        print(json.dumps(segment_meta))
        segments.append(segment_meta)
    full_meta_data = {
        'file': p,
        'md5': origin_file_md5,
        'segments': segments
    }
    with open(os.path.basename(p) + '.json', 'w') as f:
        f.write(json.dumps(full_meta_data))

# convert_file(p)

#
dataset_dir = '/root/workspace/dataset'
for file_name in os.listdir(dataset_dir):
    pkl_file = os.path.join(dataset_dir, file_name)
    if pkl_file[-3:] == 'pkl':
        print(pkl_file)
