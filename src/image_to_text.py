import os
import shutil
from PIL import Image
import pytesseract
from PIL import Image
import pandas as pd

input_dir="./input"
output_dir="./output"

def extract_texts():    
    texts =[]
    for root, dirs, filenames in os.walk(input_dir):
        for filename in filenames:
            im = Image.open(input_dir +"/"+filename)
            text = pytesseract.image_to_string(im, lang='eng')
            texts.append(text)
            df=pd.DataFrame(texts)
    df.to_csv(output_dir+'/output.csv', index=False)
    #open the output file and see

def main():
    # init output dirctory
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir)
    extract_texts()

if __name__ == '__main__':
    main()