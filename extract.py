
from PIL import Image
from pytesseract import pytesseract

def show_text():

    tesseract_exe = r"D:\pycharm_projects\tesseract\tesseract.exe" #path of tessract.exe
    image_path = "File_008.jpg" #path of input image

    input_image = Image.open(image_path)
    pytesseract.tesseract_cmd = tesseract_exe
    extracted_text = pytesseract.image_to_string(input_image)

    file = "extracted_text.txt"
    with open(file, "w") as outfile:
        for s in extracted_text:
            outfile.write("%s" % s)
    print("your words are extracted in extracted_text.txt file")

if __name__ == '__main__':
    show_text()
