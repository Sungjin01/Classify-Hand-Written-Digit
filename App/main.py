from tkinter import *
from PIL import Image
import torch
import torchvision
import torchvision.transforms as transforms

mycolor = "black"
device = 'cuda' if torch.cuda.is_available() else 'cpu'

def paint(event):
    x1, y1 = ( event.x-1 ), ( event.y-1 )
    x2, y2 = ( event.x+1 ), ( event.y+1 )
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)

def classify_digit():
    save_as_png(canvas, 'digit')
    #load model
    model = torch.load('model/model.pt')
    model.eval()

    image_path = 'test_image/24.png'
    img = torchvision.io.read_image(image_path, torchvision.io.ImageReadMode.GRAY)
    img = transforms.Resize(size=(28, 28))(img)
    img = img.view(1, 1, 28, 28).float().to(device)

    with torch.no_grad():
        prediction = model(img)
        print(torch.argmax(prediction, 1).item())

def save_as_png(canvas,fileName):
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps') 
    img.save(fileName + '.png', 'png') 

window = Tk();
canvas = Canvas(window);
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button = Button(window, text="CLASSIFY",command=classify_digit)
button.pack()
window.mainloop()