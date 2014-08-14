#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import mimetypes
import shutil

class ReadTXTFile:
    def __init__(self,filepath):
        self.filepath = str(filepath)
        self.filelist = os.listdir(filepath)

    def getFilePath(self):
        return self.filepath
    
    def getFileList(self):
        return self.filelist
    
    
    def setFilePath(self,filepath):
        self.filepath = filepath
    
    def setFileList(self,filelist):
        self.filelist = filelist



    def readFileFromList(self):
        listfilecontent = []
        for fileName in self.filelist:
            filecontent = []
            src_file = os.path.join(self.getFilePath(), fileName)
            if mimetypes.guess_type(src_file)[0] == "text/plain":
                filetarget = open(src_file,'r')
		filecontent.append(src_file.rstrip('\r\n'))
                for i in filetarget:
                        filecontent.append(i.rstrip('\r\n'))
                listfilecontent.append(filecontent)
                filetarget.close()
      
            else:
                os.remove(src_file)
        return listfilecontent
    
    def removeFileFromList(self,filename):
        fileToRemove = os.path.join(self.getFilePath(),filename)
        os.remove(fileToRemove)
    
    def moveFileFromList(self,src_dir, dst_dir):
        shutil.move(src_dir, dst_dir)
        
    
    def writeFileFromList(self,filetarget,textcontent):
        src_file = os.path.join(self.getFilePath(), filetarget)
        if mimetypes.guess_type(src_file)[0] == "text/plain":
                filetarget = open(src_file,'w')
                filetarget.write(str(textcontent))
                filetarget.close()
        else:
            os.remove(src_file)
        
