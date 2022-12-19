import glob
import cv2
import easyocr

def read_image():
    folder = glob.glob("C:\Users\USER\Documents\opencvcitra\DeteksiPlatNomormain/*jpg")
    images = []

    for file in folder:
        images.append(file)

    count = 1

    for image in images:
        frame = cv2.imread(image)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)

        reader = easyocr.Reader(["en"])
        result = reader.readtext(gray)
        for (bbox, text, prob) in result:
            print(count, "Plat Nomor:", text, "| "
            "persentase:", prob)
            count += 1


        cv2.imshow("Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows
