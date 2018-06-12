from VIBGYOR import VIBGYORsegmentation
import matplotlib.image as mpimg
import time

name = 'NetHues.jpg'
img = mpimg.imread(name)
start_time = time.clock()
for color in ('v', 'i', 'b', 'g', 'y', 'o', 'r'):
    C = VIBGYORsegmentation(img, color)
    mpimg.imsave(f'{color.upper()} - {name}', C)
elapsed_time = time.clock() - start_time
print(f'elapsed time : {round(elapsed_time, 3)} seconds')
