import sys
from nsfw_detector import NSFWDetector
detector = NSFWDetector('./nsfw.299x299.h5')
detector_mobilenet = NSFWDetector('./nsfw_mobilenet2.224x224.h5')

print(detector.predict(sys.argv[0]))
#print(detector_mobilenet.predict(sys.argv))