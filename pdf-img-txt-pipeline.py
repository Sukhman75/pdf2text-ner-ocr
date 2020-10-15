import cv2
import pytesseract
from pdf2image import convert_from_path


def pdf2img(pdf_file):
    images = convert_from_path(pdf_file)
    for page in images:
        page.save("%s-page%d.jpg" % (pdf_file,images.index(page)), "JPEG")
        image_name = "%s-page%d.jpg" % (pdf_file,images.index(page))
        image_2_text(image_name)
def image_2_text(image="test_img.png"):
    img_cv = cv2.imread(image)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img_rgb).encode('ascii','ignore'))
pdf2img("cover_letter.pdf")