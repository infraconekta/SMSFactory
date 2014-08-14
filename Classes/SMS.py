#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import re
import gammu

class SMS:
    def __init__(self,phonenumber,textmessage):
        self.phonenumber = str(''.join(re.findall('\d', phonenumber)))
        self.textmessage = str(textmessage).rstrip('\r\n')
    
    def getNumber(self):
        return self.phonenumber
    
    def getMessage(self):
        return self.textmessage
    
    def  sendSMS(self,chipID):
        sm = gammu.StateMachine()
        sm.ReadConfig(chipID)
        sm.Init()
        message = {
                   'Text': self.getMessage(),
                   'SMSC': {'Location': 1},
                   'Number': self.getNumber(),
                 }
        sm.SendSMS(message)
    
    def readSMS(self,chipID):
	sm = gammu.StateMachine()
	sm.ReadConfig(chipID)
	sm.Init()
	return sm.GetNextSMS(Start = True, Folder = 0)
     
    def deleteSMS(self,chipID,location):
	sm = gammu.StateMachine()
	sm.ReadConfig(chipID)
	sm.Init()
	sm.DeleteSMS(0,location)

    def getSMSStatus(self,chipID):
	sm = gammu.StateMachine()
        sm.ReadConfig(chipID)
        sm.Init()
	return sm.GetSMSStatus()
