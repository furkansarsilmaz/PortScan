import customtkinter,socket,threading
from FrameRight import RightFrame
from PIL import Image

class Leftframe(customtkinter.CTkFrame):
    def __init__(self,parent,right_frame):
        super().__init__(parent)
        """
        self.banner = customtkinter.CTkImage(light_image=Image.open('page-banner-network.jpg'),size=(100,100))
        self.banner_label = customtkinter.CTkLabel(self,image=self.banner,text="")
        self.banner_label.grid(row=0,column=0,columnspan=2,pady=10)
        """
        
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

        #self.save_button = customtkinter.CTkButton(self,width=40,text="Save",command=self.saver)
        #self.save_button.grid(row=2,column=1)

    def get_ip1(self):
        host = "127.0.0.1"
        self.right_frame.text_output.delete(0.0,"end")
        ip_one = self.ip_text_box.get("0.0","end").strip()
        ip_two = self.ip2_text_box.get("0.0","end").strip()
        
        try:
            int_ip_one = int(ip_one)
            int_ip_two = int(ip_two)

            if int_ip_one < 0 or int_ip_two < 0 :
                print("Number should be greater than zero")

            else:
                """
                with for loop, create a socket and try to connect it to
                the host address. If result is zero it is open, if not 
                it is close.
                """
                for i in range(int_ip_one,int_ip_two+1,1):
                    thread = threading.Thread(target=self.scan_ips,args=(host,i))
                    thread.start()
                self.saver()

        except ValueError:
            self.right_frame.text_output.insert("0.0","Please give a number\n")

    def scan_ips(self,host,port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0 :
            self.right_frame.text_output.insert("0.0",f"{port} port is open...\n")
        else :
            self.right_frame.text_output.insert("0.0",f"{port} port is close...\n")
        s.close()


    def saver(self):
        dialog = customtkinter.CTkInputDialog(title="Saver",text="Do you want to save the results ? (y or n)")
        user_input = dialog.get_input()
        if user_input == 'y' or user_input == 'Y' :
            print("Saving...")
            with open("dosya.txt","w") as d :
                d.write(self.right_frame.text_output.get("0.0","end"))
        elif user_input == 'n' or user_input == 'N' :
            exit()
        else:
            exit()