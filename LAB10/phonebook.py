'''
1) I create table with PGadmin(with such words):

create table phonenumbers(
name VARCHAR(18) NOT NULL,
surname VARCHAR(18) NOT NULL,
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

# 2 nd task !!! 
# 1part: inserting data from cansole its "sql" :
# sql = "insert into phonenumbers values ('Yerkhan','Murapov','bee','87085855137'),('Miras','Murapov','bee','87085855137')"
# cursor.execute(sql)
# conn.commit()

# 2part: fom csv file
contact_list = [
   ('name', 'surname', 'simcard', 'number'),
   ['mother','love','bee', '87079773808'],
   ['brother', 'love','bee','87079773808'],
   ['Merey', 'love','bee','87079773808' ],
   ['father','love', 'bee','87079773808' ],
   ['Magzhan','love', 'bee','87079773808' ],
   ['Almat', 'love','bee','87079773808'],
   ['Meirambek', 'love','bee','87079773808']
]

with open('Phonebook.csv','w',newline='') as f:
   writer = csv.writer(f)
   writer.writerows(contact_list)




sql_csv = """COPY phonenumbers(name, surname, simcard, number)
             FROM r\'C:\Users\murap\Desktop\PP2\Phonebook.csv\' 
             DELIMITER \',\' 
             CSV HEADER;
             """
cursor.execute(sql_csv)
conn.commit()

# #3rd task)
# sql2 = "update phonenumbers set name = 'TheBestProggrammer' , number = '87988988998' where simcard = 'bee' and name = 'Yerkhan'"
# cursor.execute(sql2)
# conn.commit()

# # 4TH TASK
# 1st FILTER)
# sql3 = "select * from phonenumbers where simcard = 'bee'"
# cursor.execute(sql3)
# 2 nd FILTER)
# sql3_1 = "select name,surname from phonenumbers where surname = \'Murapov\'"
# cursor.execute(sql3_1)
# nums = cursor.fetchall()
# print(nums)

# 5TH TASK
# nameuser = input()
# sql4 = f'delete from phonenumbers where name = \'{nameuser}\' '
# print(sql4)
# cursor.execute(sql4)
# conn.commit()



cursor.close()
conn.close()
