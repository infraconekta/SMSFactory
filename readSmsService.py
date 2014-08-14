#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo
# Data: 11/08/2014
# Versão: 2.0


import time
import os
from Classes.SMS import SMS
from Classes.dbSMS import DBSMS

while True:
    time.sleep(120)
    qtdChip = 2
    for chipID in range(0,qtdChip):
            newSMS = SMS('23423423423','dfsfdgsdfgsdfgsd')
            try:
                qtdSMS = int(newSMS.getSMSStatus(chipID)['SIMUsed'])
            except:
                print "Erro ao receber o status do modem."
            if qtdSMS > 0:
	       try:
		   sms = newSMS.readSMS(chipID)
                   smsData =  sms[0]
                   dataRecebimento =  smsData['SMSCDateTime']
                   numeroEnviou = smsData['Number']
                   numeroRecebeu = smsData['SMSC']['Number']
                   mensagem = smsData['Text']
                   location = smsData['Location']
                   newDBSMS = DBSMS()
                   newDBSMS.insertReadSMS(dataRecebimento,numeroEnviou,numeroRecebeu,mensagem)
	       except:
		   print "Nao foi possivel ler o SMS."
               newSMS.deleteSMS(chipID,location)
