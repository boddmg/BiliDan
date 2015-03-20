#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib.parse
import re
import bilidan
import sys

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		request_url = self.requestline.split(" ")[1][1:]
		request_url = urllib.parse.unquote(request_url)
		if re.findall("av[0-9]+",request_url):
			print(request_url)
			sys.argv = sys.argv[:1]
			sys.argv.append(request_url)
			sys.argv.append("--source --html5")
			bilidan.main()

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()

