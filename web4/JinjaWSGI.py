from wsgiref import simple_server
from jinja2 import Environment, FileSystemLoader

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
    env = Environment(loader=FileSystemLoader("C:\\Users\\Алена\Desktop\5к\WEB\web1\git\webProgramming\web4"))
    status = "404 Not Found"
    template =['File not found.']
    title = link1 = link2 = ""
    path = environ['PATH_INFO']
    if path == "/index.html" or path == "/":
        status = "200 OK"
        title = "Task4Index"
        link1='<a href="about\\aboutme.html"> link2 </a>'
        link2 ='<a href="C:\\Users\\Алена\Desktop\5к\WEB\web1\git\webProgramming\web4\\about\\aboutme.html">'
        template = env.get_template('/index.html')
    elif path == "/about/aboutme.html":
        status = "200 OK"
        title='Task4Anoutme'
        link1='<a href="..\index.html"> link </a>'
        link2 ='<a href="C:\\Users\\Алена\Desktop\5к\WEB\web1\git\webProgramming\web4\index.html">"'
        template = env.get_template('about/aboutme.html')
    print(template)
    start_response(status, [('Content-Type', 'text/html; charset=utf-8')])
    return [template.render(title = title, link1 = link1, link2 = link2).encode('utf-8')]

server = simple_server.WSGIServer(
            ('localhost', 8080),
            simple_server.WSGIRequestHandler,
        )
app = Middleware(simple_app)
server.set_app(app)
server.serve_forever()