'''
1) I create table with PGadmin(with such words):

create table phonenumbers(
name VARCHAR(18) NOT NULL,
surname VARCHAR(18) ,
simcard VARCHAR(10),
number VARCHAR(11) NOT NULL
);

'''

import psycopg2,csv


conn = psycopg2.connect(

            host='localhost',
            database='phonebook',
            user='postgres',
            password='yerkhan2003',
)

cursor = conn.cursor()

print("HELLO! WHAT DO YOU WANT \n   2.1 or 2.2 or 3 or 4 or 5")
mode = input()
# 1part: inserting data from cansole its "sql" :
if mode == '2.1':
    print("please enter your name ,surname,simcard,number")
    name_ = input()
    surname_ = input()
    simcard_ = input()
    number_ = input()
    sql = f"insert into phonenumbers values ('{name_}','{surname_}','{simcard_}','{number_}') "
    cursor.execute(sql)
    conn.commit()
if mode == '2.2':
    #2part: fom csv file
    #create csv file
    contact_list = [
    ['mother','love','bee', '87079773808'],
    ['brother', 'love','bee','87079773808'],
    ['Mery', 'love','bee','87079773808' ],
    ['father','love', 'bee','87079773808' ],
    ['Magzhan','love', 'bee','87079773808' ],
    ['Almat', 'love','bee','87079773808'],
    ['Meirambek', 'love','bee','87079773808']
    ]

    with open('Phonebook.csv','w',newline='') as f:
      writer = csv.writer(f)
      writer.writerows(contact_list)

    insert = "INSERT INTO phonenumbers VALUES (%s,%s,%s,%s)"
    with open('Phonebook.csv','r') as f:
        reader = csv.reader(f,delimiter = ',')
        print(reader) # csv reader object adress !!!
        for row in reader:
            print(row)
            cursor.execute(insert, row)
            conn.commit()
        
# sql_csv = " \copy  phonenumbers FROM '/Users/murap/Desktop/PP2/Phonebook.csv' DELIMITER ',' CSV HEADER;"
# cursor.execute(sql_csv)
# conn.commit()

if mode == '3':
    print("please enter name and number and new_number")
    name_ = input()
    number_ = input()
    namenew_ = input()
    sql2 = f"update phonenumbers set name = '{namenew_}' , number = '{number_}' where   name = '{name_}'"
    cursor.execute(sql2)
    conn.commit()


if mode == '4':
    # first filter 
    sql3 = "select * from phonenumbers where simcard = 'bee'"
    cursor.execute(sql3)
    q_ = cursor.fetchall()
    print(q_)

# 2 nd FILTER)
# sql3_1 = "select name,surname from phonenumbers where surname = \'Murapov\'"
# cursor.execute(sql3_1)
# nums = cursor.fetchall()
# print(nums)

if mode == '5':
    nameuser = input()
    sql4 = f'delete from phonenumbers where name = \'{nameuser}\' '
    print(sql4)
    cursor.execute(sql4)
    conn.commit()

cursor.close()
conn.close()
