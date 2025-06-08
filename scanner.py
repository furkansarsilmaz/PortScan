import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Myapp(customtkinter.CTk):
    #our Constructor
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Mein App")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)


        self.right_frame = RightFrame(self)
        self.right_frame.grid(row=0,column=1,sticky="ne",padx=30,pady=30)

        self.myframe = Leftframe(self,self.right_frame)
        self.myframe.grid(row=0, column=0,sticky="nw",padx=70,pady=30)

        
class Leftframe(customtkinter.CTkFrame):
    def __init__(self,parent,right_frame):
        super().__init__(parent)
        self.right_frame = right_frame
        #for the beginning of the ip values
        self.ip_label = customtkinter.CTkLabel(self,text="IP :")
        self.ip_label.grid(row=0,column=0)

        self.ip_text_box = customtkinter.CTkTextbox(self,width=50,height=10)
        self.ip_text_box.grid(row=0,column=1)
        
        #for the end of the ip values
        self.ip2_label = customtkinter.CTkLabel(self,text="IP2 :")
        self.ip2_label.grid(row=1,column=0)

        self.ip2_text_box = customtkinter.CTkTextbox(self,width=50,height=10)
        self.ip2_text_box.grid(row=1,column=1)

        self.submit_button = customtkinter.CTkButton(self,width=30,text="Submit",command=self.get_ip1)
        self.submit_button.grid(row=2,column=0)

        self.save_button = customtkinter.CTkButton(self,width=40,text="Save")
        self.save_button.grid(row=2,column=1)

    def get_ip1(self):
        ip_one = self.ip_text_box.get("0.0","end")
        ip_two = self.ip2_text_box.get("0.0","end")
        int_ip_one = int(ip_one)
        int_ip_two = int(ip_two)
        if int_ip_one < 0 or int_ip_two < 0 :
            print("Number should be greater than zero")
        else:
            self.right_frame.text_output.insert("0.0","Working on it...")

class RightFrame(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.label_output = customtkinter.CTkLabel(self,text="Output")
        self.label_output.grid(row=0,column=0)

        self.text_output = customtkinter.CTkTextbox(self)
        self.text_output.grid(row=1,column=0)

if __name__ == '__main__' :
    app = Myapp()
    app.mainloop()