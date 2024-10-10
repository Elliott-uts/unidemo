import http.server
import socketserver
from urllib.parse import parse_qs
from control.cli.admin_control import AdminControl
from control.cli.student_control import StudentControl

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.admin_control = AdminControl()
        self.student_control = StudentControl()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = 'template/index.html'  # Serve the HTML file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])  # Get the size of the data
            post_data = self.rfile.read(content_length)  # Read the data
            data = parse_qs(post_data.decode('utf-8'))
            option = data.get('option', [''])[0].upper()  # Extract the option field

            # Handle different options
            response = ""
            if option == 'A':
                response = self.admin_control.show_admin_main_menu()  # Call admin menu
            elif option == 'S':
                response = self.student_control.show_student_main_menu()  # Call student menu
            elif option == 'X':
                response = "Thank You"
            else:
                response = "Incorrect input, please try again."

            # Create a simple response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"<html><body><h1>{response}</h1></body></html>".encode('utf-8'))

PORT = 8080

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
