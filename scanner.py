import customtkinter,socket,time,threading
from FrameRight import RightFrame
from FrameLeft import Leftframe
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Myapp(customtkinter.CTk):
    #Constructor
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("PortScanner")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.background_image = customtkinter.CTkImage(light_image=Image.open('page-banner-network.jpg'),size=(500,300))
        self.background_label = customtkinter.CTkLabel(self,image=self.background_image,text="")
        self.background_label.grid(row=0,column=0, rowspan=2, columnspan=2)

        self.right_frame = RightFrame(self)
        self.right_frame.grid(row=0,column=1,sticky="ne",padx=30,pady=30)

        self.left_frame = Leftframe(self,self.right_frame)
        self.left_frame.grid(row=0, column=0,sticky="nw",padx=70,pady=80)

if __name__ == '__main__' :
    app = Myapp()
    app.mainloop()