import numpy as np
from pylab import imshow, show
from timeit import default_timer as timer

def mandel(x, y, max_iter):
	c = complex(x,y)
	z = 0.0j
	for i in range(max_iter):
		z = z*z + c
		if (z.real * z.real + z.imag*z.imag) >= 4:
			return i
	return max_iter

def create_fractal(min_x, max_x, min_y, max_y, image, iters):
	height, width = image.shape

	pixel_size_x = float(max_x - min_x) / width
	pixel_size_y = float(max_y - min_y) / height

	for x in range(width):
		real = min_x + x * pixel_size_x
		for y in range(height):
			imag = min_y + y * pixel_size_y
			color = mandel(real, imag, iters)
			image[y, x] = color

image = np.zeros((1024, 1536), dtype = np.uint8)
start = timer()
create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20) 
dt = timer() - start

print "Mandelbrot created in %f s" % dt
imshow(image)
show()