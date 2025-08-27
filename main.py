import cv2
import numpy as np
from camcapture import vid
from reddec import reddetection


frame = vid()
reddetection(frame)

