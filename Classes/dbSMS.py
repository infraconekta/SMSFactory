#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import MySQLdb
import time
class DBSMS:
    def __init__(self):
	try:
	    self.dataBase=MySQLdb.connect("localhost","root","","smsdPy")
	    self.cursor = self.dataBase.cursor()
	except:
	    print "Erro ao conectar a base de dados."

    
    def insertSentSMS(self, phoneNumber, textMessage, systemID):
	insertDate = "'"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"'"
	phoneNumber = "'"+phoneNumber+"'"
	textMessage = "'"+textMessage+"'"
	systemID = "'"+systemID+"'"
	self.cursor.execute("""SELECT max(id) FROM sentitems""")
	lastId = self.cursor.fetchone()
	id = int(lastId[0])+ 1
	self.dataBase.query("""INSERT INTO sentitems (InsertIntoDB, SendingDateTime, DestinationNumber, TextDecoded,ID, creatorID) VALUES (%s,%s,%s,%s,%s,%s)""" % (insertDate, insertDate, phoneNumber, textMessage,id, systemID))

    def insertReadSMS(self, receivingDate, senderNumber, receivedNumber, textMessage):
	receivingDate = "'"+str(receivingDate)+"'"
	senderNumber = "'"+senderNumber+"'"
	receivedNumber = "'"+receivedNumber+"'"
	textMessage = "'"+textMessage+"'"
	self.cursor.execute("""SELECT max(id) FROM inbox""")
	lastId = self.cursor.fetchone()
	id = int(lastId[0])+ 1
	self.dataBase.query("""INSERT INTO inbox (ReceivingDateTime,SenderNumber, SMSCNumber, TextDecoded, ID, Processed) VALUES (%s,%s,%s,%s,%s,%s)""" % (receivingDate,senderNumber,receivedNumber,textMessage,id,"'false'"))
    
    def selectReadSMS(self):
	smsList = [[]]
	self.cursor.execute("""SELECT SenderNumber, TextDecoded, id FROM inbox WHERE Processed = 'false'""")
	smsList = self.cursor.fetchall()
	return smsList

    def updateReadSMS(self,idSms):
	self.dataBase.query("""UPDATE inbox SET Processed = 'true' WHERE id = %s""" % idSms)
