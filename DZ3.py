from wsgiref import simple_server

class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        top = "<div class='top'>Middleware TOP</div>\n"
        bottom = "<div class='botton'>Middleware BOTTOM</div\n"
        page = self.app(environ, start_response).decode("utf-8")
        result = ""
        index_endbody_start = page.find("</body>")
        index_body_end = page.rfind("<body>")
        start = page[:index_body_end]
        flesh = page[index_body_end:index_endbody_start]
        end = page[index_endbody_start:]
        result += start + top + flesh + bottom + end
        return [result.encode("utf-8")]

def simple_app(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]
    result = ""
    path = environ['PATH_INFO']
    if path == "/index.html" or path == "/about/aboutme.html":
        start_response(status, response_headers)
        result = open(path[1:]).read().encode('utf-8')
    else:
        start_response("404 Not Found", response_headers)
    return result

server = simple_server.WSGIServer(
            ('localhost', 8080),
            simple_server.WSGIRequestHandler,
        )
app = Middleware(simple_app)
server.set_app(app)
server.serve_forever()
