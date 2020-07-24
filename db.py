import mysql.connector
import re
from pyfiglet import Figlet
from tabulate import tabulate

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123qwe#Bilal',
    database  = 'airport',
    auth_plugin='mysql_native_password'
)
dbCursor = mydb.cursor()

print (Figlet(font='speed').renderText("Airport DBMS"))

print('Welcome to Airport!')

username = input('Enter Username: ')
password = input('Enter Password: ')
if password == 'a' and username=='a':
    print('admin')
    while True:
        print('You can do following things: ')
        print('0. Quit\n1. Add a new Flight Record.\n2. Update details of Flight Record.\n3. Delete Flight Record. ')
        print('4. View all flights landing or taking off for a particular day\n5. View All Tables in Database')

        try:
            option = int(input('Select one option : '))
        except: 
            print('Invalid Option!')
            continue
        if option == 0:
            break
        if option>5 or option <0:
            print('invalid option')
            continue
        if option==1:
            try:
                flight_id = input('Enter Flight ID: ')
                departure_airport = input('Enter departure aiport IATA code : ')
                arrival_airport  = input('Enter arrival aiport IATA code : ')
                departure_time = input('Enter departure time(YYYY-MM-DD HH:MM:SS) : ')
                arrival_time = input('Enter arrival time(YYYY-MM-DD HH:MM:SS) : ')
                airplane = input('Enter  Airplane: ')
                fair = int(input('Enter Fare : '))
            except:
                print('Error: ::: : > Invalid Format')
                continue
            if not (re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',departure_time) or re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}',arrival_time)):
                print('=======Invalid Time format!=====')
                continue
            if len(departure_airport)!=3 or len(arrival_airport)!=3:
                print('======Invalid Iata code!=====') 
                continue
            dbCursor.execute('insert into flight values (%s,%s,%s,%s,%s,%s.%s)',(flight_id,departure_airport,arrival_airport,departure_time,arrival_time, airplane,fair))
            mydb.commit()
        if option==2:
            try:
                previousFlight_id = input('Enter Flight ID: ')
                flight_id = input('Enter updated Flight ID: ')
                departure_airport = input('Enter updated departure aiport IATA code : ')
                arrival_airport  = input('Enter updated arrival aiport IATA code : ')
                departure_time = input('Enter  updated departure time(YYYY-MM-DD HH:MM:SS) : ')
                arrival_time = input('Enter updated arrival time(YYYY-MM-DD HH:MM:SS) : ')
                airplane = input('Enter updated  Airplane: ')
                fair = int(input('Enter updated Fare : '))
            except:
                print('Error: ::: : > Invalid Format')
                continue
            if not (re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',departure_time) or re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}',arrival_time)):
                print('=======Invalid Time format!=====')
                continue
            if len(departure_airport)!=3 or len(arrival_airport)!=3:
                print('======Invalid Iata code!=====') 
                continue
            dbCursor.execute('update flight set flight_id = %s, departure_airport=%s, arrival_airport=%s, departure_time=%s, arrival_time=%s,airplane=%s, fair =%s where flight_id = previousFlight_id',(flight_id,departure_airport,arrival_airport,departure_time,arrival_time, airplane,fair,previousFlight_id))
            mydb.commit()
            if dbCursor.rowcount == 0:
                print('No Such Existing Flight Found')
            else : 
                print('========Updated=======')

        if option == 3:
            flight_id = input('Enter the Flight ID to be cancelled: ')
            dbCursor.execute('delete from flight where flight_id = %s',(flight_id,))
            mydb.commit()
            print('==========Flight Record Deleted==============')
        
        if option==4:
            arrival_airport  = input('Enter arrival aiport IATA code : ')
            day = input('Enter the Day(YYYY-MM-DD): ')
            if len(arrival_airport)!=3:
                print('======Invalid Iata code!=====') 
                continue
            if not ( re.match(r'\d{4}-\d{2}-\d{2}', day)):
                print('Invalid Day!')
                continue
            initTime = day + ' 00:00:00'
            finishTime = day + ' 23:59:59'
            dbCursor.execute('select * from flight where arrival_airport =%s and departure_time>=%s and departure_time<=%s',(arrival_airport, initTime, finishTime))
            result = dbCursor.fetchall()
            if dbCursor.rowcount == 0:
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<< No Such Flight Exists >>>>>>>>>>>>>>>>>>')
            
            for i in result:
                print('Flight ID : '+ str(i[0]) + ' Departure Airport: '+ str(i[1]) + ' Arrival Airport: '+ str(i[2]) + ' Departure Time: '+ str(i[3]) + ' Arrival Time: '+ str(i[4]) + ' Airplane: '+ str(i[5]) + ' Fare: '+ str(i[6]) )
        if option==5:
            dbCursor.execute('Select * from flight')
            resultFlight = dbCursor.fetchall()
            dbCursor.execute('Select * from person_prime')
            resultpersonPrime = dbCursor.fetchall()
            dbCursor.execute('Select * from passengers')
            resultpassengers = dbCursor.fetchall()
            dbCursor.execute('Select * from prime')
            resultprime = dbCursor.fetchall()
            print('==============================Flight =====================')

            print(tabulate(resultFlight, headers=['Flight ID','Departure Airport','Arrival Airport', 'Departure Time', 'Arrival Time', 'Airplane', 'Fare']))
            print('==============================Person Prime =====================')
            print(tabulate(resultpersonPrime, headers=['CNIC','Phone',  'Nationality','Name','Address']))

            print('==============================Passengers =====================')
            print(tabulate(resultpassengers , headers=['Passenger ID', 'CNIC', 'Name']))

            print('==============================Prime =====================')
            print(tabulate(resultprime, headers=['Flight ID', 'Passenger ID', 'Ticket ID']))
elif password == 'r' and username=='r':
    print('receptionist')
    while True:
        print('You can do following things: ')
        print('0.Exit\n1. Add Passenger Record.\n2. Update Passenger Record.\n3. Check Availaible Flights.')
        print('4. Generate Ticket Record.\n5. View The Cheapest Flight.\n6. Find Flight History of Passenger.\n7. Delete Ticket Record. ')
        try:
            option = int(input('Select one option : '))
        except: 
            print('Invalid Option!')
            continue
        if option == 0:
            break
        if option>7 or option <0:
            print('invalid option')
            continue
        if option == 1 : 
            try:
                name = input('Please Enter Username: ')
                cnic = int(input('Please Enter CNIC: '))
                phone = int(input('Please Enter Phone Number: '))
                address = input('Please Enter Address: ')
                nationality = input('Please Enter Nationality: ')
            except: 
                print('Error ::::> Wrong Data Type Entered! ')
                continue  
            phone = '0'+str(phone)                     
            if len(str(phone))!=11:
                print(len(str(phone)))
                print('Error ::::> Unrecogonized Phone Number Format! ')
            if len(str(cnic))!=13 :
                print('Error ::::> Unrecogonized CNIC Format! ')

            
            checkPhoneQ = 'select cnic,pname from person_prime where cnic = %s and pname=%s;'
            dbCursor.execute(checkPhoneQ,(cnic, name))
            phoneNum = dbCursor.fetchall()
            if phoneNum.__len__()>0:
                print('Error ::::> Record Already Exists!')
                continue                
                
            insertionQprime = "insert into person_prime values(%s,%s, %s, %s, %s);"
            dbCursor.execute(insertionQprime,(cnic, phone, nationality,name, address))
            mydb.commit()


            insertionQPass = "insert into passengers(cnic, pname) values( %s, %s);"
            dbCursor.execute(insertionQPass, (cnic,name))
            mydb.commit()

            dbCursor.execute("select passenger_id from passengers where cnic = %s and pname = %s", (cnic,name))
            result = dbCursor.fetchall()
            print('This is the Passenger ID :  ' + str(result[0]))
            
        if option == 2:
            try:
                previousCNIC = int(input('Please Enter Previous CNIC: '))
                previousName = input('Please Enter Previous Name: ') 
                name = input('Please Enter updated Name: ')
                cnic = int(input('Please Enter updated CNIC: '))
                phone = int(input('Please Enter updated Phone Number: '))
                address = input('Please Enter updated Address: ')
                nationality = input('Please Enter updated Nationality: ')
            except: 
                print('Error ::::> Wrong Data Type Entered! ')
                continue  
            phone = '0'+str(phone)                     
            if len(str(phone))!=11:
                print(len(str(phone)))
                print('Error ::::> Unrecogonized Phone Number Format! ')
            if len(str(cnic))!=13 and len(str(previousCNIC))!=13:
                print('Error ::::> Unrecogonized CNIC Format! ')

            insertionQprime = "update person_prime set cnic=%s,phone=%s,pnationality= %s,pname= %s,paddress= %s where cnic=%s and pname=%s;"
            dbCursor.execute(insertionQprime,(cnic, phone, nationality,name, address,previousCNIC,previousName))
            mydb.commit()
            if dbCursor.rowcount == 0:
                print('No Such Record!')
            else:
                print('updated!')
        if option==3:
            dICode = input('Enter Departure Airport IATA code:  ')
            aICode = input('Enter Arrival Airport IATA code:  ')
            startInterval = input('Enter Start time for Search(YYYY/MM/DD HH:MM:SS) in 24-hour format:  ')
            finishInterval = input('Enter finish time for Search(YYYY/MM/DD HH:MM:SS) in 24-hour format:  ')
            if dICode.__len__()!=3 or aICode.__len__()!=3:
                print('Error::::> Wrong IATA code format!')
                continue
            if not (re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',startInterval) or re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}',finishInterval)):
                print('Error:::::> Wrong Format for finish or start time.')
                continue
            
            dbCursor.execute('Select flight_id,departure_time,arrival_time,fair from flight where departure_airport=%s and arrival_airport=%s and departure_time>=%s and arrival_time<=%s;', (dICode,aICode,startInterval,finishInterval))
            result = dbCursor.fetchall()
            print('Following Flights are availaible in the required time: ')
            for i in result:
                print('Flight ID : ' + i[0] + ' | Departure Time : '+str(i[1]) + ' | Arrival Time :' + str(i[2])+' | Fare : ' + str(i[3]))
        if option == 4:
            try:
                name = input('Please Enter Name: ')
                cnic = int(input('Please Enter CNIC: '))  
                flight_id = input('Enter the Flight ID: ')              
            except: 
                print('Error ::::> Wrong Data Type Entered! ')
                continue  
            if len(str(cnic))!=13:
                print('Error ::::> Unrecogonized CNIC Format! ')
            
            dbCursor.execute('Select passenger_id from passengers where cnic=%s and pname =%s', (cnic,name))
            result=dbCursor.fetchall()
            if(dbCursor.rowcount==0):
                print('First Register the passenger.')
                continue
            passID = result[0][0]
            
            dbCursor.execute('Select flight_id from flight where flight_id=%s', (flight_id,))
            result = dbCursor.fetchall()
            if dbCursor.rowcount == 0 :
                print('NO SUCH FLIGHT!')
                continue
            dbCursor.execute('insert  into prime(flight_id,passenger_id) values(%s,%s)',(flight_id, passID))
            mydb.commit()
            print('======Inserted!=====')
        if option == 5:
            dICode = input('Enter Departure Airport IATA code:  ')
            aICode = input('Enter Arrival Airport IATA code:  ')
            if dICode.__len__()!=3 or aICode.__len__()!=3:
                print('Error::::> Wrong IATA code format!')
                continue      
            dbCursor.execute('select min(fair) from flight where departure_airport = %s and arrival_airport = %s', (dICode, aICode))
            result=dbCursor.fetchall()
            minFair = result[0][0]   
            dbCursor.execute('select flight_id,departure_time,arrival_time,fair from flight where departure_airport=%s and arrival_airport=%s and fair=%s;', (dICode,aICode,minFair))
            result = dbCursor.fetchall()
            if dbCursor.rowcount == 0:
                print('No flights form given departure airport to given arrival airport! ')
            for i in result:
                print('Flight ID : ' + i[0] + ' | Departure Time : '+str(i[1]) + ' | Arrival Time :' + str(i[2])+' | Fare : ' + str(i[3]))
        if option == 6:
            try:
                name = input('Please Enter Name: ')
                cnic = int(input('Please Enter CNIC: '))  
            except: 
                print('Error ::::> Wrong Data Type Entered! ')
                continue  
            if len(str(cnic))!=13:
                print('Error ::::> Unrecogonized CNIC Format! ')
            
            dbCursor.execute('Select passenger_id from passengers where cnic=%s and pname =%s', (cnic,name))
            result=dbCursor.fetchall()
            if(dbCursor.rowcount==0):
                print('First Register the passenger.')
                continue
            passID = result[0][0]
            dbCursor.execute('select flight_id from prime where passenger_id = %s;' , (passID,))
            result = dbCursor.fetchall()
            if dbCursor.rowcount==0:
                print('No Flights taken by passenger!')
            print('Following are flights taken by this passenger: ')
            for i in result:
                print(' ==> Flight ID :  ' + i[0])
        if option == 7:
            try:
                name = input('Please Enter Name: ')
                cnic = int(input('Please Enter CNIC: '))  
                flight_id = input('Enter the Flight ID: ')              
            except: 
                print('Error ::::> Wrong Data Type Entered! ')
                continue  
            if len(str(cnic))!=13:
                print('Error ::::> Unrecogonized CNIC Format! ')
            
            dbCursor.execute('Select passenger_id from passengers where cnic=%s and pname =%s', (cnic,name))
            result=dbCursor.fetchall()
            if(dbCursor.rowcount==0):
                print('First Register the passenger.')
                continue
            passID = result[0][0]
            
            dbCursor.execute('Select flight_id from flight where flight_id=%s', (flight_id,))
            result = dbCursor.fetchall()
            if dbCursor.rowcount == 0 :
                print('NO SUCH FLIGHT!')
                continue
            dbCursor.execute('delete from prime where flight_id = %s and passenger_id = %s',(flight_id,passID))
            mydb.commit()
            if dbCursor.rowcount == 0:
                print('No Ticket with the given record was found!')
            else : 
                print(' ===========Deleted===========')
            
else :
    print('not authorized!')