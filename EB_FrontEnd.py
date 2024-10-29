#FrontEnd

from tkinter import*
import tkinter.messagebox
import EB_BackEnd
class Electricity_Bill:

    def __init__(self,root):
        self.root =root
        self.root.title("Electricity Bill Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="ghost white")

        CustomerID = StringVar()
        CustomerName = StringVar()
        UnitsConsumed = StringVar()
        Amount = StringVar()
        #===============================================================Function======================================================

        def Exit_Option():
            Exit_Option=tkinter.messagebox.askyesno("Electricity Bill Management Systems","Are sure you want to exit ?")
            if Exit_Option > 0:
                root.destroy()
                return

        def ClearEBData():
            self.txtCustomerID.delete(0,END)
            self.txtCustomerName.delete(0,END)
            self.txtUnitsConsumed.delete(0,END)
            self.txtAmount.delete(0,END)

        def CalculateEBData():
            if(len(CustomerID.get()) != 0):
                EB_BackEnd.CalculateEBRecord( CustomerID.get(), CustomerName.get(), UnitsConsumed.get())
                EBlist.delete(0, END)
                EBlist.insert(END, ( CustomerID.get(), CustomerName.get(), UnitsConsumed.get()))   

        def DisplayEBData():
            EBlist.delete(0,END)
            for row in EB_BackEnd.ViewEBData():
                EBlist.insert(END,row,str(""))

        def EBRecord(event):
            global ebd
            searchEB = EBlist.curselection()[0]
            ebd = EBlist.get(searchEB)

            self.txtCustomerID.delete(0,END)
            self.txtCustomerID.insert(END,ebd[1])
            self.txtCustomerName.delete(0,END)
            self.txtCustomerName.insert(END,ebd[2])
            self.txtUnitsConsumed.delete(0,END)
            self.txtUnitsConsumed.insert(END,ebd[3])
            self.txtAmount.delete(0,END)
            self.txtAmount.insert(END,ebd[4])

        def DeleteEBData():
            if(len(CustomerID.get()) != 0):
                EB_BackEnd.DeleteEBRecord(ebd[0])
                ClearEBData()
                DisplayEBData()

        def SearchEBDatabase():
            EBlist.delete(0,END)
            for row in EB_BackEnd.SearchEBData( CustomerID.get(), CustomerName.get()):
                EBlist.insert(END,row,str(""))

      
        #===============================================================Frames========================================================

        MainFrame = Frame(self.root,bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font = ('Edwardian Script ITC',47,'bold'),text=" Electricity BIll Management Systems ",bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",font = ('Edwardian Script ITC',30,'bold'),text="Customer Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White",font = ('Edwardian Script ITC',30,'bold'),text="EB Database\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #===============================================================Labels and Entry Widget=======================================

        self.lblCustomerID = Label(DataFrameLEFT,font=('arial',25,'bold'),text="Customer ID :",padx=2,pady=2,bg="Ghost White")
        self.lblCustomerID.grid(row=0,column=0,sticky=W)
        self.txtCustomerID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=CustomerID,width=39)
        self.txtCustomerID.grid(row=0,column=1)

        self.lblCustomerName = Label(DataFrameLEFT,font=('arial',25,'bold'),text="Customer Name :",padx=2,pady=2,bg="Ghost White")
        self.lblCustomerName.grid(row=1,column=0,sticky=W)
        self.txtCustomerName = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=CustomerName,width=39)
        self.txtCustomerName.grid(row=1,column=1)

        self.lblUnitsConsumed = Label(DataFrameLEFT,font=('arial',25,'bold'),text="Units Consumed :",padx=2,pady=2,bg="Ghost White")
        self.lblUnitsConsumed.grid(row=2,column=0,sticky=W)
        self.txtUnitsConsumed = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=UnitsConsumed,width=39)
        self.txtUnitsConsumed.grid(row=2,column=1)

        self.lblAmount = Label(DataFrameLEFT,font=('arial',25,'bold'),text="Total Amount :",padx=2,pady=2,bg="Ghost White")
        self.lblAmount.grid(row=3,column=0,sticky=W)
        self.txtAmount = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Amount,width=39)
        self.txtAmount.grid(row=3,column=1)

        #===============================================================ListBox and ScrollBar Widget==================================

        scroll_bar = Scrollbar(DataFrameRIGHT)
        scroll_bar.grid(row=0,column=1,sticky='ns')

        EBlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scroll_bar.set)
        EBlist.bind('<<ListboxSelect>>', EBRecord)
        EBlist.grid(row=0,column=0,padx=0)
        scroll_bar.config(command = EBlist.yview)
        
        #===============================================================Button Widget=================================================

        self.ButtonDisplayData = Button(ButtonFrame,text="Calculate",font=('arial',20,'bold'),height=1,width=10,bd=4,command=CalculateEBData)
        self.ButtonDisplayData.grid(row=0,column=0)

        self.ButtonClearData = Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=ClearEBData)
        self.ButtonClearData.grid(row=0,column=1)

        self.ButtonDeleteData = Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteEBData)
        self.ButtonDeleteData.grid(row=0,column=2)

        self.ButtonSearchData = Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=SearchEBDatabase)
        self.ButtonSearchData.grid(row=0,column=3)

        self.ButtonUpdateData = Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayEBData)
        self.ButtonUpdateData.grid(row=0,column=4)

        self.ButtonExitData = Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=Exit_Option)
        self.ButtonExitData.grid(row=0,column=5)
        
if __name__=='__main__':
    root = Tk()
    application = Electricity_Bill(root)
    root.mainloop()

