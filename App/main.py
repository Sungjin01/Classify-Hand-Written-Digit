from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PIL.ImageGrab as ImageGrab
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

mycolor = "black"
device = 'cuda' if torch.cuda.is_available() else 'cpu'

#Model Define
class CNN(torch.nn.Module):

    def __init__(self):
        super(CNN, self).__init__()
        
        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1)),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2))
        
        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1)),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2))
        
        self.fc = torch.nn.Linear(7*7*64, 10, bias=True)
        #이게 뭔지 찾기
        torch.nn.init.xavier_uniform_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        #flatten
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out

def paint(event):
    x1, y1 = ( event.x-1 ), ( event.y-1 )
    x2, y2 = ( event.x+1 ), ( event.y+1 )
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor, width=4)

def classify_digit():
    save_as_png(canvas, 'digit')
    #load model
    model = torch.load('model/model.pt')
    model.eval()

    image_path = './digit.png'
    img = torchvision.io.read_image(image_path, torchvision.io.ImageReadMode.GRAY)
    img = transforms.Resize(size=(28, 28))(img)
    img = np.invert(img)
    img = img.view(1, 1, 28, 28).float().to(device)
    

    with torch.no_grad():
        prediction = model(img)
        messagebox.showinfo("CLASSIFY", torch.argmax(prediction, 1).item())
        #print(torch.argmax(prediction, 1).item())

def save_as_png(canvas,fileName):
    location = './digit.png'
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    img = ImageGrab.grab(bbox=(x, y, x+350, y+250))
    img.save(location)

def clear():
    canvas.delete("all")

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button1 = Button(window, text="CLASSIFY",command=classify_digit)
button2 = Button(window, text="CLEAR", command=clear)
button1.pack()
button2.pack()
window.mainloop()