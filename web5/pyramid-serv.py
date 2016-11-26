from jinja2 import Environment, FileSystemLoader
from pyramid.config import Configurator
from wsgiref.simple_server import make_server
from pyramid.response import Response

env = Environment(loader=FileSystemLoader("C:\\Users\\Алена\Desktop\webProgramming\web5"))
link1 = link2 = ""

def index(request):
    link1='<a href="about\\aboutme.html"> link to index </a>'
    link2 ='<a href="C:\\Users\\Алена\Desktop\webProgramming\web5\\about\\aboutme.html">'
    template = env.get_template('/index.html')
    return Response(template.render(link1 = link1, link2 = link2))

def about(request):
    link1='<a href="..\index.html"> link to aboutme </a>'
    link2 ='<a href="C:\\Users\\Алена\Desktop\webProgramming\web5\index.html">'
    template = env.get_template('about/aboutme.html')
    return Response(template.render(link1 = link1, link2 = link2))

def main():
    config = Configurator()
    config.add_route('index_page', '/index.html')
    config.add_view(index, route_name='index_page')
    config.add_route('about_page', '/about/aboutme.html')
    config.add_view(about, route_name='about_page')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

if __name__ == "__main__":
    main()