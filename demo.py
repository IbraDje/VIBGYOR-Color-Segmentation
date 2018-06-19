from VIBGYOR import VIBGYORsegmentation
import matplotlib.image as mpimg
import time


name = 'NetHues.jpg'
# name = 'colorcube-1_66.jpg'
# name = 'rainbow-page2.jpg'
img = mpimg.imread(name) # reading the test image
start_time = time.clock() # start calculating execution time
for color in ('v', 'i', 'b', 'g', 'y', 'o', 'r'): # loopig through all 7 colors
    C = VIBGYORsegmentation(img, color) # calling the VIBGYORsegmentation function on the image
    mpimg.imsave(f'{color.upper()} - {name}', C) # saving the resulting image
elapsed_time = time.clock() - start_time # end calculating execution time
print(f'elapsed time : {round(elapsed_time, 3)} seconds') # printing the excution time
