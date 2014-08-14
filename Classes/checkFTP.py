#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
from ftplib import FTP

class CheckFTP:
    def __init__(self,remotehost,ftpuser,ftppass,localpath,remotepath):
        self.remotehost = remotehost
        self.ftpuser = ftpuser
        self.ftppass = ftppass
        self.localpath = localpath
        self.remotepath = remotepath
        
    def getRemoteHost(self):
        return self.remotehost
    
    def getFtpUser(self):
        return self.ftpuser
    
    def getFtpPass(self):
        return self.ftppass
    
    def getLocalPath(self):
        return self.localpath
    
    def getRemotePath(self):
        return self.remotepath
    
    
    def downloadFiles(self):
        remoteFileList = []
        fileName = ''
        try:       
            remoteFTP = FTP(self.remotehost)
            remoteFTP.login (self.ftpuser,self.ftppass)
            remoteFTP.retrlines('NLST', remoteFileList.append)
            if remoteFileList != []:                    
                for i in remoteFileList:
                    fileName = i.strip('')
                    try:
                        localFilePath = os.path.join(self.getLocalPath(),fileName)
                        getFile = open(localFilePath,'wb')
                        remoteFTP.retrbinary("RETR " + fileName, getFile.write)
                        getFile.close()
                        remoteFTP.delete(fileName)
                    except:
                        pass
            remoteFTP.timeout
        except:
            pass
        try:
            remoteFTP.quit()
        except:
            pass
