# VIBGYOR Color Segmentation
Python implementation of the VIBGYOR Color Segmentation.

- Explanation : 
The distance between peaks (high points) in wave is called wavelength. 
The wavelength term is commonly use in electromagnetic radiation like radios waves, light waves or infrared (heat) waves. 
Each waves containing shapes and length. 
VIBGYOR is just the expression of the color of the spectrum of white light which are Violet, Indigo, Blue, Green, Yellow, Orange and Red. 
Each color is associated with light of a particular wavelength. Red light has longer wavelengths than the blue light. 
The angle of deviation by a prism is not the same for all the wavelength (colors) of light. 
The violet is the most deviated while the red is the least deviated.

The wavelength aka VIBGYOR define the different colour based on their wavelength range on the image, then segment different colour light, and apply the colour filter to remove the colour selected.

- Algorithm

We use a color image, as input image. And we define two functions:

. Function for color image segmentation called VIBGYOR segmentation
  Where we divide different objects on the image in the space. Row, column and planes

  Where plane must be equal to 3.

  Then we can select the color in the image.

. Function for color filter
Is to filter the different color in the image in the space. With this function we extract the color in the image.

Source : https://dipcsc2014.wordpress.com/author/iefyerhemlock/
