from CameraCalibration import CameraCalibration
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

calib = CameraCalibration('camera_cal', 9, 6)
img = mpimg.imread('test_images/test1.jpg')
undistorted = calib.undistort(img)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')
plt.subplot(1, 2, 2)
plt.imshow(undistorted)
plt.title('Undistorted')
plt.show()
