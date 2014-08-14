#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo 
# Data: 15/01/2014
# Versão: 2.0


import time
import os
import re
import random
from Classes.SMS import SMS
from Classes.checkFTP import CheckFTP
from Classes.readTXTFile import ReadTXTFile

qtdModem = 3
smsTelList = '/var/www/html/gammu/sendFiles/numeros'
messageFile = '/var/www/html/gammu/sendFiles/mensagem'
smsToSend = '/opt/SMSFactory/toSend/'
smsSended = '/opt/SMSFactory/sended/'

while True:
    time.sleep(3)
####Abrir Arquivos de texto
    telList = ReadTXTFile(smsTelList)
    message = ReadTXTFile(messageFile)
    if telList.getFileList() != [] and message.getFileList() != []:       
        text = re.sub('[\[\]\']','',str(message.readFileFromList()[0][1]))
        for phoneNumber in telList.getFileList():
            filetargetTel = os.path.join(telList.getFilePath(),phoneNumber)
	    for messageTxt in message.getFileList():	
		filetargetMes = os.path.join(message.getFilePath(),messageTxt)
#    	    print filetargetTel
#	    print filetargetMes

        for i in telList.readFileFromList():
            if i != []:
                for telefone in i:
		    filename = 'mensagem_'+ str(random.randint(100,100000)) + '.txt'
		    file = open(smsToSend+filename, 'a')
		    file.write(telefone+'\n'+text)
#		    print filename
#		    print telefone
#		    print text
		    file.close()
    try:
        telList.removeFileFromList(filetargetTel)
        message.removeFileFromList(filetargetMes)
    except:
        pass
