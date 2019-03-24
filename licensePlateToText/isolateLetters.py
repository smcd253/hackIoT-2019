from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

car_image = imread("letters.jpg", as_gray=True)
# it should be a 2 dimensional array
print(car_image.shape)

# the next line is not compulsory however, a grey scale pixel
# in skimage ranges between 0 & 1. multiplying it with 255
# will make it range between 0 & 255 (something we can relate better with

gray_car_image = car_image * 255
threshold_value = 30
binary_car_image = gray_car_image > threshold_value
plt.imshow(binary_car_image, cmap="gray")
plt.show()
plt.savefig('lettersIsolated.jpg')