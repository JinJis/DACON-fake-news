import json
import os

if __name__ == '__main__':
    base_path = os.path.abspath('')
    train_file = 'train_result.json'
    scraped_file = 'fake_filtered_final.json'

    # file paths
    train_path = os.path.join(base_path, train_file)
    scraped_path = os.path.join(base_path, scraped_file)

    with open(train_path, encoding='utf-8') as fh:
        train_data = json.load(fh)

    with open(scraped_path, encoding='utf-8') as fh:
        scraped_data = json.load(fh)

    for s_title in scraped_data:
        if s_title in train_data:
            diff = set(scraped_data[s_title]) - set(train_data[s_title])
            scraped_data[s_title] = list(diff)

    # dump to json
    result_path = os.path.join(base_path, 'fake_filtered_final2.json')
    with open(result_path, 'w', encoding='utf8') as fp:
        json.dump(scraped_data, fp, ensure_ascii=False)
