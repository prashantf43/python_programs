from tkinter import Tk,Label,Entry,Button
from tkinter.messagebox import showwarning

root = Tk()
root.title("Employee Salary Sheet")
root.geometry("1200x700")



def empinfo():

    empname=e1.get() #get Employee name
    empsal=e2.get()  #get Employee Salary

    
    
    if(empname and empsal):

        salary=float(empsal)

        da=float(salary*0.25)
        hra=float(salary*0.15)
        pf=float((salary+da)*0.12)
        ta=float(salary*0.075)
        netpay=float(salary+da+hra+ta)
        grosspay=float(netpay-pf)

        if salary <= 250000:
            tax = 0

        elif salary <= 500000:
            tax = (salary - 250000) * 0.05

        elif salary <= 750000:
            tax = (salary - 500000) * 0.10 + 12500 

        elif salary <= 1000000:
            tax = (salary - 750000) * 0.15 + 37500 

        elif salary <= 1250000:
            tax = (salary - 1000000) * 0.20 + 75000 

        elif salary <= 1500000:
            tax = (salary - 1250000) * 0.25 + 125000 

        else:
            tax = (salary - 1500000) * 0.30 + 187500



        #convert float in String for concatinate
        da=str(da)
        hra=str(hra)
        pf=str(pf)
        ta=str(ta)
        netpay=str(netpay)
        grosspay=str(grosspay)
        tax = str(tax)

        #appent date to file (file is append mode)
        file = open('employee.txt','a')
        file.write("\n"+empname+"\t"+empsal+"rs\t"+da+"rs\t"+hra+"rs\t"+pf+"rs\t"+ta+"rs\t"+netpay+"rs\t"+grosspay+"rs\t"+tax+"rs")
        file.close()
    else:
        showwarning("Warning!","Please fill the field")

def showemp():

    #read data from file (file is read mode)
    file = open('employee.txt','r')
    file_data = file.read()

    #get a line from file
    file_line = file_data.split("\n")
    c,r=0,7
    
    Label(root,text="Employee Name",fg="royalblue",font=("Arial",12)).grid(row=6,column=0,padx=5)
    Label(root,text="Basic Pay",fg="royalblue",font=("Arial",12)).grid(row=6,column=1,padx=5)
    Label(root,text="DA",fg="royalblue",font=("Arial",12)).grid(row=6,column=2,padx=5)
    Label(root,text="HRA",fg="royalblue",font=("Arial",12)).grid(row=6,column=3,padx=5)
    Label(root,text="PF",fg="royalblue",font=("Arial",12)).grid(row=6,column=4,padx=5)
    Label(root,text="TA",fg="royalblue",font=("Arial",12)).grid(row=6,column=5,padx=5)
    Label(root,text="Net Salary",fg="royalblue",font=("Arial",12)).grid(row=6,column=6,padx=5)
    Label(root,text="Gross Salary",fg="royalblue",font=("Arial",12)).grid(row=6,column=7,padx=5)
    Label(root,text="TAX",fg="royalblue",font=("Arial",12)).grid(row=6,column=8,padx=5)

    #geting words from line in file
    for line in file_line:
        word = line.split("\t")
        r+=1
        c=0
        for i in word:
            Label(root,text=i,font=("Arial",12)).grid(row=r,column=c,padx=5)
            c+=1
    file.close()
    
 
Label(root, text="Employee Name : ",font=("Arial",12),fg="blue").grid(row=0,column=0)
Label(root, text="Basic Pay : ",font=("Arial",12),fg="blue").grid(row=1,column=0)


e1 = Entry(root,font=("Arial",12))
e1.grid(row=0,column=1)
 
e2 = Entry(root,font=("Arial",12))
e2.grid(row=1,column=1)

#this label for gap
Label(root).grid(row=2)
Label(root).grid(row=4)
Label(root).grid(row=5)
 
btn=Button(root, text="Submit",font=("Arial",12),background="royalblue",fg="white", command=empinfo)
btn1=Button(root, text="Show Employee Info",font=("Arial",12),background="royalblue",fg="white", command=showemp)

btn.grid(row=3,column=0)
btn1.grid(row=3,column=1)
 
root.mainloop()