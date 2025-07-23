"""
Lane Lines Detection pipeline with Object Detection

Usage:
    main.py [--video] INPUT_PATH OUTPUT_PATH 

Options:
    -h --help       Show this screen
    --video         Process video file instead of image
"""

import numpy as np
import matplotlib.image as mpimg
import cv2
from docopt import docopt
from moviepy.editor import VideoFileClip

from CameraCalibration import CameraCalibration
from Thresholding import *
from PerspectiveTransformation import *
from LaneLines import *
from ObjectDetector import ObjectDetector  # ✅ New import


class FindLaneLines:
    """ Lane line and object detection pipeline. """

    def __init__(self):
        """ Init application components. """
        self.calibration = CameraCalibration('camera_cal', 9, 6)
        self.thresholding = Thresholding()
        self.transform = PerspectiveTransformation()
        self.lanelines = LaneLines()
        self.detector = ObjectDetector()  # ✅ Init YOLO detector

    def forward(self, img):
        """ Complete processing pipeline for a single frame/image. """
        out_img = np.copy(img)

        # Lane detection steps
        img = self.calibration.undistort(img)
        img = self.transform.forward(img)
        img = self.thresholding.forward(img)
        img = self.lanelines.forward(img)
        img = self.transform.backward(img)

        # Overlay lane lines on original
        out_img = cv2.addWeighted(out_img, 1, img, 0.6, 0)
        out_img = self.lanelines.plot(out_img)

        # ✅ Object detection (YOLO)
        results = self.detector.detect(out_img)
        out_img = self.detector.draw_boxes(out_img, results)

        return out_img

    def process_image(self, input_path, output_path):
        """ Process a single image. """
        img = mpimg.imread(input_path)
        out_img = self.forward(img)
        mpimg.imsave(output_path, out_img)

    def process_video(self, input_path, output_path):
        """ Process a video file frame-by-frame. """
        clip = VideoFileClip(input_path)
        out_clip = clip.fl_image(self.forward)
        out_clip.write_videofile(output_path, audio=False)


def main():
    args = docopt(__doc__)
    input_path = args['INPUT_PATH']
    output_path = args['OUTPUT_PATH']

    findLaneLines = FindLaneLines()
    if args['--video']:
        findLaneLines.process_video(input_path, output_path)
    else:
        findLaneLines.process_image(input_path, output_path)


if __name__ == "__main__":
    main()
