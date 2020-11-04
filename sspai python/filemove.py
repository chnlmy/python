import os
import shutil
from glob import glob

os.chdir(os.path.expanduser('~/Documents/Python/sspai examples/06-file-classify'))

dir_files = set(map(lambda f: f.split(sep='.')[1],os.listdir()))
print(dir_files)

def move_file(suffix):
    for single_file in glob('*.{}'.format(suffix)):
        shutil.move(single_file, class_dir)
        print(f'flie:{single_file} moved to --> dir: {class_dir}')

for suffix in dir_files:
    class_dir = '{}'.format(suffix)
    if not os.path.exists(class_dir):
        os.mkdir(suffix)
        move_file(suffix)
    else:
        move_file(suffix)