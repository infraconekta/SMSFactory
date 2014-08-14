#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo 
# Data: 15/01/2014
# Versão: 2.0


import time
from Classes.dbSMS import DBSMS
from Classes.email import EMAIL

while True:
   time.sleep(30)
   newCon = DBSMS()
   for newReceivedSMS in newCon.selectReadSMS():
      if newReceivedSMS != []:
   	   email = EMAIL()
   	   numero =  newReceivedSMS[0]
   	   text = newReceivedSMS[1]
   	   id = int(newReceivedSMS[2])
   	   mensagem = '\nNumero: '+ numero +'\nMensagem:'+ text
	   try:
   	       email.sendMessage('infra@redeconekta.com.br',mensagem)
	       try:
	           newCon.updateReadSMS(id)
	       except:
                   print "Não foi possivel atualizar a base de dados."
	   except:
	       print "Não foi possivel enviar o email"
