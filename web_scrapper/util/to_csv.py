import os

if __name__ == '__main__':
    base_path = os.path.abspath('')
    final_real_file = '<NEED_OVERRIDE>'
    final_fake_file = '<NEED_OVERRIDE>'

    final_real_file_path = os.path.join(base_path, final_real_file)
    final_fake_file_path = os.path.join(base_path, final_fake_file)
