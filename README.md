# image_to_text python script
Scan images in a given input folder with the tesseract OCR (via its python wrapper) and generate in an output folder :
1. a .txt file with a concatenation of all texts extracted from images
2. a .csv file with 2 columns : "file" and "text"
     "file" : the image filename
     "text" : text content of the image    

# Installation
1. download and install tesseract : 
    https://digi.bib.uni-mannheim.de/tesseract/?C=M;O=A
2. install pytesseract:
    https://pypi.org/project/pytesseract/
    for example :
    pip install pytesseract