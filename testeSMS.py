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
from Classes.email import EMAIL
qtdChip = 2
for chipID in range(0,qtdChip):
	newSMS = SMS('23423423423','dfsfdgsdfgsdfgsd')
	qtdSMS = int(newSMS.getSMSStatus(chipID)['SIMUsed'])
	if qtdSMS > 0:
   	   sms = newSMS.readSMS(chipID)
   	   dicionario =  sms[0]
   	   dataRecebimento =  dicionario['SMSCDateTime']
   	   numeroEnviou = dicionario['Number']
   	   numeroRecebeu = dicionario['SMSC']['Number']
   	   mensagem = dicionario['Text']
   	   location = dicionario['Location']
   	   newDBSMS = DBSMS()
   	   newDBSMS.insertReadSMS(dataRecebimento,numeroEnviou,numeroRecebeu,mensagem)
   	   newSMS.deleteSMS(chipID,location)
