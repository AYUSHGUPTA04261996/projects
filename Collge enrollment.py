import MySQLdb

try:
        
        def Newstudent():
                cursor=con.cursor()
                Rollno=int(input('Enter Rollno:'))
                name=input('Enter student name:')
                course=input('Enter course name:')
                fees=int(input('Enter amount of fees:'))

                data=[Rollno,name,course,fees]
                q="insert into STUDENT values(%s,%s,%s,%s)"

                r=cursor.execute(q,data)

                if r>0:
                        print("data inserted")

                else:
                        print('error in data insertion')

                con.commit()

        def Rollno():
                cursor=con.cursor()
                Rollno=int(input('Enter Rollno:'))


                r=cursor.execute("SELECT * from STUDENT where Rollno={Rollno}")
                r=cursor.fetchall()

                con.commit()

                for x in r:
                        print(x)

        def name():
                cursor=con.cursor()
                name=input('enter name')

                r=cursor.execute("SELECT * from STUDENT where name={name}")

                r=cursor.fetchall()
                con.commit()


                for x in r:
                        print(x)

        def course():
                cursor=con.cursor()
                course=input('enter course name:')

                r=cursor.execute("SELECT * from STUDENT where course={course}")
                r=cursor.fetchall()
                con.commit()

                for x in r:
                        print(x)

        def showall():
                r=cursor.execute("SELECT * from STUDENT")
                if r>0:
                    print("no of rows",r)

                    rows=cursor.fetchall()

                    for row in rows:
                        print(row[0],row[1],row[2],row[3])
                con.commit()

        def update():
                cursor=con.cursor()
                Rn=int(input('Enter Rollno:'))
                nm=input('Enter student name:')
                crs=input('Enter course name:')
                fs=int(input('Enter amount of fees:'))

                data=[Rollno,name,course,fees]
                q="UPDATE STUDENT set Rollno=%s,name=%s,course=%s,fees=%s, where Rollno={Rn},name={nm},course={crs},fees={fs}"
                r=cursor.execute(q,data)
                if r>0:
                        print('data updated!')
                con.commit()

        def remove():
                cursor=con.cursor()
                Rn=int(input('Enter Rollno:'))
                r=cursor.execute("DELETE from STUDENT where Rollno={Rn}")
                if r>0:
                    print('data deleted')
                con.commit()	
except Exception as e:
        print("error",e)

try:
    con=MySQLdb.connect(host='localhost',database='student',user='root',password='root')
    print("Connected")


    cursor=con.cursor()


            
    n=-1
    while n!=0:
            print('******MENU******')
            print('1.New student:')
            print('2.SEARCH ROll no:')
            print('3.SEARCH name:')
            print('4.SEARCH course name:')
            print('5.Show ALL')
            print('6.Update')
            print('7.Remove')
            print('0.Exit')
            n=int(input('enter option:'))

            if n==0:
                    print("THANKYOU EXIT")
                    break
                    
            if n==1:
                    s=Newstudent()

                    
            elif n==2:
                    s=Rollno()

            elif n==3:
                    s=name()

            elif n==4:
                    s=course()

            elif n==5:
                    s=showall()

            elif n==6:
                    s=update()

            elif n==7:
                    s=remove()

            else:
                    print("invalid entry")
                    
except Exception as e:
    print("error : ",e)
                    




