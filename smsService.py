#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo 
# Data: 15/01/2014
# Versão: 2.0


import time
import os
from Classes.SMS import SMS
from Classes.checkFTP import CheckFTP
from Classes.readTXTFile import ReadTXTFile
from Classes.dbSMS import DBSMS

qtdModem = 2
toSendDir = '/opt/SMSFactory/toSend'
sendedDir = '/opt/SMSFactory/sended/'
errorDir = '/opt/SMSFactory/error/'

while True:
    time.sleep(10)
####Abrir Arquivos de texto
    fileSpool = ReadTXTFile(toSendDir)
    fileList = []
    if fileSpool.getFileList() != []:       
#	    print fileList
#### Envia SMS a partir dos arquivos  
    	chipIDLST = ReadTXTFile('/opt/SMSFactory/chip/')
        chipIDSTR = (chipIDLST.readFileFromList()[0])
        chipIDINT = int(chipIDSTR[1])
        for fileContent in fileSpool.readFileFromList():
	    if fileContent != []:
               if chipIDINT >= qtdModem:
                      chipIDINT = 0
               newSMS = SMS(fileContent[1],fileContent[2])
               try:
	       	      newSMS.sendSMS(chipIDINT)
		      try:
			newDB = DBSMS();
			newDB.insertSentSMS(newSMS.getNumber(),newSMS.getMessage(),"smsService.py")
		      except:
			print "Não foi possivel inserir o dado no banco."
            	      try: 
	       		fileSpool.moveFileFromList(fileContent[0],sendedDir)
	    	      except:
	       		fileSpool.removeFileFromList(fileContent[0])
	       except:
		      print "Erro no arquivo: "+fileContent[0]+" numero: "+fileContent[1]+" Conteudo: "+fileContent[2]
               chipIDINT = chipIDINT + 1
	       chipIDLST.writeFileFromList(chipIDLST.getFileList()[0], str(chipIDINT))
	       
