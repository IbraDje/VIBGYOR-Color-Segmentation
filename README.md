# VIBGYOR Color Segmentation
Python implementation of the VIBGYOR Color Segmentation Algorithm.

The distance between peaks (high points) in wave is called wavelength. The wavelength term is commonly use in electromagnetic radiation like radios waves, light waves or infrared (heat) waves. Each waves containing shapes and length. VIBGYOR is just the expression of the color of the spectrum of white light, which are Violet, Indigo, Blue, Green, Yellow, Orange and Red. Each color is associated with light of a particular wavelength. Red light has longer wavelengths than the blue light. The angle of deviation by a prism is not the same for the entire wavelength (colors) of light. The violet is the most deviated while the red is the least deviated.
The wavelength aka VIBGYOR define the different color based on their wavelength range on the image, then segment different color light, and apply the color filter to remove the color selected.
- Algorithm explanation:
We use a color image, as input image. We define two functions:
1.	Function for color image segmentation :<br>
•	Where we divide different objects on the image in the space. Row, column and planes.<br>
•	Where plane must be equal to three.<br>
•	Then we can select a color in the image.<br>
2.	Function for color filter:<br>
•	Is to filter the different colors in the image in the space. With this function, we extract the selected color in the image<br>

Source : https://dipcsc2014.wordpress.com/author/iefyerhemlock/


<h3>Parameters of the main function (VIBGYORsegmentation) :</h3>
    <ul>
        <li><u>image</u> : a 3D numpy array (plane must be equal to 3)</li>
        <li><u>color</u> :<br><ul>
            <li>'v' / 'V' - for <b>Violet</b> Color</li>
            <li>'i' / 'I' - for <b>Indigo</b> Color</li>
            <li>'b' / 'B' - for <b>Blue</b> Color</li>
            <li>'g' / 'G' - for <b>Green</b> Color</li>
            <li>'y' / 'Y' - for <b>Yellow</b> Color</li>
            <li>'o' / 'O' - for <b>Orange</b> Color</li>
            <li>'r' / 'R' - for <b>Red</b> Color</li>
        </ul></li>
    </ul>
<h3>Return values :</h3>
    <ul><li><u>C</u> : the filtered image</li></ul>
