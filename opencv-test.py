import cv2
filepath = input("File path of the image (press enter to see a banana): ")
windowTitle = 'This is your image'
if filepath == '':
    filepath = 'Banana.jpg'
    windowTitle = "This is a banana"
print("Image Color:\n1 - Color\n2 - Grayscale\n3 - Unchanged")
try:
    cvflag = int(input("Select Color (Default: 1): "))
except:
    cvflag = 1
if cvflag > 3:
    print("Choose only 1 - 3...\nExitting...")
    exit()
elif cvflag == 3:
    cvflag = -1
elif cvflag == 2:
    cvflag = 0

readCvImage = cv2.imread(filepath, cvflag)
try:
    cv2.imshow(windowTitle, readCvImage)
except:
    print("Invalid File Location...\nExitting...")
    exit()
cv2.waitKey(0)
cv2.destroyAllWindows()