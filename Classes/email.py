# -*- coding: iso-8859-1 -*-
import smtplib

class EMAIL:
    def __init__(self):
        try:
	    self.newEmail = smtplib.SMTP('mail.redeconekta.com.br',587)
	    self.newEmail.login('sms@redeconekta.com.br','Saa1muR1vae2fou')
	except:
	    print "Não foi possivel autenticar no email!"


    def sendMessage(self,email, message):
	newMessage = '''Subject: Novo SMS recebido'''+'\n'+ message 
	#try:
	self.newEmail.sendmail('sms@redeconekta.com.br',email,newMessage)
	#except:
	#    print "Não foi possivel enviar o email!"
