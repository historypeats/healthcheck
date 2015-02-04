#!/usr/bin/env python

#
#	Author: historypeats <msantillana@2u.com>
#	Description: This is a quick webserver/app that provides a healthcheck functionality
#

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# GLOBAL CONFIG
PORT = 7777
PING_URI = '/ping'
SERVER_NAME = '2U'

class webHandler(BaseHTTPRequestHandler):
	''' This is a web handler object. 
		This handles the web request made to the server

	'''
	
	global PING_URI, SERVER_NAME

	def do_GET(self):
		''' Define the GET method'''

		# We only want to respond to our PING_URI.
		# Example: server.com/ping
		if self.path == PING_URI:
			self.send_response(200)
			self.send_header('Content-type','custom/API')
			self.send_header('Server', SERVER_NAME)
			self.end_headers()

			# Retrieve the Location header from request
			self.location = self.headers['Location']
			
			# Return response with location header
			self.wfile.write(self.location)
			
			return


def main():
	''' Main '''

	global PORT

	try: 
		print "[+] Starting server on port {0}".format(PORT)
		server = HTTPServer(("", PORT), webHandler)
		server.serve_forever()
	
	except KeyboardInterrupt:
		print "[+] Pressed ^C, closing server"
		server.socket.close()
	
	except:
		print '[!] Unknown error occured'
		server.socket.close()


if __name__ == '__main__':
	main() 