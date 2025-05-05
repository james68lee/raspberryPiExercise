import numpy as np
from PIL import Image
import gradio as gr

def rgb2gray(input):
    img = Image.fromarray(input)
    img = img.convert('L')
    return np.array(img)
    
app = gr.Interface(rgb2gray,
                   gr.Image(image_mode="RGB"), 
                   "image")
app.launch(server_name="raspberrypi.local")