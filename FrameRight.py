import customtkinter
class RightFrame(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.label_output = customtkinter.CTkLabel(self,text="Output")
        self.label_output.grid(row=0,column=0)

        self.text_output = customtkinter.CTkTextbox(self)
        self.text_output.grid(row=1,column=0)