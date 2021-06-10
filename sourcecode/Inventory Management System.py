import pymysql as py
con=py.connect("localhost","root","","IMS")
cur=con.cursor()


def manage_stock():
    print("\n1. update product quantity in stock\n2. view stock")
    ch=int(input("\n enter your choice : "))
    if(ch==1):
        update_product_quantity_in_stock()
    elif(ch==2):
        view_stock()
def sale():
    print("\n1. insert product sale detail\n2. updata product sale detail\n3. view product sale detail\n4. remove product sale detail")
    chh=int(input("\n enter your choice : "))
    if(chh==1):
        insert_product_sale_detail()
    elif(chh==2):
         update_product_sale_detail()
    elif(chh==3):
         view_product_sale_detail()
    elif(chh==4):
        remove_product_sale_detail()
def manage_product():
    print("\n1. add new product\n2. view all products\n3. remove product")
    chhh=int(input("\n enter your choice : "))
    if(chhh==1):
        add_new_product()
    elif(chhh==2):
        view_all_products()
    elif(chhh==3):
        remove_product()

def update_product_quantity_in_stock():
    product_name=input("which product do you want update : ")
    product_qty=int(input("enter the quantity : "))
    q="update product set product_qty=%d where product_name='%s'"%(product_qty,product_name)
    cur.execute(q)
    print("\n thank you your product are update successfully")
    con.commit()

def view_stock():
    q="select * from product"
    cur.execute(q)
    res=cur.fetchall()
    print("................STOCK AVAILABLE DETAILS...............")
    print(" \n"  "product_id  ""|""  product_name  ""|"" purchase_price  ""|""  sale_price ""|""  product_qty  ") 
    print("---------------------------------------------------------------------------------------")
    for i in res:
        
        print("(",i[0],"     ""|"" ",i[1],"       ""|""  ",i[2],"  ""|""      ",i[3],"      ""|"" ",i[4],"    ""|""    )")

 


def insert_product_sale_detail():

    
    sale_id=int(input(" enter unique sale id : "))
    product_id=int(input(" enter the product id : "))
    price=int(input(" enter the price : "))
    date=input(" enter the date : ")

    sale_qty=int(input(" enter the sale qnty"))
    q="insert into sale values(%d,%d,%d,%d,'%s')"%(sale_id,product_id,price,sale_qty,date)
    cur.execute(q)
    print("thank you your product are insert")
    con.commit()

def update_product_sale_detail():
    sale_id=int(input(" on which sale_id do you want update : "))
    sale_qty=int(input(" enter the quantity for update : "))
    q="update sale set sale_qty=%d where sale_id=%d"%(sale_qty,sale_id)
    cur.execute(q)
    print("\n thank you ! your sale quantity are update successfully")
    con.commit()
    
def view_product_sale_detail():
    q="select * from sale"
    cur.execute(q)
    res=cur.fetchall()
    print("................PRODUCT SALE DETAILS...............")
    print(" \n sale_id   ""|"" product_id      ""|"" price  ""|"" sale_qnty    ""|"" date  ") 
    print("--------------------------------------------------------------------------")
    for i in res:
        
        print("(",i[0],"     ""|"" ",i[1],"       ""|""  ",i[2],"     ""|""  ",i[3],"    ""|"" ",i[4]," )")



def remove_product_sale_detail():
    sale_id=int(input("enter your sale_id"))
    q="delete from sale where sale_id=%d"%(sale_id)
    cur.execute(q)
    print(" Delete....",cur.rowcount)
    print(" Record successfully delete of sale_id",sale_id)

    
def add_new_product():
     
     
    product_id=int(input("enter your product id : "))
    product_name=input("enter your product name : ")
    purchase_price=int(input("enter your purchase price : "))
    sale_price=int(input("enter your sale price : "))
    product_qty=int(input("enter your product qnty : "))
    q="insert into product values('%d','%s',%d,%d,%d)"%(product_id,product_name,purchase_price,sale_price,product_qty)
    cur.execute(q)
    print(" thank you your product are add")
    con.commit()  
def view_all_products():
    q="select * from product"
    cur.execute(q)
    res=cur.fetchall()
    print("................ALL PRODUCT DETAILS...............")
    print(" \n  product_id  ""|""  product_name   ""|"" purchase_price  ""|""  sale_price ""|""  product_qnty  ") 
    print("---------------------------------------------------------------------------------------")
    for i in res:
        
        print("(",i[0],"     ""|"" ",i[1],"       ""|""  ",i[2],"  ""|""      ",i[3],"      ""|"" ",i[4],"  )")


def remove_product():
    product_id=int(input("enter your product id"))
    q="delete from product where product_id=%d"%(product_id)
    cur.execute(q)
    print("Delete...",cur.rowcount)
    print(" Record successfully delete of product_id ",product_id)
    con.commit()

def view_profit_details():
     import numpy as np
     q="select purchase_price from product"
     cur.execute(q)
     a=cur.fetchall()
     con.commit()
     p="select sale_price from product"
     cur.execute(p)
     b=cur.fetchall()
     x=np.array(a)
     y=np.array(b)
     c=y-x
     summ=0
     h=c.size
     for i in range(0,h):
         summ=summ+c[i]
     print("profit is :" , summ)
     con.commit()
     
    
#def exit():




print("***************......WELCOME IN INVENTORY MANAGEMENT SYASTEM....**********************")
opt='y'
while(opt=='y' or opt=='Y'):
    print("\n1. manage stock\n2. sale\n3. manage product\n4. view profit details\n5. exit")   
    choice=int(input("\n enter your choice what do you want : "))
    if(choice==1):
        manage_stock()
        con.commit()
    elif(choice==2):
        sale()
        con.commit()
    elif(choice==3):
        manage_product()
        con.commit()
    elif(choice==4):
        view_profit_details()
        con.commit()
    elif(choice==5):
        exit()
       
    else:
        print("\nwrong choice please eneter your correct choice")

    opt=input("\ndo you want any other quary or not(y/n) :")
