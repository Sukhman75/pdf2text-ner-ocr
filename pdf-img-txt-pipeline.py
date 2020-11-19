import cv2
import spacy
import pytesseract

from pytesseract import Output
from pdf2image import convert_from_path

nlp = spacy.load("en_core_web_lg")
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# fontScale 
fontScale = 1   
# Blue color in BGR 
color = (255, 0, 0) 
# Line thickness of 2 px 
thickness = 1

def get_entities(text):
    doc = nlp(text)
    labels = []
    for ent in doc.ents:
        #print(ent.text, ent.start_char, ent.end_char, ent.label_)
        labels.append(ent.label_)
    return labels   

def image_2_text(image="test_img.png"):
    img_cv = cv2.imread(image)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img_rgb).encode('ascii','ignore'))
    print(pytesseract.image_to_data(img_rgb, output_type=Output.DICT))
    data = pytesseract.image_to_data(img_rgb, output_type=Output.DICT)
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            text = data['text'][i]
            #print(text)
            ent_str = " | ".join(get_entities(text))
            print(ent_str)
            img_rgb = cv2.putText(img_rgb, ent_str, (x, y), font,  
                   fontScale, color, thickness, cv2.LINE_AA)
            img_rgb = cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("out", img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def pdf2img(pdf_file):
    images = convert_from_path(pdf_file)
    for page in images:
        page.save("%s-page%d.jpg" % (pdf_file,images.index(page)), "JPEG")
        image_name = "%s-page%d.jpg" % (pdf_file,images.index(page))
        image_2_text(image_name)  

if __name__ == "__main__":          
    pdf2img("cover_letter.pdf")

