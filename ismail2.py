#!/usr/bin/python3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys, os
from os import path
from mainwindow import Ui_Form
import psycopg2
import sys
from datetime import date
from datetime import datetime


FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"mains.ui"))
class main(QWidget,FORM_CLASS):
   def __init__(self, parent = None):
      super(main,self).__init__(parent)
      QWidget.__init__(self)
      global list_visit
      global list1
      global f
      global d
      d = {}
      list_visit = []
      list1 = []
      f = 0
      self.setupUi(self)
      self.pushButton.clicked.connect(self.addst)
      self.pushButton_2.clicked.connect(self.addvs)
      self.pushButton_3.clicked.connect(self.depl)
      self.pushButton_4.clicked.connect(self.clr)
      self.pushButton_5.clicked.connect(self.clrst)
      self.check_database()
      self.c_table()

   def dates(self):
       datex = date.today()
       d = datex.strftime("%d-%m-%Y") + ".txt"
       return d

   def times(self):
       now = datetime.now()
       tim = now.strftime("%H:%M:%S")
       return tim

   def check_database(self):
       con = psycopg2.connect(user='postgres', password='postgres')  # connect to database postgres
       con.autocommit = True
       cur = con.cursor()
       cur.execute("""SELECT datname FROM pg_database;""")
       list_database = cur.fetchall()
       if ('zone_de_stockage',) not in list_database:
           cur.execute("CREATE database zone_de_stockage")
           print("Database zone_de_stockage Created ...")
       cur.close()
       con.close()

   def c_table(self):
       con = psycopg2.connect(database='zone_de_stockage', user='postgres',
                              password='postgres')  # connect to database postgr>
       cur = con.cursor()
       print("Connected To zone_de_stockage ...")
       cur.execute("SELECT table_name FROM information_schema.tables where table_schema = 'public';")
       list_tables = cur.fetchall()
       if ('line1',) not in list_tables:
           cur.execute(
               "CREATE TABLE line1 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT , emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line2 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line3 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line4 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line5 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line6 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line7 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line8 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line9 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line10 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line11 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line12 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line13 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line14 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line15 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line16 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line17 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line18 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line19 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line20 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           cur.execute(
               "CREATE TABLE line21 (pile INT, dimension INT,dimension_conteneur INT, emplacement1 TEXT, emplacement2 TEXT, emplacement3 TEXT)")
           con.commit()
           con.close()

   def insert_stockage(self,names, dimension_conteneur, list_visita):

       c = [14, 14, 14, 16, 14, 14, 15, 15, 14, 14, 14, 13, 14, 13, 14, 14, 13, 14, 14, 13, 14]
       con = psycopg2.connect(database='zone_de_stockage', user='postgres',
                              password='postgres')  # connect to database postgr>
       cur = con.cursor()
       # dimension = 20
       for i in range(21):
           if i == 0:
               dimension = [20, 20, 40, 20, 40, 40, 20, 20, 20, 40, 20, 40, 20, 40]
           elif i == 1:
               dimension = [20, 40, 40, 20, 20, 40, 40, 20, 20, 20, 40, 20, 20, 40]
           elif i == 2:
               dimension = [40, 20, 20, 40, 20, 20, 20, 20, 20, 40, 20, 40, 40, 40]
           elif i == 3:
               dimension = [20, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40, 20, 20, 20]
           elif i == 4:
               dimension = [40, 20, 20, 40, 20, 20, 40, 40, 40, 20, 20, 20, 40, 20]
           elif i == 5:
               dimension = [40, 20, 40, 20, 40, 20, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 6:
               dimension = [20, 20, 40, 40, 20, 20, 40, 20, 20, 20, 20, 40, 20, 40, 20]
           elif i == 7:
               dimension = [40, 40, 20, 20, 20, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40]
           elif i == 8:
               dimension = [20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 20, 40, 20]
           elif i == 9:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 10:
               dimension = [40, 40, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 40, 20]
           elif i == 11:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40]
           elif i == 12:
               dimension = [40, 20, 20, 40, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20]
           elif i == 13:
               dimension = [40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40, 40, 20]
           elif i == 14:
               dimension = [40, 20, 40, 20, 20, 40, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 15:
               dimension = [20, 20, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40, 20]
           elif i == 16:
               dimension = [40, 20, 20, 20, 40, 40, 20, 40, 40, 40, 20, 20, 40]
           elif i == 17:
               dimension = [20, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40]
           elif i == 18:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 19:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 20, 40, 40]
           elif i == 20:
               dimension = [40, 40, 20, 40, 20, 20, 20, 40, 20, 40, 40, 20, 20, 20]
           else:
               pass
           for p in range(c[i]):  # pile
               cur.execute("SELECT emplacement1 FROM line" + str(i + 1) + " where pile = " + str(p + 1))
               data1 = cur.fetchall()
               # print (data1)
               # cur.execute("SELECT emplacement2 FROM line"+str(i+1)+" where pile = "+str(p+1))
               # data2 = cur.fetchall()
               # cur.execute("SELECT emplacement3 FROM line"+str(i+1)+" where pile = "+str(p+1))
               # data3 = cur.fetchall()
               if not data1:
                   if dimension_conteneur == dimension[p]:
                       emplacement1 = names
                       emplacement2 = "0"
                       emplacement3 = "0"
                       cur.execute("INSERT INTO line" + str(i + 1) + " VALUES('" + str(p + 1) + "','" + str(
                           dimension[p]) + "','" + str(dimension_conteneur) + "','" + str(emplacement1) + "','" + str(
                           emplacement2) + "','" + str(emplacement3) + "')")
                       con.commit()
                       self.showdialog(
                           names + " est dans la " + str(i + 1) + " line, " + str(p + 1) + " pile, premier emplacement")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + names + " est dans la " + str(i + 1) + " line, " + str(
                               p + 1) + " pile, premier emplacement")
                           folder.close()
                       return None

               if ("0",) in data1:
                   if dimension_conteneur == dimension[p]:
                       cur.execute("UPDATE line" + str(
                           i + 1) + " SET emplacement1 = '" + names + "',emplacement2 = '0',emplacement3 = '0' where pile = " + str(
                           p + 1))
                       con.commit()
                       self.showdialog(
                           names + " est dans la " + str(i + 1) + " line, " + str(p + 1) + " pile, premier emplacement")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + names + " est dans la " + str(i + 1) + " line, " + str(
                               p + 1) + " pile, premier emplacement\n")
                           folder.close()
                       return None
       for i in range(21):
           if i == 0:
               dimension = [20, 20, 40, 20, 40, 40, 20, 20, 20, 40, 20, 40, 20, 40]
           elif i == 1:
               dimension = [20, 40, 40, 20, 20, 40, 40, 20, 20, 20, 40, 20, 20, 40]
           elif i == 2:
               dimension = [40, 20, 20, 40, 20, 20, 20, 20, 20, 40, 20, 40, 40, 40]
           elif i == 3:
               dimension = [20, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40, 20, 20, 20]
           elif i == 4:
               dimension = [40, 20, 20, 40, 20, 20, 40, 40, 40, 20, 20, 20, 40, 20]
           elif i == 5:
               dimension = [40, 20, 40, 20, 40, 20, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 6:
               dimension = [20, 20, 40, 40, 20, 20, 40, 20, 20, 20, 20, 40, 20, 40, 20]
           elif i == 7:
               dimension = [40, 40, 20, 20, 20, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40]
           elif i == 8:
               dimension = [20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 20, 40, 20]
           elif i == 9:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 10:
               dimension = [40, 40, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 40, 20]
           elif i == 11:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40]
           elif i == 12:
               dimension = [40, 20, 20, 40, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20]
           elif i == 13:
               dimension = [40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40, 40, 20]
           elif i == 14:
               dimension = [40, 20, 40, 20, 20, 40, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 15:
               dimension = [20, 20, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40, 20]
           elif i == 16:
               dimension = [40, 20, 20, 20, 40, 40, 20, 40, 40, 40, 20, 20, 40]
           elif i == 17:
               dimension = [20, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40]
           elif i == 18:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 19:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 20, 40, 40]
           elif i == 20:
               dimension = [40, 40, 20, 40, 20, 20, 20, 40, 20, 40, 40, 20, 20, 20]
           else:
               pass

           for p in range(c[i]):
               cur.execute("SELECT emplacement2 FROM line" + str(i + 1) + " where pile = " + str(p + 1))
               data2 = cur.fetchall()
               # emplacement1 pour verifier est ce que dans la list des visits
               cur.execute("select emplacement1 from line" + str(i + 1) + " where pile = " + str(p + 1))
               empl1 = cur.fetchall()
               # cur.execute("SELECT emplacement3 FROM line"+str(i+1)+" where pile = "+str(p+1))
               # data3 = cur.fetchall()
               if ("0",) in data2:
                   if dimension_conteneur == dimension[p] and empl1[0][0] not in list_visita:
                       cur.execute(
                           "UPDATE line" + str(i + 1) + " SET emplacement2 = '" + names + "' where pile = " + str(
                               p + 1))
                       con.commit()
                       self.showdialog(names + " est dans la " + str(i + 1) + " line, " + str(
                           p + 1) + " pile, deuxieme emplacement")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + names + " est dans la " + str(i + 1) + " line, " + str(
                               p + 1) + " pile, deuxieme emplacement\n")
                           folder.close()
                       return None
       for i in range(21):
           if i == 0:
               dimension = [20, 20, 40, 20, 40, 40, 20, 20, 20, 40, 20, 40, 20, 40]
           elif i == 1:
               dimension = [20, 40, 40, 20, 20, 40, 40, 20, 20, 20, 40, 20, 20, 40]
           elif i == 2:
               dimension = [40, 20, 20, 40, 20, 20, 20, 20, 20, 40, 20, 40, 40, 40]
           elif i == 3:
               dimension = [20, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40, 20, 20, 20]
           elif i == 4:
               dimension = [40, 20, 20, 40, 20, 20, 40, 40, 40, 20, 20, 20, 40, 20]
           elif i == 5:
               dimension = [40, 20, 40, 20, 40, 20, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 6:
               dimension = [20, 20, 40, 40, 20, 20, 40, 20, 20, 20, 20, 40, 20, 40, 20]
           elif i == 7:
               dimension = [40, 40, 20, 20, 20, 20, 20, 40, 20, 40, 20, 20, 20, 20, 40]
           elif i == 8:
               dimension = [20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 20, 40, 20]
           elif i == 9:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 10:
               dimension = [40, 40, 20, 40, 20, 20, 40, 20, 40, 20, 20, 20, 40, 20]
           elif i == 11:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40]
           elif i == 12:
               dimension = [40, 20, 20, 40, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20]
           elif i == 13:
               dimension = [40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40, 40, 20]
           elif i == 14:
               dimension = [40, 20, 40, 20, 20, 40, 20, 20, 40, 40, 20, 20, 20, 40]
           elif i == 15:
               dimension = [20, 20, 20, 40, 40, 20, 40, 40, 20, 20, 40, 20, 40, 20]
           elif i == 16:
               dimension = [40, 20, 20, 20, 40, 40, 20, 40, 40, 40, 20, 20, 40]
           elif i == 17:
               dimension = [20, 20, 20, 40, 20, 40, 40, 20, 40, 20, 20, 40, 20, 40]
           elif i == 18:
               dimension = [20, 20, 40, 40, 20, 40, 20, 40, 40, 20, 20, 40, 20, 20]
           elif i == 19:
               dimension = [20, 40, 20, 40, 40, 20, 40, 40, 20, 20, 20, 40, 40]
           elif i == 20:
               dimension = [40, 40, 20, 40, 20, 20, 20, 40, 20, 40, 40, 20, 20, 20]
           else:
               pass

           for p in range(c[i]):
               cur.execute("SELECT emplacement3 FROM line" + str(i + 1) + " where pile = " + str(p + 1))
               data3 = cur.fetchall()
               cur.execute("select emplacement2 from line" + str(i + 1) + " where pile = " + str(p + 1))
               empl2 = cur.fetchall()
               cur.execute("select emplacement1 from line" + str(i + 1) + " where pile = " + str(p + 1))
               empl1 = cur.fetchall()
               if ("0",) in data3:
                   if dimension_conteneur == dimension[p] and empl1[0][0] not in list_visita and empl2[0][
                       0] not in list_visita:
                       cur.execute(
                           "UPDATE line" + str(i + 1) + " SET emplacement3 = '" + names + "' where pile = " + str(
                               p + 1))
                       con.commit()
                       self.showdialog(names + " est dans la " + str(i + 1) + " line, " + str(
                           p + 1) + " pile, troisieme emplacement")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + names + " est dans la " + str(i + 1) + " line, " + str(
                               p + 1) + " pile, troisieme emplacement\n")
                           folder.close()
                       return None

   # table : url_info
   # column : main_site,parameter
   # table : vuln
   # column : parameter_vuln,url_vuln

   def sorti(self,list_visita):
       global list_visit
       global d
       global list1
       con = psycopg2.connect(database='zone_de_stockage', user='postgres',
                              password='postgres')  # connect to database postgr>
       cur = con.cursor()
       # list_visita = ['cx318']
       list_visit6 = []
       list_visit5 = []
       list_visit4 = []
       list_visit3 = []
       list_visit2 = []
       list_visit1 = []
       for Av in list_visita:
           for table in range(21):
               cur.execute("select emplacement3 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em3 = cur.fetchall()
               cur.execute("select emplacement2 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em2 = cur.fetchall()
               cur.execute("select emplacement1 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em1 = cur.fetchall()
               if (Av,) in em1 and ("0",) in em2 and ("0",) in em3:
                   list_visit1.append(Av)
                   break
               elif (Av,) in em2 and ("0",) in em3:
                   list_visit2.append(Av)
                   break
               elif (Av,) in em3:
                   list_visit3.append(Av)
                   break
               elif (Av,) in em1 and ("0",) not in em2 and ("0",) in em3:
                   list_visit4.append(Av)
                   break
               elif (Av,) in em2 and ("0",) not in em3:
                   list_visit5.append(Av)
                   break
               elif (Av,) in em1 and ("0",) not in em2 and ("0",) not in em3:
                   list_visit6.append(Av)
                   break
               else:
                   pass
       list_visit = list_visit1 + list_visit2 + list_visit3 + list_visit4 + list_visit5 + list_visit6
       # print (list_visit)
       for Av in list_visit:
           for table in range(21):
               cur.execute("select emplacement3 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em3 = cur.fetchall()
               cur.execute("select emplacement2 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em2 = cur.fetchall()
               cur.execute("select emplacement1 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em1 = cur.fetchall()

               if (Av,) in em3:
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement3 = '" + Av + "'")
                   p = cur.fetchall()
                   self.showdialog(Av + " est un sommet ,"+Av + " est dans la line " + str(table + 1) + ", pile " + str(p[0][0]) + ", emplacement3")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + "]" + Av + " est dans la line " + str(table + 1) + ", pile " + str(
                           p[0][0]) + ", emplacement3\n")
                       folder.close()
                   cur.execute(
                       "update line" + str(table + 1) + " SET emplacement3='0' where pile ='" + str(p[0][0]) + "'")
                   con.commit()
                   #self.tableWidget_2.removeRow(d[Av])
                   self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                   if list_visit:
                      del list_visit[0]

                   return None
               elif (Av,) in em2 and ("0",) in em3:
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement2 = '" + Av + "'")
                   p = cur.fetchall()
                   self.showdialog(Av + " est un sommet ,"+Av + " est dans la line " + str(table + 1) + ", pile " + str(p[0][0]) + ", emplacement2")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + Av + " est dans la line " + str(table + 1) + ", pile " + str(
                           p[0][0]) + ", emplacement2\n")
                       folder.close()
                   cur.execute(
                       "update line" + str(table + 1) + " SET emplacement2='0' where pile ='" + str(p[0][0]) + "'")
                   con.commit()
                   del list_visit[0]
                   self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                   return None
               elif (Av,) in em1 and ("0",) in em2:
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement1 = '" + Av + "'")
                   p = cur.fetchall()
                   self.showdialog(Av + " est un sommet ,"+Av + " est dans la line " + str(table + 1) + ", pile " + str(p[0][0]) + ", emplacement1")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + Av + " est dans la line " + str(table + 1) + ", pile " + str(
                           p[0][0]) + ", emplacement1\n")
                       folder.close()
                   cur.execute(
                       "update line" + str(table + 1) + " SET emplacement1='0' where pile ='" + str(p[0][0]) + "'")
                   con.commit()
                   self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                   if list_visit:
                      del list_visit[0]

                   return None
               else:
                   pass
       for Av in list_visit:
           for table in range(21):
               cur.execute("select emplacement3 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em3 = cur.fetchall()
               cur.execute("select emplacement2 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em2 = cur.fetchall()
               cur.execute("select emplacement1 from line" + str(
                   table + 1) + " where emplacement1 = '" + Av + "' or emplacement2 = '" + Av + "' or emplacement3 = '" + Av + "'")
               em1 = cur.fetchall()
               # print(em3+"zoova")
               if (Av,) in em2 and em3 != ("0",):
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement2 = '" + Av + "'")
                   p = cur.fetchall()
                   self.showdialog(Av + " not sommet ,"+Av + " est dans la line " + str(table + 1) + ", pile " + str(p[0][0]) + ", emplacement2")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + "]" + Av + " est dans la line " + str(table + 1) + ", pile " + str(
                           p[0][0]) + ", emplacement2\n")
                       folder.close()
                   cur.execute(
                       "select dimension_conteneur from line" + str(table + 1) + " where pile = '" + str(p[0][0]) + "'")
                   dim_p = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement1 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "'")
                   s = cur.fetchall()
                   if s:
                       self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                           s[0][0]) + ", emplacement1")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + " deplacer " + str(em3[0][0]) + " vers line" + str(
                               table + 1) + ", pile " + str(s[0][0]) + ", emplacement1\n")
                           folder.close()
                       cur.execute("update line" + str(table + 1) + " SET emplacement1='" + str(
                           em3[0][0]) + "' where pile = '" + str(s[0][0]) + "'")
                       con.commit()
                       cur.execute("update line" + str(
                           table + 1) + " SET emplacement2='0',emplacement3='0' where pile ='" + str(p[0][0]) + "'")
                       con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]
                       return None
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement2 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   x = cur.fetchall()

                   if x:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(x[0][0]) + "'")
                       emp1 = cur.fetchall()

                       if emp1[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               x[0][0]) + ", emplacement2")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em3[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(x[0][0]) + ", emplacement2\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement2='" + str(
                               em3[0][0]) + "' where pile = '" + str(x[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement2='0',emplacement3='0' where pile ='" + str(p[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement3 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement2 not like '" + Av + "'")
                   y = cur.fetchall()

                   if y:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp2 = cur.fetchall()
                       cur.execute(
                           "select emplacement2 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp3 = cur.fetchall()
                       if emp2[0][0] not in list_visit and emp3[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               y[0][0]) + ", emplacement3")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em3[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(y[0][0]) + ", emplacement3\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3='" + str(
                               em3[0][0]) + "' where pile = '" + str(y[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement2='0',emplacement3='0' where pile ='" + str(p[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

               elif (Av,) in em1 and em2 != ("0",) and ("0",) in em3:
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement1 = '" + Av + "'")
                   p = cur.fetchall()
                   self.showdialog(Av + " not sommet, "+Av + " est dans la line " + str(table + 1) + ", pile " + str(p[0][0]) + ", emplacement1")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + "]" + Av + " est dans la line " + str(table + 1) + ", pile " + str(
                           p[0][0]) + ", emplacement1\n")
                       folder.close()
                   cur.execute(
                       "select dimension_conteneur from line" + str(table + 1) + " where pile = '" + str(p[0][0]) + "'")
                   dim_p = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement1 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "'")
                   s1 = cur.fetchall()
                   if s1:
                       self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                           s1[0][0]) + ", emplacement1")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + " deplacer " + str(em2[0][0]) + " vers line" + str(
                               table + 1) + ", pile " + str(s1[0][0]) + ", emplacement1\n")
                           folder.close()
                       cur.execute("update line" + str(table + 1) + " SET emplacement1='" + str(
                           em2[0][0]) + "' where pile = '" + str(s1[0][0]) + "'")
                       con.commit()
                       cur.execute("update line" + str(
                           table + 1) + " SET emplacement1 = '0', emplacement2 = '0',emplacement3='0' where pile = '" + str(
                           p[0][0]) + "'")
                       con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]

                       return None
                   # select un pile vide
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement2 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   x = cur.fetchall()

                   if x:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(x[0][0]) + "'")
                       emp1 = cur.fetchall()

                       if emp1[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               x[0][0]) + ", emplacement2")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em2[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(x[0][0]) + ", emplacement2\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement2='" + str(
                               em2[0][0]) + "' where pile = '" + str(x[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement1 = '0', emplacement2 ='0', emplacement3 = '0' where pile = '" + str(
                               p[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement3 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "' ")
                   y = cur.fetchall()

                   if y:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp2 = cur.fetchall()
                       # print (emp2)
                       cur.execute(
                           "select emplacement2 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp3 = cur.fetchall()
                       # print(emp3)
                       if emp2[0][0] not in list_visit and emp3[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               y[0][0]) + ", emplacement3")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em2[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(y[0][0]) + ", emplacement3\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3='" + str(
                               em2[0][0]) + "' where pile = '" + str(y[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement1 = '0', emplacement2 ='0', emplacement3 = '0' where pile = '" + str(
                               p[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

               #            cur.execute("update line"+str(table+1)+" SET emplacement1='0' where pile ='"+str(p[0][0])+"'")
               #            con.commit()
               elif (Av,) in em1 and em2 != ("0",) and em3 != ("0"):
                   cur.execute("select pile from line" + str(table + 1) + " where emplacement1 = '" + Av + "'")
                   p1 = cur.fetchall()
                   self.showdialog(Av + " not sommet, "+Av + " est dans la line" + str(table + 1) + ", pile " + str(p1[0][0]) + ", emplacement1")

                   with open(self.dates(), "a") as folder:
                       folder.write("[" + self.times() + "]" + Av + " est dans la line" + str(table + 1) + ", pile " + str(
                           p1[0][0]) + ", emplacement1\n")
                       folder.close()
                   cur.execute("select dimension_conteneur from line" + str(table + 1) + " where pile = '" + str(
                       p1[0][0]) + "'")
                   dim_p = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement1 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "'")
                   s2 = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement2 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   x = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement3 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   y = cur.fetchall()

                   if s2:
                       self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                           s2[0][0]) + ", emplacement1")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "] " + "deplacer " + str(em3[0][0]) + " vers line" + str(
                               table + 1) + ", pile " + str(s2[0][0]) + ", emplacement1\n")
                           folder.close()
                       cur.execute("update line" + str(table + 1) + " SET emplacement1 = '" + str(
                           em3[0][0]) + "' where pile = '" + str(s2[0][0]) + "'")
                       con.commit()
                       cur.execute("update line" + str(table + 1) + " SET emplacement3 = '0' where pile = '" + str(
                           p1[0][0]) + "'")
                       con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]


                   elif x:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(x[0][0]) + "'")
                       emp1 = cur.fetchall()
                       if emp1[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               x[0][0]) + ", emplacement2")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em3[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(x[0][0]) + ", emplacement2\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement2 = '" + str(
                               em3[0][0]) + "' where pile = '" + str(x[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3 = '0' where pile = '" + str(
                               p1[0][0]) + "'")
                           con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]



                   elif y:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp2 = cur.fetchall()
                       cur.execute(
                           "select emplacement2 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp3 = cur.fetchall()
                       if emp2[0][0] not in list_visit and emp3 not in list_visit:
                           self.showdialog("deplacer " + str(em3[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               y[0][0]) + ", emplacement3")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "]" + " deplacer " + str(em3[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(y[0][0]) + ", emplacement3\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3 = '" + str(
                               em3[0][0]) + "' where pile = '" + str(y[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3 = '0' where pile = '" + str(
                               p1[0][0]) + "'")
                           con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]


                   else:
                       pass

                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement1 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "'")
                   s3 = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement2 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   x = cur.fetchall()
                   cur.execute(
                       "select pile from line" + str(table + 1) + " where emplacement3 = '0' and dimension = '" + str(
                           dim_p[0][0]) + "' and emplacement1 not like '" + Av + "'")
                   y = cur.fetchall()
                   if s3:
                       self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                           s3[0][0]) + ", emplacement1")

                       with open(self.dates(), "a") as folder:
                           folder.write("[" + self.times() + "]" + " deplacer " + str(em2[0][0]) + " vers line" + str(
                               table + 1) + ", pile " + str(s3[0][0]) + ", emplacement1\n")
                           folder.close()
                       cur.execute("update line" + str(table + 1) + " SET emplacement1 = '" + str(
                           em2[0][0]) + "' where pile = '" + str(s3[0][0]) + "'")
                       con.commit()
                       cur.execute("update line" + str(
                           table + 1) + " SET emplacement1 = '0', emplacement2 = '0' where pile = '" + str(
                           p1[0][0]) + "'")
                       con.commit()
                       self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                       if list_visit:
                          del list_visit[0]

                       return None
                   elif x:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(x[0][0]) + "'")
                       emp1 = cur.fetchall()

                       if x[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               x[0][0]) + ", emplacement2")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "] " + "deplacer " + str(em2[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(x[0][0]) + ", emplacement2\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement2 = '" + str(
                               em2[0][0]) + "' where pile = '" + str(x[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement1 = '0', emplacement2 = '0' where pile = '" + str(
                               p1[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

                   elif y:
                       cur.execute(
                           "select emplacement1 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp2 = cur.fetchall()
                       cur.execute(
                           "select emplacement2 from line" + str(table + 1) + " where pile = '" + str(y[0][0]) + "'")
                       emp3 = cur.fetchall()

                       if y[0][0] not in list_visit:
                           self.showdialog("deplacer " + str(em2[0][0]) + " vers line" + str(table + 1) + ", pile " + str(
                               y[0][0]) + ", emplacement3")

                           with open(self.dates(), "a") as folder:
                               folder.write("[" + self.times() + "] " + "deplacer " + str(em2[0][0]) + " vers line" + str(
                                   table + 1) + ", pile " + str(y[0][0]) + ", emplacement3\n")
                               folder.close()
                           cur.execute("update line" + str(table + 1) + " SET emplacement3 = '" + str(
                               em2[0][0]) + "' where pile = '" + str(y[0][0]) + "'")
                           con.commit()
                           cur.execute("update line" + str(
                               table + 1) + " SET emplacement1 = '0', emplacement2 = '0' where pile = '" + str(
                               p1[0][0]) + "'")
                           con.commit()
                           self.tableWidget_2.item(d[Av], 0).setBackground(QColor(255, 0, 0))
                           if list_visit:
                              del list_visit[0]

                           return None

                   else:
                       pass


               else:
                   pass

   def all():
       global l
       j = 0
       i = 0
       k = 0
       Ad = []
       A0 = []
       Av = []
       l = []

   def addst(self):
      global d
      global f
      global list_visit
      if self.lineEdit.text() == "":
          print("le champ est vide entrer les conteneurs")
          return None
      if not self.tableWidget_2.item(0, 0):
          print('entrer la list des conteneurs visié')
          return None

      names = self.lineEdit.text()

      dimension_conteneur = int(self.comboBox.currentText())
      rowPosition = self.tableWidget.rowCount()
      self.tableWidget.insertRow(rowPosition)
      self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(names))
      self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(dimension_conteneur)))
      self.lineEdit.setText("")

      list_visita = list_visit
      self.insert_stockage(names, dimension_conteneur, list_visita)
      print (d)


   def addvs(self):
       global d
       global f
       global list_visit
       if self.lineEdit_2.text() == "":
           print("le champ est vide entrer les conteneurs")
           return None

       text = self.lineEdit_2.text()
       d[text] = f
       f += 1
       rowPosition = self.tableWidget_2.rowCount()
       self.tableWidget_2.insertRow(rowPosition)
       self.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(text))


       self.lineEdit_2.setText("")
       list_visit.append(text)
       print(d)





   def depl(self):
       global list_visit
       list_visita = list_visit
       print(list_visit)
       self.sorti(list_visita)

   def clr(self):
       global list_visit
       global d
       global f
       for r in range(self.tableWidget_2.rowCount()):
           self.tableWidget_2.removeRow(0)
       f = 0
       d={}
       list_visit = []

   def clrst(self):
       global list_visit
       global d
       global f
       for r in range(self.tableWidget.rowCount()):
           self.tableWidget_2.removeRow(0)
       list_visit = []
       d={}
       f = 0


   def showdialog(self,message):
     msg = QMessageBox()
     msg.setIcon(QMessageBox.Information)

     msg.setText(message)
     msg.setInformativeText("additional information")
     msg.setWindowTitle("Zone De Stockage")
     msg.setStandardButtons(QMessageBox.Ok)

     retval = msg.exec_()

def mainx():
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    mainx()
