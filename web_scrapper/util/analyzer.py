import os
import json


if __name__ == '__main__':
    base_path = os.path.abspath('')
    result_name = '<NEED_OVERRIDE>'
    result_path = os.path.join(base_path, result_name)
    with open(result_path, encoding='utf-8') as fh:
        data = json.load(fh)

    num_keys = len(data.keys())
    num_vals = 0
    for _, val in data.items():
        if type(val) is list:
            num_vals += len(val)

    print(num_keys)
    print(num_vals)