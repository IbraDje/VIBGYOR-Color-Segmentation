from VIBGYOR import VIBGYORsegmentation
import matplotlib.image as mpimg
import time


name = 'NetHues.jpg'
# name = 'colorcube-1_66.jpg'
# name = 'rainbow-page2.jpg'
img = mpimg.imread(name)
start_time = time.clock()
for color in ('v', 'i', 'b', 'g', 'y', 'o', 'r'):
    C = VIBGYORsegmentation(img, color)
    mpimg.imsave(f'{color.upper()} - {name}', C)
elapsed_time = time.clock() - start_time
print(f'elapsed time : {round(elapsed_time, 3)} seconds')
