def dearness(x):
    da=x*0.8
    return da

def house(x):
    hra=x*0.1
    return hra

def gross(x,y,z):
    grosspay=x+y+z
    return grosspay

def pfund(x):
    pf=x*0.1
    return pf

def netd(x,y):
    netded=x+y
    return netded

def taxb(x,y,z):
    taxable=x-y-z
    return taxable

def ann(x,y):
    annual =(x*12)-y
    return annual

def tot_ded(x,y,z):
    totalded=x+y+z
    return totalded

empid=int(input("Enter employee id: "))
name=input("Enter name of employee: ")
dept=input("Enter name of department: ")
basic=int(input("Enter Basic Salary: "))
da=round(dearness(basic),1)
hra=round(house(basic),1)
grosspay=round(gross(basic,da,hra),1)
pf=round(pfund(basic),1)
prof_tax=200.0
netded=round(netd(pf,prof_tax),1)
std_ded=50000.0
taxable=round(taxb(grosspay,pf,prof_tax),1)
annual=round(ann(taxable,std_ded),1)

if annual<=250000:
    tax=0
elif annual>250000 and annual<=500000:
    tax=(annual-250000)*0.05
elif annual>500000 and annual<=1000000:
    tax=((500000-250000)*0.05)+((annual-500000)*0.2)
else:
    tax=((500000-250000)*0.05)+((1000000-500000)*0.2)+((annual-1000000)*0.3)
    
totalded=round(tot_ded(pf,prof_tax,tax/12),1)
monthly_inc=round(taxable-(tax/12),1)
net_inc=round(monthly_inc*12,1)

while True:
    print("\n")
    print("Menu Driven Program")
    print("1. Earnings")
    print("2. Deductions")
    print("3. Full Payslip")
    print("4. Exit")
    choice=int(input("Enter your choices: "))

    if choice==1:
        print("\n")
        print("XYZ COMPANY LTD")
        print("\n")
        print("---DECEMBER 2020---")
        print("\n")
        print(" NAME OF EMPLOYEE : ",name)
        print(" DEPARTMENT : ",dept)
        print("\n")
        print("---EARNINGS---")
        print(" BASIC SALARY : ",basic)
        print(" DEARNESS ALLOW. : ",da)
        print(" HOUSE RENT ALLOW. : ",hra)
        print("\n")
        print("----TOTAL-----")
        print(" TOTAL EARNING : ",grosspay)
        

    elif choice==2:
        print("\n")
        print("XYZ COMPANY LTD")
        print("\n")
        print("---DECEMBER 2020---")
        print("\n")
        print(" NAME OF EMPLOYEE : ",name)
        print(" DEPARTMENT : ",dept)
        print("\n")
        print("---DEDUCTIONS---")
        print(" PROVIDENT FUND : ",pf)
        print(" PROFESSIONAL TAX : ",prof_tax,)
        print(" INCOME TAX : ",round(tax/12,1))
        print("\n")
        print("----TOTAL-----")
        print(" TOTAL DEDUCTION : ",totalded)
        

    elif choice==3:
        print("\n")
        print("XYZ COMPANY LTD")
        print("\n")
        print("------PAYSLIP------")
        print("---DECEMBER 2020---")
        print("\n")
        print(" NAME OF EMPLOYEE : ",name)
        print(" DEPARTMENT : ",dept)
        print("\n")
        print("---EARNINGS---",end="                   ")
        print("---DEDUCTIONS---")
        print(" BASIC SALARY : ",basic,sep="      ",end="     ")
        print(" PROVIDENT FUND : ",pf,sep="   ")
        print(" DEARNESS ALLOW. : ",da,sep="   ",end="   ")
        print(" PROFESSIONAL TAX : ",prof_tax,)
        print(" HOUSE RENT ALLOW. : ",hra,end="    ")
        print(" INCOME TAX : ",round(tax/12,1),sep="       ")
        print("\n")
        print("----TOTAL-----")
        print(" TOTAL EARNING : ",grosspay,sep="          ")
        print(" TOTAL DEDUCTION : ",totalded,sep="        ")
        print(" MONTHLY TAXABLE INCOME : ",taxable)
        print("\n")
        print("--PROJECTED TAX CALCULATION--")
        print(" GROSS SALARY : ",round(grosspay*12,1),sep="             ")
        print(" GROSS TAXABLE INCOME : ",round(taxable*12,1),sep="     ")
        print(" STANDARD DEDUCTION : ",std_ded,sep="       ")
        print(" INCOME UNDER HEAD SALARY : ",annual)
        print("\n")
        print("----SUMMARY----")
        print(" MONTHLY NET INCOME : ",monthly_inc,sep="")
        print(" ANNUAL NET INCOME : ",net_inc)
        
    elif choice==4:
        print("Program End")
        break
    
    else:
        print("Wrong choice")
