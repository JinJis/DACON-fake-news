import csv
import json
import os

if __name__ == '__main__':
    base_path = os.path.abspath('')
    csv_file = 'news_train.csv'
    csv_path = os.path.join(base_path, csv_file)

    result = {}
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            title = row[2]
            subject = row[3]
            if title in result:
                result[title].append(subject)
                continue
            result[title] = [subject]

    # dump to json
    result_path = os.path.join(base_path, 'train_result.json')
    with open(result_path, 'w', encoding='utf8') as fp:
        json.dump(result, fp, ensure_ascii=False)
