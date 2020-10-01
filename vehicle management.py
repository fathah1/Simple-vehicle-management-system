
import os
import platform
import mysql.connector
def selection():
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    print('-----------------------------------\nVEHICLE MANAGEMENT SYSTEM\n-----------------------------------')
    print("1.VEHICLE MANAGMENT")
    print("2.OWNERSHIP MANAGEMENT")
    print("3.REGISTRATION MANAGEMENT")
    print("4.exit")

    ch=int(input("\nEnter ur choice (1-3) : ")) 
    if ch==1:
        print('\nVEHICLE MANAGEMENT SYSTEM\n')
        print('a.NEWLY REGISTERING')
        print('b.UPDATE CURRENT VEHICLE DETAILS')
        print('c.DELETE')
        print('d.SEARCH A VEHICLE')  
        c = input("Enter ur choice (a-d) : ")
        if c=='a':
            insert1()
        elif c=='b':
            update1()
            print('\nModified Details Are..\n')
        elif c=='c' :
            delete1()
            print('\nModified Details Are..\n')
            display1()
        elif c=='d':
            print('\nCurrent Details Are..\n')
            display1()
        else:
            print('Enter correct choice...!!')
    elif ch==2:
        print('OWNER MANAGEMENT SYSTEM')
        print('a.NEW OWNER')
        print('b.UPDATE OWNER DETAILS')
        print('c.DELETE OWNER')
        print('d.SHOW OWNER DETAILS')
        c=input("Enter ur choice : ")
        if c=='a':
            insert2()
            print('\nModified Details Are..\n')
            display2()
        elif c=='b':
            update2()
            print('\nModified Details Are..\n')
            display2()
        elif c=='c':
            delete2()
            print('\nModified Details Are..\n')
            display2()
        elif c=='d':
            print('\nCurrent Details Are..')
            display2()
        else:
            print('Enter Correct Choice...!!') 
    elif ch==3:
        print('REGISTRATION MANAGEMENT SYSTEM')
        print('a.NEW FEE')
        print('b.UPDATE FEE')
        print('c.DELETE FEE')
        print('d.SHOW FEE TABLE')
        c=input("Enter ur choice : ")
        if c=='a':
            insert3()
        elif c=='b':
            update3()
        elif c=='c':
            delete3()
        elif c=='d':
            print('\nCurrent Details Are..')
            display3()
        else:
            print('Enter correct choice...!!')
            selection()
def insert1():
    regno=int(input("Enter reg no : "))
    regdate=input("Enter reg date (yyyy-mm-dd): ")
    Type=input("Enter type of vehicle")
    manufacturer=input("Enter Manufacturer")
    model=input("Enter Model")
    color = input("Enter Colour")
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor() 
    sql="INSERT INTO vehicle_detail(regno,regdate,Type,manufacturer,model,color) VALUES ( '%d' ,'%s','%s','%s','%s','%s')"%(regno,regdate,Type,manufacturer,model,color)
    cursor.execute(sql)
    db.commit()
    selection()
  
def display1():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql= "SELECT * FROM vehicle_detail"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno = c[0]
            regdate= c[1]
            Type=c[2]
            manufacturer=c[3]
            model=c[4]
            color =c[5]
            print ("(regno=%d,regdate=%s,Type=%s,manufacturer=%s,model=%s,color=%s)"%(regno,regdate,Type,manufacturer,model,color))
        selection()
    except:
        print ("Error: unable to fetch data")
        db.close()
def update1():
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql = "SELECT * FROM vehicle_detail"
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        regno = c[0]
        regdate= c[1]
        Type=c[2]
        manufacturer=c[3]
        model=c[4]
        color =c[5]

    tempst=int(input("Enter reg No : "))
    temp=input("Enter new manufacturer  : ")
    temp1=input("enter new type: ")
    temp2=input("enter new model: ")
    temp3=input("enter new reg date: ")
    temp4=input("enter new color: ")
    sql5 = "Update vehicle_detail set manufacturer=%s where regno= %s "%(temp,tempst)
    sql1= "Update vehicle_detail set Type='s' where regno= %s "%(temp1,tempst)
    sql2= "Update vehicle_detail set model='s' where regno= %s " %(temp2,tempst)
    sql3="Update vehicle_detail set regdate='s' where regno= %s "%(temp3,tempst)
    sql4="Update vehicle_detail set color='s' where regno= %s "%(temp4,tempst)
    cursor.execute(sql)
    db.commit() 
    db.close() 
   
def delete1():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql = "SELECT * FROM vehicle_detail"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno = c[0]
            regdate= c[1]
            Type=c[2]
            manufacturer=c[3]
            model=c[4]
            color=c[5]

    except:
        print ("Error: unable to fetch data")


    temp=int(input("\nEnter regno to be deleted : "))
    try:
        sql = "delete from vehicle_detail where regno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()
def insert2():
    regno=int(input("Enter registration no : "))
    owner=input("Enter owners name : ")
    address=input("Enter address: ")
    bank_name=input("Enter the name of bank: ")
    mobile_no=int(input("Enter the number: "))
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql="INSERT INTO owner_detail(regno,owner,address,bank_name,mobile_no) VALUES ( '%d' ,'%s','%s','%s',%d)"%(regno,owner,address,bank_name,mobile_no)
    try:
        cursor.execute(sql)
        db.commit()
        selection()
    except:
        db.rollback()
        db.close() 
def display2():
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql = "SELECT * FROM owner_detail"
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        regno = c[0]
        owner= c[1] 
        address=c[2]
        bank_name=c[3]
        mobile_no=[4]
        print ("(regno=%s,owner=%s,address=%s,bank_name=%s,mobile_no=%s)"%(regno,owner,address,bank_name,mobile_no))
    selection()
def update2():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql = "SELECT * FROM owner_detail"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno = c[0]
            owner= c[1]
            address=c[2]
            bank_name=c[3]
            mobile_no=[4]
    except:
        print ("Error: unable to fetch data")
        print()
    tempst=int(input("Enter regno : "))
    temp=input("Enter new bank_name  : ")
    temp1=input("Enter new owner name  : ")
    temp2=input("Enter new address  : ")
    temp3=input("Enter new no  : ")
    
    try:
        sql = "Update owner_detail set bank_name='%s' where regno='%d'" % (temp,tempst)
        sql1 = "Update owner_detail set owner='%s' where regno='%d'" % (temp1,tempst)
        sql2 = "Update owner_detail set address='%s' where regno='%d'" % (temp2,tempst)
        sql3 = "Update owner_detail set mobile_no='%s' where regno='%d'" % (temp3,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        db.close()
def delete2():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql = "SELECT * FROM owner_detail"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno = c[0]
            owner= c[1]
            address=c[2]
            namae=c[3]
            mobile_no=c[4]
             
    except:
        print ("Error: unable to fetch data")
    temp=int(input("\nEnter registration no to be deleted : "))
    try:
        sql = "delete from owner_detail where regno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()
def insert3():
    regno=int(input("Enter reg no: "))
    model=str(input("Enter model name: "))
    price=float(input("Enter price: "))
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql="INSERT INTO registration_details(regno,model,price) VALUES ( '%d','%s','%d')"%(regno,model,price)
    try:
        cursor.execute(sql)
        db.commit()
        selection()
    except:
        db.rollback()
        db.close()
def display3():
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql = "SELECT * FROM registration_details"
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
        regno= c[0]
        model=c[1]
        price=c[2]
        print ("(regno=%s,model=%s,price=%s)"%(regno,model,price)) 
    selection()
def update3():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql = "SELECT * FROM registration_details"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno= c[0]
            model=c[1]
            price=c[2]
            
    
        tempst=int(input("Enter regno No : "))
        temp=input("Enter new fee : ")
        sql = "Update registration_details set price=%s where regno='%d'" % (temp,tempst)
        cursor.execute(sql) 
        db.commit()
        selection()
    except Exception as e:
        print (e)
        db.close() 
def delete3():
    try:
        db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
        cursor = db.cursor()
        sql = "SELECT * FROM registration_details"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            regno= c[0]
            model=c[1]
            price=c[2]
            
        temp=int(input("\nEnter reg no to be deleted : "))
        sql = "delete from registration_details where regno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
        selection()
    except Exception as e:
        print (e)
        db.close()
def search():
    db = mysql.connector.connect(user='root', password='12com.sci', host='localhost',database='vehicle_management')
    cursor = db.cursor()
    sql = "SELECT * FROM vehicle_details"
    cursor.execute(sql)
    selection()
    
selection()

