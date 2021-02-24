import json
import os
import random
if __name__ == '__main__':
    base_path = os.path.abspath('')
    final_real_file = 'real_filtered_final.json'
    final_real_file_path = os.path.join(base_path, final_real_file)

    with open(final_real_file_path, encoding='utf-8') as fh:
        data = json.load(fh)

    fill_num = 15
    max_index = len(data.keys())
    for index, title in enumerate(data):
        # reset
        data[title] = []
        # choose excluding curr index
        r = list(range(0, index)) + list(range(index + 1, max_index))
        # random choose indexes
        index_picked = random.choices(r, k=fill_num)

        for i_p in index_picked:
            sub_list = list(data.items())[i_p][1]
            if not sub_list:
                continue
            random_sub = random.choice(sub_list)
            data[title].append(random_sub)

    # dump to json
    result_path = os.path.join(base_path, 'fake_filtered_final.json')
    with open(result_path, 'w', encoding='utf8') as fp:
        json.dump(data, fp, ensure_ascii=False)