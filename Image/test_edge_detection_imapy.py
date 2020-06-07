import skimage
import skimage.feature
import skimage.viewer
import sys

image = skimage.io.imread(fname='straw.jpg', as_gray=True)
#viewer = skimage.viewer.ImageViewer(image)
#viewer.show()

sigma = 0.1
low_threshold = 0.05
high_threshold = 0.08

edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)

viewer1 = skimage.viewer.ImageViewer(edges)
viewer1.show()
