import cv2
import easyocr
import matplotlib.pyplot as plt

# Read Image 
image_path = "test1.png"
img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu = True)
text_ = reader.readtext(img)

all_text = ""

for t in text_:
    #print(t)
    bbox, text, score = t
    all_text += text + "\n"

    
    cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
    cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)
    
    file_path = "text_of_ocr.txt"
    
    with open(file_path, "w") as file:
        
        file.write(all_text)
    
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    