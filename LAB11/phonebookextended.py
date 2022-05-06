import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="phonebook",
  user="postgres",
  password="yerkhan2003")
cursor = conn.cursor()

print("Hello! What do you want?\n 1 or 2 or 3 or 4 or 5")
mode = input()

if mode == '1':
  # sql = '''
  # create or replace function getAll()
  #   returns table
  #           (
  #               name varchar,
  #               surname varchar,
  #               number  varchar
  #           )
  # as
  # $$
  # begin
  #     return query
  #       select ph.name, ph.surname, ph.number
  #       from phonenumbers  as ph;
  # end
  # $$ language plpgsql
  # '''
  # cursor.execute(sql)
  # conn.commit()
  # execute a function 
  sql2 = "select * from getAll()"
  cursor.execute(sql2)
  get_all = cursor.fetchall()
  print(get_all)

if mode == '2':
  sql3 = '''
  create or replace procedure addph1(name_ varchar,number_ varchar)
  as
  $$
  begin
      if  exists(select * from phonenumbers where name = name_) then
      update phonenumbers set number = number_ where name = name_;
    
	    else 
	    insert into phonenumbers(name,number) values (name_,number_);
	
	end if;
  end;
  $$
    LANGUAGE plpgsql
  '''
  cursor.execute(sql3)
  conn.commit()
  sql4 = "call  addph1('Aan','87086563625')"
  cursor.execute(sql4)
  conn.commit()

if mode == '3':
  sql5 = '''
    create or replace procedure task3(list varchar[][] ,size integer) as
    $$
    begin
    for i in 1..size loop
    if (list[i][2] like '87%') then
    insert into phonenumbers(name,number)
    values (list[i][1], list[i][2] );
    end if;
    end loop;
    end;
    $$
    language plpgsql
  '''
  cursor.execute(sql5)
  conn.commit()
  sql6 = "call task3('{{'ereke', '87083907226'}, {'ak', '+7083907221'}}', 2)"
  cursor.execute(sql6)
  conn.commit()

if mode == '4':
    sql7 = '''
    create or replace function pagination(offset_ integer,limit_ integer)
    returns table
      (
                    name varchar,
                    number  varchar
                )
    as
    $$
    begin
        return query
            select ph.name,  ph.number 
            from phonenumbers  as ph offset offset_ limit limit_;
    end
    $$ language plpgsql
    '''
    cursor.execute(sql7)
    conn.commit()
    sql8 = "cursor.callproc('pagination', (1,2))"
    cursor.execute(sql8)
    results = cursor.fetchall()
    print(results)

if mode == '5':
  sql9 = '''
  create or replace procedure deleteph(name_ varchar)
  as
  $$
  begin
      delete from phonenumbers where name = name_;
  end;
  $$
      LANGUAGE plpgsql;
  '''
  cursor.execute(sql9)
  conn.commit()
  sql10 = "call  deleteph('Miras')"
  cursor.execute(sql10)
  conn.commit()

cursor.close()
conn.close()



