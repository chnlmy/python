import os
from PIL import Image
from tqdm import tqdm

ROOT_PATH = os.path.expanduser("~/Documents/Python/sspai examples/05-piczoom")
os.chdir(ROOT_PATH)
PIC_FORMAT = ['.png', '.jpg', '.jpeg']

def BindPath(dir_path, filename):
    return os.path.join(dir_path,filename)

RESIZED_PATH = BindPath(os.getcwd(), "ResizedPics")
if not os.path.exists(RESIZED_PATH):
    os.mkdir(RESIZED_PATH)

for file in tqdm(os.listdir(os.getcwd()), ascii=True):
    name, suffix = os.path.splitext(file)
    if suffix in PIC_FORMAT:
        pic = Image.open(file)
        width, height = pic.size
        pic.thumbnail((width*0.5, height*0.5), Image.ANTIALIAS)
        pic.save(BindPath(RESIZED_PATH, (name+"-resized"+suffix)), 
                  format = suffix.replace('.','').replace('jpg', 'jpeg'), 
                  optimize=True)
    else:
        continue