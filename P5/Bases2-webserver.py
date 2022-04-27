import http.server
import socketserver
import termcolor
import pathlib

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)

        path = self.requestline.split(" ")[1] #ES LO MISMO QUE EN P4 PERO EN VEZ DE ROUTE, AQUÍ ES PATH
        if path == "/":
            contents = pathlib.Path("index.html").read_text()
        #try:
            #if path == "/info/A":
            #contents = pathlib.Path("info/A.html").read_text()
        #elif path == "/info/C":
            #contents = pathlib.Path("info/C.html").read_text()
        #elif path == "/info/G":
            #contents = pathlib.Path("info/G.html").read_text()
        #TIENES QUE PONER QUE SI PONES UN FILENAME QUE EXISTA, LO ABRA. SI NO EXISTE, SE ABRE EL ERROR. #contents = read_html_file(path[1:] + ".html")
        else:
            contents = pathlib.Path("ERROR.html").read_text()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

#coger el 2.2
#answer part of the server 2.3
#if cmd == nseq, hacer nseq