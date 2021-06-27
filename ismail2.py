#!/usr/bin/python3

import psycopg2
import sys
def check_database():
   con = psycopg2.connect(user='postgres',password='postgres') #connect to database postgres
   con.autocommit = True
   cur = con.cursor()
   cur.execute("""SELECT datname FROM pg_database;""")
   list_database = cur.fetchall()
   if ('zone_de_stockage',) not in list_database:
      cur.execute("CREATE database zone_de_stockage")
      print("Database zone_de_stockage Created ...")
   cur.close()
   con.close()
   c_table()



def c_table():
   con = psycopg2.connect(database='zone_de_stockage',user='postgres',password='postgres') #connect to database postgr>
   cur = con.cursor()
   print("Connected To zone_de_stockage ...")
   cur.execute("SELECT table_name FROM information_schema.tables where table_schema = 'public';")
   list_tables = cur.fetchall()
   if ('line1',) not in list_tables:
      cur.execute("CREATE TABLE line1 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT , emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line2 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line3 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line4 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line5 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line6 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line7 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line8 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line9 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line10 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line11 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line12 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line13 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line14 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line15 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line16 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line17 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line18 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line19 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line20 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      cur.execute("CREATE TABLE line21 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
      con.commit()
      con.close()


def insert_stockage(names,dimension_conteneur):
   c = [14,14,14,16,14,14,15,15,14,14,14,13,14,13,14,14,13,14,14,13,14]
   distance = {"pile1":6,"pile2":12,"pile3":14}
   con = psycopg2.connect(database='zone_de_stockage',user='postgres',password='postgres') #connect to database postgr>
   cur = con.cursor()
   #dimension = 20
   for i in range(21):
      if i == 0:
         dimension = [20,20,40,20,40,40,20,20,20,40,20,40,20,40]
      elif i == 1:
         dimension = [20,40,40,20,20,40,40,20,20,20,40,20,20,40]
      elif i == 2: 
         dimension = [40,20,20,40,20,20,20,20,20,40,20,40,40,40]
      elif i == 3: 
         dimension = [20,20,40,20,20,40,20,40,20,20,20,20,40,20,20,20]
      elif i == 4: 
         dimension = [40,20,20,40,20,20,40,40,40,20,20,20,40,20]
      elif i == 5: 
         dimension = [40,20,40,20,40,20,20,20,40,40,20,20,20,40]
      elif i == 6: 
         dimension = [20,20,40,40,20,20,40,20,20,20,20,40,20,40,20]
      elif i == 7: 
         dimension = [40,40,20,20,20,20,20,40,20,40,20,20,20,20,40]
      elif i == 8: 
         dimension = [20,40,20,40,40,20,40,20,20,40,20,20,40,20]
      elif i == 9: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 10: 
         dimension = [40,40,20,40,20,20,40,20,40,20,20,20,40,20]
      elif i == 11: 
         dimension = [20,40,20,40,40,20,40,40,20,20,40,20,40]
      elif i == 12: 
         dimension = [40,20,20,40,20,20,40,20,40,40,20,40,20,20]
      elif i == 13: 
         dimension = [40,20,40,40,20,40,20,20,40,20,40,40,20]
      elif i == 14: 
         dimension = [40,20,40,20,20,40,20,20,40,40,20,20,20,40]
      elif i == 15: 
         dimension = [20,20,20,40,40,20,40,40,20,20,40,20,40,20]
      elif i == 16: 
         dimension = [40,20,20,20,40,40,20,40,40,40,20,20,40]
      elif i == 17: 
         dimension = [20,20,20,40,20,40,40,20,40,20,20,40,20,40]
      elif i == 18: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 19: 
         dimension = [20,40,20,40,40,20,40,40,20,20,20,40,40]
      elif i == 20: 
         dimension = [40,40,20,40,20,20,20,40,20,40,40,20,20,20]
      else:
         pass
      for p in range(c[i]): #pile
        cur.execute("SELECT emplacement1 FROM line"+str(i+1)+" where pile = "+str(p+1))
        data1 = cur.fetchall()
        #cur.execute("SELECT emplacement2 FROM line"+str(i+1)+" where pile = "+str(p+1))
        #data2 = cur.fetchall()
        #cur.execute("SELECT emplacement3 FROM line"+str(i+1)+" where pile = "+str(p+1))
        #data3 = cur.fetchall()
        if not data1:
           if dimension_conteneur == dimension[p]:
              emplacement1 = names
              emplacement2 = "0"
              emplacement3 = "0"
              cur.execute("INSERT INTO line"+str(i+1)+" VALUES('"+str(p+1)+"','"+str(dimension[p])+"','"+str(dimension_conteneur)+"','"+str(emplacement1)+"','"+str(emplacement2)+"','"+str(emplacement3)+"')")
              con.commit()
              print (names+" est dans la "+str(i+1)+" line, "+str(p+1)+" pile, premier emplacement")
              #con.close()
              return None
 
        if ("0",) in data1:
           if dimension_conteneur == dimension[p]:
              cur.execute("UPDATE line"+str(i+1)+" SET emplacement1 = '"+names+"',emplacement2 = '0',emplacement3 = '0' where pile = "+str(p+1))
              con.commit()
              return None
              print (names+" est dans la "+str(i+1)+" line, "+str(p+1)+" pile, premier emplacement")

   for i in range(21):
      if i == 0:
         dimension = [20,20,40,20,40,40,20,20,20,40,20,40,20,40]
      elif i == 1:
         dimension = [20,40,40,20,20,40,40,20,20,20,40,20,20,40]
      elif i == 2: 
         dimension = [40,20,20,40,20,20,20,20,20,40,20,40,40,40]
      elif i == 3: 
         dimension = [20,20,40,20,20,40,20,40,20,20,20,20,40,20,20,20]
      elif i == 4: 
         dimension = [40,20,20,40,20,20,40,40,40,20,20,20,40,20]
      elif i == 5: 
         dimension = [40,20,40,20,40,20,20,20,40,40,20,20,20,40]
      elif i == 6: 
         dimension = [20,20,40,40,20,20,40,20,20,20,20,40,20,40,20]
      elif i == 7: 
         dimension = [40,40,20,20,20,20,20,40,20,40,20,20,20,20,40]
      elif i == 8: 
         dimension = [20,40,20,40,40,20,40,20,20,40,20,20,40,20]
      elif i == 9: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 10: 
         dimension = [40,40,20,40,20,20,40,20,40,20,20,20,40,20]
      elif i == 11: 
         dimension = [20,40,20,40,40,20,40,40,20,20,40,20,40]
      elif i == 12: 
         dimension = [40,20,20,40,20,20,40,20,40,40,20,40,20,20]
      elif i == 13: 
         dimension = [40,20,40,40,20,40,20,20,40,20,40,40,20]
      elif i == 14: 
         dimension = [40,20,40,20,20,40,20,20,40,40,20,20,20,40]
      elif i == 15: 
         dimension = [20,20,20,40,40,20,40,40,20,20,40,20,40,20]
      elif i == 16: 
         dimension = [40,20,20,20,40,40,20,40,40,40,20,20,40]
      elif i == 17: 
         dimension = [20,20,20,40,20,40,40,20,40,20,20,40,20,40]
      elif i == 18: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 19: 
         dimension = [20,40,20,40,40,20,40,40,20,20,20,40,40]
      elif i == 20: 
         dimension = [40,40,20,40,20,20,20,40,20,40,40,20,20,20]
      else:
         pass

      for p in range(c[i]):
         cur.execute("SELECT emplacement2 FROM line"+str(i+1)+" where pile = "+str(p+1))
         data2 = cur.fetchall()
         #cur.execute("SELECT emplacement3 FROM line"+str(i+1)+" where pile = "+str(p+1))
         #data3 = cur.fetchall()
         if ("0",) in data2:
            if dimension_conteneur == dimension[p]:
               cur.execute("UPDATE line"+str(i+1)+" SET emplacement2 = '"+names+"' where pile = "+str(p+1))
               con.commit()
               print (names+" est dans la "+str(i+1)+" line, "+str(p+1)+" pile, deuxieme emplacement")
               return None
   for i in range(21):
      if i == 0:
         dimension = [20,20,40,20,40,40,20,20,20,40,20,40,20,40]
      elif i == 1:
         dimension = [20,40,40,20,20,40,40,20,20,20,40,20,20,40]
      elif i == 2: 
         dimension = [40,20,20,40,20,20,20,20,20,40,20,40,40,40]
      elif i == 3: 
         dimension = [20,20,40,20,20,40,20,40,20,20,20,20,40,20,20,20]
      elif i == 4: 
         dimension = [40,20,20,40,20,20,40,40,40,20,20,20,40,20]
      elif i == 5: 
         dimension = [40,20,40,20,40,20,20,20,40,40,20,20,20,40]
      elif i == 6: 
         dimension = [20,20,40,40,20,20,40,20,20,20,20,40,20,40,20]
      elif i == 7: 
         dimension = [40,40,20,20,20,20,20,40,20,40,20,20,20,20,40]
      elif i == 8: 
         dimension = [20,40,20,40,40,20,40,20,20,40,20,20,40,20]
      elif i == 9: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 10: 
         dimension = [40,40,20,40,20,20,40,20,40,20,20,20,40,20]
      elif i == 11: 
         dimension = [20,40,20,40,40,20,40,40,20,20,40,20,40]
      elif i == 12: 
         dimension = [40,20,20,40,20,20,40,20,40,40,20,40,20,20]
      elif i == 13: 
         dimension = [40,20,40,40,20,40,20,20,40,20,40,40,20]
      elif i == 14: 
         dimension = [40,20,40,20,20,40,20,20,40,40,20,20,20,40]
      elif i == 15: 
         dimension = [20,20,20,40,40,20,40,40,20,20,40,20,40,20]
      elif i == 16: 
         dimension = [40,20,20,20,40,40,20,40,40,40,20,20,40]
      elif i == 17: 
         dimension = [20,20,20,40,20,40,40,20,40,20,20,40,20,40]
      elif i == 18: 
         dimension = [20,20,40,40,20,40,20,40,40,20,20,40,20,20]
      elif i == 19: 
         dimension = [20,40,20,40,40,20,40,40,20,20,20,40,40]
      elif i == 20: 
         dimension = [40,40,20,40,20,20,20,40,20,40,40,20,20,20]
      else:
         pass

      for p in range(c[i]):
         cur.execute("SELECT emplacement3 FROM line"+str(i+1)+" where pile = "+str(p+1)) 
         data3 = cur.fetchall()
         if ("0",) in data3:
            if dimension_conteneur == dimension[p]:
               cur.execute("UPDATE line"+str(i+1)+" SET emplacement3 = '"+names+"' where pile = "+str(p+1))
               con.commit()
               print (names+" est dans la "+str(i+1)+" line, "+str(p+1)+" pile, troisieme emplacement")
               return None
#table : url_info
#column : main_site,parameter
#table : vuln
#column : parameter_vuln,url_vuln


def sorti():
   con = psycopg2.connect(database='zone_de_stockage',user='postgres',password='postgres') #connect to database postgr>
   cur = con.cursor()
   list_visit = ['cx88','cont12']
   for Av in list_visit:
      for table in range(21):
         cur.execute("select emplacement3 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em3 = cur.fetchall()
         cur.execute("select emplacement2 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em2 = cur.fetchall()
         cur.execute("select emplacement1 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em1 = cur.fetchall()
         #print(str(em1)+'zooba')
         #cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '"+Av+"')
         #p = cur.fetchall()
         #print(str(em3)+"and "+str(em2)+" and"+str(em1))
         if (Av,) in em3:
            cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '"+Av+"'")
            p = cur.fetchall()
            print(Av+" est un sommet")
            print(Av+" est dans la line "+str(table+1)+", pile "+str(p[0][0])+", emplacement3")
            cur.execute("update line"+str(table+1)+" SET emplacement3='0' where pile ='"+str(p[0][0])+"'")
            con.commit()
            return None
         elif (Av,) in em2 and ("0",) in em3:
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '"+Av+"'")
            p = cur.fetchall()
            print(Av+" est un sommet")
            print(Av+" est dans la line "+str(table+1)+", pile "+str(p[0][0])+", emplacement2")
            cur.execute("update line"+str(table+1)+" SET emplacement2='0' where pile ='"+str(p[0][0])+"'")
            con.commit()
            return None
         elif (Av,) in em1 and ("0",) in em2:
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '"+Av+"'")
            p = cur.fetchall()
            print(Av+" est un sommet")
            print(Av+" est dans la line "+str(table+1)+", pile "+str(p[0][0])+", emplacement1")
            cur.execute("update line"+str(table+1)+" SET emplacement1='0' where pile ='"+str(p[0][0])+"'")
            con.commit()
            return None
         else:
            pass
   for Av in list_visit:
      for table in range(21):
         cur.execute("select emplacement3 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em3 = cur.fetchall()
         cur.execute("select emplacement2 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em2 = cur.fetchall()
         cur.execute("select emplacement1 from line"+str(table+1)+" where emplacement1 = '"+Av+"' or emplacement2 = '"+Av+"' or emplacement3 = '"+Av+"'")
         em1 = cur.fetchall()
         #print(em3+"zoova")
         if (Av,) in em2 and em3 != ("0",):
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '"+Av+"'")
            p = cur.fetchall()
            print(Av+ " not sommet")
            print(Av+" est dans la line "+str(table+1)+", pile "+str(p[0][0])+", emplacement2")
            cur.execute("select dimension_conteneur from line"+str(table+1)+" where pile = '"+str(p[0][0])+"'")
            dim_p = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            s = cur.fetchall()
            if s:
               print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(s[0][0])+", emplacement1")
               cur.execute("update line"+str(table+1)+" SET emplacement1='"+str(em3[0][0])+"' where pile = '"+str(s[0][0])+"'")
               con.commit()
               cur.execute("update line"+str(table+1)+" SET emplacement2='0',emplacement3='0' where pile ='"+str(p[0][0])+"'")
               con.commit()
               return None
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            x = cur.fetchall()
            if x:
               if x[0][0] not in list_visit:
                  print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(x[0][0])+", emplacement2")
                  cur.execute("update line"+str(table+1)+" SET emplacement2='"+str(em3[0][0])+"' where pile = '"+str(x[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement2='0',emplacement3='0' where pile ='"+str(p[0][0])+"'")
                  con.commit()
                  return None
            cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            y = cur.fetchall()
            if y:
               if y[0][0] not in list_visit:
                  print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(y[0][0])+", emplacement3")
                  cur.execute("update line"+str(table+1)+" SET emplacement3='"+str(em3[0][0])+"' where pile = '"+str(y[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement2='0',emplacement3='0' where pile ='"+str(p[0][0])+"'")
                  con.commit()
                  return None


         elif (Av,) in em1 and em2 != ("0",) and ("0",) in em3:
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '"+Av+"'")
            p = cur.fetchall()
            print(Av+" not sommet")
            print(Av+" est dans la line "+str(table+1)+", pile "+str(p[0][0])+", emplacement1")
            cur.execute("select dimension_conteneur from line"+str(table+1)+" where pile = '"+str(p[0][0])+"'")
            dim_p = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            s1 = cur.fetchall()
            if s1:
               print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(s1[0][0])+", emplacement1")
               cur.execute("update line"+str(table+1)+" SET emplacement1='"+str(em2[0][0])+"' where pile = '"+str(s1[0][0])+"'")
               con.commit()
               cur.execute("update line"+str(table+1)+" SET emplacement1 = '0', emplacement2 = '0',emplacement3='0' where pile = '"+str(p[0][0])+"'")
               con.commit()
               return None
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            x = cur.fetchall()
            if x:
               if x[0][0] not in list_visit:
                  print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(x[0][0])+", emplacement2")
                  cur.execute("update line"+str(table+1)+" SET emplacement2='"+str(em2[0][0])+"' where pile = '"+str(x[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement1 = '0' emplacement2 ='0', emplacement3 = '0' where pile = '"+str(p[0][0])+"'")
                  con.commit()
                  return None

            cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            y = cur.fetchall()
            if y:
               if y[0][0] not in list_visit:
                  print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(y[0][0])+", emplacement3")
                  cur.execute("update line"+str(table+1)+" SET emplacement3='"+str(em2[0][0])+"' where pile = '"+str(y[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement1 = '0' emplacement2 ='0', emplacement3 = '0' where pile = '"+str(p[0][0])+"'")
                  con.commit()
                  return None

#            cur.execute("update line"+str(table+1)+" SET emplacement1='0' where pile ='"+str(p[0][0])+"'")
#            con.commit()
         elif (Av,) in em1 and em2 != ("0",) and em3 != ("0"):
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '"+Av+"'")
            p1 = cur.fetchall()
            print(Av+" not sommet")
            print(Av+" est dans la line"+str(table+1)+", pile "+str(p1[0][0])+", emplacement1")
            cur.execute("select dimension_conteneur from line"+str(table+1)+" where pile = '"+str(p1[0][0])+"'")
            dim_p = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            s2 = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            x = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            y = cur.fetchall()

            if s2:
               print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(s2[0][0])+", emplacement1")
               cur.execute("update line"+str(table+1)+" SET emplacement1 = '"+str(em3[0][0])+"' where pile = '"+str(s2[0][0])+"'")
               con.commit()
               cur.execute("update line"+str(table+1)+" SET emplacement3 = '0' where pile = '"+str(p1[0][0])+"'")
               con.commit()
            elif x:
               if x[0][0] not in list_visit:
                  print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(x[0][0])+", emplacement2")
                  cur.execute("update line"+str(table+1)+" SET emplacement2 = '"+str(em3[0][0])+"' where pile = '"+str(x[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement3 = '0' where pile = '"+str(p1[0][0])+"'")
                  con.commit()
            elif y:
               if y[0][0] not in list_visit:
                  print("deplacer "+str(em3[0][0])+" vers line"+str(table+1)+", pile "+str(y[0][0])+", emplacement3")
                  cur.execute("update line"+str(table+1)+" SET emplacement3 = '"+str(em3[0][0])+"' where pile = '"+str(y[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement3 = '0' where pile = '"+str(p1[0][0])+"'")
                  con.commit()
            else:
               pass
            cur.execute("select pile from line"+str(table+1)+" where emplacement1 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            s3 = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement2 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            x = cur.fetchall()
            cur.execute("select pile from line"+str(table+1)+" where emplacement3 = '0' and dimension = '"+str(dim_p[0][0])+"'")
            y = cur.fetchall()

            if s3:
               print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(s3[0][0])+", emplacement1")
               cur.execute("update line"+str(table+1)+" SET emplacement1 = '"+str(em2[0][0])+"' where pile = '"+str(s3[0][0])+"'")
               con.commit()
               cur.execute("update line"+str(table+1)+" SET emplacement1 = '0', emplacement2 = '0' where pile = '"+str(p1[0][0])+"'") 
               con.commit()
               return None
            elif x :
               if x[0][0] not in list_visit:
                  print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(x[0][0])+", emplacement2")
                  cur.execute("update line"+str(table+1)+" SET emplacement2 = '"+str(em2[0][0])+"' where pile = '"+str(x[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement1 = '0', emplacement2 = '0' where pile = '"+str(p1[0][0])+"'")
                  con.commit()
                  return None
            elif y :
               if y[0][0] not in list_visit:
                  print("deplacer "+str(em2[0][0])+" vers line"+str(table+1)+", pile "+str(y[0][0])+", emplacement3") 
                  cur.execute("update line"+str(table+1)+" SET emplacement3 = '"+str(em2[0][0])+"' where pile = '"+str(y[0][0])+"'")
                  con.commit()
                  cur.execute("update line"+str(table+1)+" SET emplacement1 = '0', emplacement2 = '0' where pile = '"+str(p1[0][0])+"'")
                  con.commit()
                  return None
            else:
               pass


         else:
            pass
            #print("please verifier votre conteneur il n exsit pas dans ma base de donnes")


def all():
   j=0
   i=0
   k=0
   Ad = []
   A0 = []
   Av= []
   l= []
   choix = input("Sort ou stock 1/2 : ")
   if choix == "1":
      sorti()
   elif choix == "2":
      names = input("Entrer le nom de conteneur : ")
      dimension_conteneur = int(input("Entrer la dimension de "+names+" : "))
      A0.append(names)
      insert_stockage(names,dimension_conteneur)
   else:
      print("please entrer 1 ou 2")
      sys.exit()

if __name__ == "__main__":
   check_database()
   all()
