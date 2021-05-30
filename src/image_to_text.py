import os
import shutil
from PIL import Image
import pytesseract
from PIL import Image
import pandas as pd

input_dir="./input"
output_dir="./output"

def extract_texts():    
    files = []
    texts = []
    for root, dirs, filenames in os.walk(input_dir):
        for filename in filenames:
            im = Image.open(input_dir +"/"+filename)
            text = pytesseract.image_to_string(im, lang='eng')
            files.append(filename)     
            texts.append(text)            
    df_file_and_text = pd.DataFrame(data={'file': files, 'text':texts})
    # save texts plus each image filename in a .csv    
    df_file_and_text.to_csv(output_dir+'/file_and_text.csv', index=False,header=True)
    # save texts from all scanned images in another .csv
    df_file_and_text['text'].to_csv(output_dir+'/text_only.txt', index=False,header=False)   

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