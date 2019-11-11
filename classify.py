import sys
from nsfw_detector import NSFWDetector
detector = NSFWDetector('../models/nsfw.299x299.h5')
detector_mobilenet = NSFWDetector('../models/nsfw_mobilenet2.224x224.h5')

for file in sys.argv[1:]:
    try:
         classification = detector.predict(file,image_size=(299,299))
         score = classification[file]
         #if score['porn'] > 0.9:
         print(file)
         display(Image(filename = file, width=200, height=200))
         print(score)
    except:
        pass
            #traceback.print_exc(file=sys.stdout)
#print(detector_mobilenet.predict(sys.argv))
