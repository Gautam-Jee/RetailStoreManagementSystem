from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1375x750+0+0")
        root.iconbitmap("img\Flaticonmaker-Flat-Style-Shopping-bag.ico")
        self.root.title(
            "Retail Store Managementre  System | Developed By Gautam , Nishant , Nitin , Prashant , Session-2020-2022")
        self.root.config(bg="white")

        # ----title-----
        self.icon_title = PhotoImage(file="img\logo1.png")
        title = Label(self.root, text="Retail Store Managementre  System ", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, "bold"), bg="navy blue", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # ------btn_logout-------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2").place(x=1200, y=15, height=40, width=150)
        #---clock-----
        self.lbl_clock = Label(self.root, text="Welcome to Retail Store System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",  font=(
            "times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #----Left Menu-------
        self.MenuLogo=Image.open("img\menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102, width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side = PhotoImage(file="img\side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        #-----content-----
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)






        #---footer-----
        self.lbl_footer = Label(self.root, text="Retail Store Management system | Developed By Gautam ,Nishant , Nitin , Prashant\n MCA BATCH 2020-2022\n For any Technical Issue Contact Us:gautamxxxx@gmail.com",  font=("times new roman", 12), bg="#4d636d", fg="white")
        self.lbl_footer.pack(side=BOTTOM,fill=X)

    #==========================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)




if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()


