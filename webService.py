#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo
# Data: 11/08/2014
# Versão: 2.0

import SimpleHTTPServer
import SocketServer
import logging
import cgi
import random
import sys
import urlparse
import re

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = ""
else:
    PORT = 8000
    I = ""


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
	#getReceived = SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
	#SimpleHTTPServer.SimpleHTTPRequestHandler.parse_request()
	smsToSend = '/opt/SMSFactory/toSend/' 
	o = urlparse.urlparse(self.path)
        dados = urlparse.parse_qs(o.query)
	telefone = re.sub('[\[\]\']','',str(dados['Celular']))
	text =  re.sub('[\[\]\']','',str(dados['Mensagem']))
	filename = 'mensagem_'+ str(random.randint(100,10000)) + '.txt'
        file = open(smsToSend+filename, 'a')
        file.write(telefone+'\n'+text)
        file.close()
	#print celular
	#print mensagem
	#print dados
    def do_POST(self):
	smsToSend = '/opt/SMSFactory/toSend/' 
	postContent = []
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
	if "NumUsu" and "Senha" and "SeuNum" and "Celular" and "Mensagem" in form:
	    for item in form.list:
	        postContent.append(item.value)
	#print postContent
	telefone = postContent[3]
	text = postContent[4]
	filename = 'mensagem_'+ str(random.randint(100,10000)) + '.txt'
	file = open(smsToSend+filename, 'a')
	file.write(telefone+'\n'+text)
	file.close()

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

#print "Serving at: http://%(interface)s:%(port)s" % dict(interface=I or "localhost", port=PORT)
httpd.serve_forever()
