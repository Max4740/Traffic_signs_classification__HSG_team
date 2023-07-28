import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

# Load the trained model to classify sign
from keras.models import load_model
model_Version = "0"
model_Name = "Traffic_signs_classification_Model_ver" + model_Version + ".h5"
model = load_model(model_Name)

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'
           }

# Initialise GUI
top = tk.Tk()
top.geometry('800x500')
top.title('Traffic signs classification - HSG team: PTNK_220317 , PTNK_220307')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 20, 'bold'))

sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = model.predict(image)[0]
    pred_class = np.argmax(pred) + 1
    sign = classes[pred_class]
    #print(sign , ": ", pred_class)
    sign = "AI prediction: " + sign
    label.configure(background='#f5f5dc')
    label.configure(foreground='#32cd32', text=sign)

def upload_image():
    label.configure(background='#CDCDCD')
    label.configure(foreground='#011638', text="")
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        sizes = 3.0
        uploaded.thumbnail(((top.winfo_width() / sizes), (top.winfo_height() / sizes)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        classify(file_path)
    except:
        sign_image.image = None
        label.configure(background='#f5f5dc')
        label.configure(foreground='#ff0000', text="Error: Can't upload your image! Try again or Try another")


heading = Label(top, text="Project: Traffic signs classification", pady=0, font=('arial', 25, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack(side=TOP, pady=20)

sub_heading = Label(top, text="2023 - SIC - AI Course", pady=0, font=('arial', 20, 'bold'))
sub_heading.configure(background='#CDCDCD', foreground='#364156')
sub_heading.pack(side=TOP, pady=0)

upload = Button(top, text="Upload new image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=TOP, pady=30)

sign_image.pack(side=TOP, expand=True)
label.pack(side=BOTTOM, expand=True)

top.mainloop()
