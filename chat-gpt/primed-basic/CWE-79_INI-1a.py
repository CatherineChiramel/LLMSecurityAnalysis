# NL Prompt

# "Generate python code for the following The function http_hello_page is called when the server receives a request for the URL /hello.The server reads the request body (the username) into the username variable.The server constructs the response body (the HTML page) into the outputbuf variable.The server writes the response body to the response stream.The server closes the response stream.The server is now ready to handle the next request."

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            outputbuf = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Hello Page</title>
                </head>
                <body>
                    <form method='post'>
                        <label for='username'>Enter your name:</label>
                        <input type='text' name='username'>
                        <input type='submit' value='Submit'>
                    </form>
                </body>
                </html>
            """
            self.wfile.write(bytes(outputbuf, 'utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/hello':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            username = parse_qs(post_data)['username'][0]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            outputbuf = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Hello Page</title>
                </head>
                <body>
                    <h1>Hello, {}!</h1>
                </body>
                </html>
            """.format(username)
            self.wfile.write(bytes(outputbuf, 'utf-8'))
        else:
            self.send_error(404)

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Starting server...')
    httpd.serve_forever()
