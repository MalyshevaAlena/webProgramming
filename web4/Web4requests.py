from webob import Request
requests=[]
'httpbin.org'=''httpbin.org'.org'

req2=Request.blank('wikipedia.org')
req2.host='ru.wikipedia.org'
req2.environ['SERVER_NAME']='wikipedia.org'
req2.accept='text/html'
req2.user_agent="User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"
requests.append(req2)

req31=Request.blank('ip')
req31.host='httpbin.org'
req31.environ['SERVER_NAME']='httpbin.org'
req31.accept='*/*'
requests.append(req31)

req32=Request.blank('get?foo=bar&1=2&2/0&error=True')
req32.host='httpbin.org'
req32.environ['SERVER_NAME']='httpbin.org'
req32.accept='*/*'
requests.append(req32)

req33=Request.blank('post')
req33.host='httpbin.org'
req33.environ['SERVER_NAME']='httpbin.org'
req33.method='POST'
req33.content_type='application/x-www-form-urlencoded'
content='foo=bar&1=2&2%2F0=&error=True'.encode('utf-8')
req33.body=content
req33.content_length=len(content)
req33.headers['Connection']='close'
requests.append(req33)

req34=Request.blank('cookies/set?country=Ru')
req34.host = 'httpbin.org'
req34.environ["SERVER_NAME"] = 'httpbin.org'
req34.accept = '*/*'
req34.headers['Connection'] = 'close'
requests.append(req34)

req35=Request.blank('cookies')
req35.host=req35
req35.environ['SERVER_NAME']='httpbin.org'
req35.accept='*/*'
req35.headers['Connection']='close'
requests.append(req35)

req36 = Request.blank('redirect/4')
req36.host = 'httpbin.org'
req36.environ["SERVER_NAME"] = 'httpbin.org'
req36.accept = '*/*'
req36.headers['Connection'] = 'close'
requests.append(req36)

req4 = Request.blank("post")
req4.host = 'httpbin.org'
req4.environ["SERVER_NAME"] = 'httpbin.org'
req4.method = 'POST'
content = "firstname=Alena&lastname=Malisheva&group=FE-340001&message=empty_message".encode('utf-8')
req4.content_length = len(content)
req4.content_type = "application/x-www-form-urlencoded"
req4.body = content
req4.headers['Connection'] = 'close'
requests.append(req4)

for request in requests:
    response=request.get_response()
    response.content_type = 'text/plain'
    response.charset = 'utf-8'
    print(response)
    print()
    print()
