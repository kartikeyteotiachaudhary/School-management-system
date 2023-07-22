import os
import platform
import mysql.connector
    
##creating database connectivity
#passwd = str(input("ENTER THE DATABASE PASSWORD: "))

#Create the connection object.
db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')

#printing the connection object.
print(db)

#creating the cursor object.
cursor = db.cursor()
print(db)
#cursor = connection.cursor()


#creating database
cursor.execute("create database if not exists kartikey")
cursor.execute("use kartikey")

#creating the tables we need
cursor.execute("create table if not exists Class(Class int(3) Primary Key, Sec char(1) Not Null, Total int(2) Not Null, Boys int(2) Not Null, Girls int(2) Not Null, Class_Teacher varchar(20) Not Null)")
cursor.execute("create table if not exists Emp(Empno int(11) Primary Key, Ename varchar(20) Not Null, Job varchar(20) NOT NULL, Hire_Date date Not Null)")
cursor.execute("create table if not exists Exam(Sname varchar(20) Not Null, Admno int(11) Primary Key, Percentage decimal(4,2) Not Null, Result varchar(10) Not Null)")
cursor.execute("create table if not exists Fee(Admno int(11) Primary Key, Fee varchar(11) Not Null, Month varchar(15) Not Null)")
cursor.execute("create table if not exists List(Sno int(3) Not Null, Holiday varchar(20) Not Null, Date date Not Null, Day varchar(10) Not Null)")
cursor.execute("create table if not exists Student(Sname varchar(30) Not Null, Admno int(11) Primary Key, Dob date Not Null,Class char(3) Not Null, City varchar(20) Not Null)")

#login or signup option
#creating table for storing the username and password of the user
cursor.execute("create table if not exists User_Data(Username varchar(30) Primary Key,password varchar(30) default'000')")
    
def main():
    global bye #Making Bye As Super Global Variable
    global ch,c
    bye = "===> Brought To You By Kartikey Teotia <==="
    db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
    cursor = db.cursor()
 
    main_menu()
    ch = int(input("\nEnter Your Choice(1-5): "))
    if ch == 1: 
        Student_menu()
    elif ch == 2:
        print('\t-----------------------------------\n\tWELCOME TO SCHOOL MANAGEMENT SYSTEM\n')
        print('\t    DEVELOPED BY KARTIKEY TEOTIA\n\t-----------------------------------\n')
        print('a. NEW EMPLOYEE')
        print('b. UPDATE STAFF DETAILS')
        print('c. DELETE EMPLOYEE')
        c=input("\nEnter Your Choice: ")
        if c == 'a':
            insert2()
            print('\nUpdated Details are...\n')
            display2()
        elif c == 'b':
            update2()
            print('\nModified Details are...\n')
            display2()
        elif c == 'c':
            delete2()
            print('\nModified Details are...\n')
            display2()
        else:
            print('\nEnter Correct Choice...!!')
            c = input("\nEnter Your Choice(a-e): ")
    elif ch == 3:
        print('\t-----------------------------------\n\tWELCOME TO SCHOOL MANAGEMENT SYSTEM\n')
        print('\t    DEVELOPED BY KARTIKEY TEOTIA\n\t-----------------------------------\n')
        print('a.NEW Fee')
        print('b.UPDATE Fee')
        print('c.EXEMPT Fee')
        c = input("\nEnter your Choice: ")
        if c == 'a':
            insert3()
        elif c == 'b':
            update3()
        elif c == 'c':
            delete3()
        else:
            print('\nEnter Correct Choice...!!')
    elif ch == 4:
        print('\t-----------------------------------\n\tWELCOME TO SCHOOL MANAGEMENT SYSTEM\n')
        print('\t    DEVELOPED BY KARTIKEY TEOTIA\n\t-----------------------------------\n')
        print('a. EXAM DETAILS')
        print('b. UPDATE DETAILS')
        print('c. DELETE DETAILS')
        c = input("\nEnter Your Choice: ")
        if c == 'a':
            insert4()
        elif c == 'b':
            update4()
        elif c == 'c':
            delete4()
        else:
            print('\nEnter Correct Choice...!!')
    elif ch == 5:
        print("\n\t*****This Software is Created By Kartikey Teotia; Class XII*****")
        wait = input("\nPress 'y' To Exit...")
        quit(bye)
    else:
        print('\nEnter Correct Choice...!!')
        main()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def insert1():
    Sname = input('\nEnter Student Name: ')
    Admno = int(input('Enter Admission Number: '))
    Dob = input('Enter Date of Birth(yyyy/mm/dd): ')
    Class = input('Enter Class Name: ')
    City = input('Enter City Name: ')
    db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
    cursor = db.cursor()
    sql = "INSERT INTO Student(Sname,Admno,Dob,Class,City) VALUES ('%s' ,'%d','%s','%s','%s')" % (Sname,Admno,Dob,Class, City)

#-----------------try-------------------------
    cursor.execute(sql)
    db.commit()
        
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display1():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Student" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            Sname = c[0]
            Admno = c[1]
            Dob = c[2]
            Class = c[3]
            City = c[4]
            print ("(Sname = %s,\tAdmno = %d,\tDob = %s,\tClass = %s,\tCity = %s)\n" % (Sname,Admno,Dob,Class,City))
    except:
        print ("\nError:Unable To Fetch Data")
        db.close()

def update1():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            Sname = c[0]
            Admno = c[1]
            Dob = c[2]
            Class = c[3]
            City = c[4]
            print ("(Sname = %s,\tAdmno = %d,\tDob = %s,\tClass = %s,\tCity = %s)\n" % (Sname,Admno,Dob,Class,City))
    except:
        print("Error:Unable To Fetch Data")
    try:
        print("\n")
        tEmpst = int(input("Enter Admission No: "))    
        tEmp = input("Enter New Class: ")
        sql = "UPDATE Student SET Class = '%s' WHERE Admno = %s" % (tEmp, tEmpst)
        cursor.execute("UPDATE Student SET Class = {} WHERE Admno = {}".format(tEmp, tEmpst))
        cursor.execute(sql)
        db.commit()
        print("\nRows affected: ",cursor.rowcount)
        db.close()
    except Exception as e:
        print(e)
        db.close()

def delete1():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Student" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            Sname = c[0]
            Admno = c[1]
            Dob = c[2]
            Class = c[3]
            City = c[4]
            print ("(Sname = %s,\tAdmno = %d,\tDob = %s,\tClass = %s,\tCity = %s)\n" % (Sname,Admno,Dob,Class,City))
    except:
            print("Error:Unable To Fetch Data")
    try:
            tEmp = int(input("\nEnter The Admno to be deleted: "))
            sql = "DELETE FROM Student WHERE Admno = '%d'" % (tEmp)
            ans = input("\nAre you sure you want to delete the record(y/n): ")
            if ans == 'y' or ans == 'Y':
                cursor.execute(sql, tEmp)
                db.commit()
                print("\nRows affected: ",cursor.rowcount)
                db.close()
    except Exception as e:
            print(e)
            db.close()

def insert2():
    ename=input("Enter Employee Name : ")
    Empno=int(input("Enter Employee No : "))
    job=input("Enter Designation: ")
    hiredate=input("Enter date of joining: ")
    db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
    cursor = db.cursor()
    sql="INSERT INTO Emp(ename,Empno,job,hiredate) VALUES ( '%s' ,'%d','%s','%s')"%(ename,Empno,job,hiredate)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display2():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Emp" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[0]
            Empno = c[1]
            job = c[2]
            hiredate = c[3]  
            print ("(Empno=%d,ename=%s,job=%s,hiredate=%s)" % (Empno,ename,job,hiredate))
    except:
        print("Error:Unable To Fetch Data")
        db.close()

def update2():
    try:
        db = kartikey.connector.connect(user='kunnu', passwd='kunnu', host='localhost',database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Emp" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[0]
            Empno = c[1]
            job = c[2]
            hiredate = c[3]     
    except:
        print("Error:Unable To Fetch Data")
        print()
        tEmpst=int(input("Enter Employee No : "))    
        tEmp=input("Enter new designation  : ")
    try:
        sql = "Update Emp set job=%s where Empno='%d'" % (tEmp,tEmpst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete2():
    try:
        db = kartikey.connector.connect(user='kunnu', passwd='kunnu', host='localhost',database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Emp" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            ename = c[0]
            Empno = c[1]
            job = c[2]
            hiredate = c[3]  
    except:
        print("Error:Unable To Fetch Data")
        tEmp=int(input("\nEnter Emp no to be deleted : "))
    try:
        sql = "delete from Emp where Empno='%d'" % (tEmp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()

def insert3():
    Admno=int(input("Enter adm no: "))
    Fee=float(input("Enter Fee amount : "))
    month=input("Enter Month: ")
    db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
    cursor = db.cursor()
    sql="INSERT INTO Fee(Admno,Fee,month) VALUES ( '%d','%d','%s')"%(Admno,Fee,month)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display3():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Fee" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            Admno = c[0]
            Fee = c[1]
            month = c[2]
            print ("(Admno=%d,Fee=%s,month=%s)" % (Admno,Fee,month))
    except:
        print("Error:Unable To Fetch Data")
        db.close()

def update3():
        try:
            db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
            cursor = db.cursor()
            sql = "SELECT * FROM Fee" 
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                Admno = c[0]
                Fee = c[1]
                month = c[2]
        except:
            print("Error:Unable To Fetch Data")
            print()
            tEmpst=int(input("Enter Admission No: "))    
            tEmp=input("Enter new class: ")
        try:
            sql = "Update Fee set month=%s where Admno='%d'" % (tEmp,tEmpst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print (e)
            db.close()

def delete3():
        try:
            db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
            cursor = db.cursor()
            sql = "SELECT * FROM Fee" 
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                Admno = c[0]
                Fee = c[1]
                month = c[2]
        except:
            print("Error:Unable To Fetch Data")
            tEmp=int(input("\nEnter adm no to be deleted : "))
        try:
            sql = "delete from Student where Admno='%d'" % (tEmp)
            ans=input("Are you sure you want to delete the record(y/n) : ")
            if ans=='y' or ans=='Y':
                cursor.execute(sql)
                db.commit()
        except Exception as e:
            print(e)
            db.close()

def insert4():
        Sname=input("Enter Student Name: ")
        Admno=int(input("Enter Admission No: "))
        per=float(input("Enter percentage: "))
        res=input("Enter result: ")
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql="INSERT INTO Exam(Sname,Admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(Sname,Admno,per,res) 
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()

def display4():
        try:
            db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
            cursor = db.cursor()
            sql = "SELECT * FROM Exam" 
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                Sname = c[0]
                Admno = c[1]
                Dob = c[2]
                Class = c[3]
                City = c[4]
                print ("(Sname,Admno,per,res)"%(Sname,Admno,per,res) )
        except:
            print("Error:Unable To Fetch Data")
            db.close()

def update4():
        try:
            db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
            cursor = db.cursor()
            sql = "SELECT * FROM Exam" 
            cursor.execute(sql)
            results = cursor.fetchall()
            for c in results:
                Sname = c[0]
                Admno = c[1]
                Dob = c[2]
                Class = c[3]
                City = c[4]       
        except:
            print("Error:Unable To Fetch Data")
            print()
            tEmpst=int(input("Enter Admission No: "))    
            tEmp=input("Enter new result: ")
        try:
            sql = "Update Student set res=%s where Admno='%d'" % (tEmp,tEmpst)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.close()

def delete4():
    try:
        db = mysql.connector.connect(host = 'localhost',user = 'kunnu',passwd = 'kunnu', database='kartikey')
        cursor = db.cursor()
        sql = "SELECT * FROM Exam" 
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            Sname = c[0]
            Admno = c[1]
            Dob = c[2]
            Class = c[3]
            City = c[4]
    except:
        print("Error:Unable To Fetch Data")
        tEmp=int(input("\nEnter adm no to be deleted: "))
    try:
        sql = "delete from Exam where Admno='%d'" % (tEmp)
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print(e)
        db.close()

def main_menu():
    print('\t-----------------------------------\n\tWELCOME TO SCHOOL MANAGEMENT SYSTEM\n')
    print('\t    DEVELOPED BY KARTIKEY TEOTIA\n\t-----------------------------------\n')
    print("\t1. STUDENT MANAGEMENT")
    print("\t2. EMPLOYEE MANAGEMENT")
    print("\t3. FEE MANAGEMENT")
    print("\t4. EXAM MANAGEMENT")
    print("\t5. EXIT")

def Student_menu():
    print('\t-----------------------------------\n\tWELCOME TO SCHOOL MANAGEMENT SYSTEM\n')
    print('\t    DEVELOPED BY KARTIKEY TEOTIA\n\t-----------------------------------\n')
    print('\ta. NEW ADMISSION')
    print('\tb. SHOW STUDENTS DETAILS')
    print('\tc. UPDATE STUDENT DETAILS')
    print('\td. ISSUE TC')
    print("\te. EXIT")
    c = input("\nEnter Your Choice(a-e): ")
    if c == 'a':
        insert1()
        print('\nUpdated Students Details are...\n')
        display1()
    elif c == 'b':
        print('\nStudents Details are...\n')
        display1()
    elif c == 'c':
        update1()
        print('\nModified Details are...\n')
        display1()
    elif c == 'd':
        delete1()
        print('\nModified Details are...\n')
        display1()
    elif c == 'e':
        print("\n\t*****This Software is Created By Kartikey Teotia; Class XII*****")
        wait = input("\nPress 'y' To Exit...")
        quit(bye)
    else:
        print('\nEnter Correct Choice...!!')
        Student_menu()

def runAgain(): #Making Runable Program
    runAgn = input("\nWant To Run Again(Y/N): ")
    if(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
            print(os.system('cls'))
            main()
            runAgain()
        else:
            print(os.system('clear'))
            main()
            runAgain()
    else:
        print("\n\t*****This Software is Created By Kartikey Teotia; Class XII*****")
        wait = input("\nPress 'y' To Exit...")
        quit(bye) #Print GoodBye Message And Exit The Program
main()
runAgain()
