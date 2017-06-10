import datetime
import sys
import sqlite3
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#bluetooth modules
import bluetooth

#espeak module
from espeak import espeak



class databaseconfig(object):

    def createConnection(self):
        connection = sqlite3.connect('/home/pi/django/mysite/mydatabase.db')
        if connection:
            return connection


    def createTable(self):
        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE Announcement(Id INTEGER PRIMARY KEY AUTOINCREMENT, Message TEXT)")
        connection.commit()

    def insertintotable(self,message,date):
        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Announcement(Message,DATE) VALUES(?,?)",(message,date))
        connection.commit()



def home(request):
    datatosend = dict()
    dt = datetime.datetime.now()
    datatosend['datetime'] = dt
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    dbconfig = databaseconfig()
    #dbconfig.createTable()
    
    port = 1
    server_socket.bind(("",port))
    server_socket.listen(1)

    client_socket,address = server_socket.accept()
    print "Accepted Connection from: ",address

    #add espeak module that prompts device connected successfully
    espeak.synth("Speak   Your   Message!")


    while 1:
        data = client_socket.recv(1024)
        print("Received data: %s"%data)

        #Insert Message into Table
        dbconfig.insertintotable(data,dt)

        connection=dbconfig.createConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT Id,Message,DATE FROM Announcement ORDER BY Id DESC")

        datatosend['announcements']=cursor.fetchall()

        datatosend['voicedata'] = data

        # add espeak module that prompts data send Successfully
        espeak.synth("Message   Send    Successfully!")

        #client_socket.close()
        #server_socket.close()

        html = get_template('index.html').render(Context(datatosend))
        return HttpResponse(html)
