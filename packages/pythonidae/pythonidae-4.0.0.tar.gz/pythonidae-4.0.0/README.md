
# Pythonidae
Pythonidae is Fast, minimalist web framework for [Python](https://www.python.org)
![Pythonidae](https://raw.githubusercontent.com/thehelkaproject/pythonidae/master/test_app/pythonidae.png)

  
  ## 'Hello, World!' Application
	
```	
from pythonidae import Pythonidae, Path, HttpResponse
		
app = Pythonidae()
		
def helloWorld(req):
		return  HttpResponse(req, '<h1>Hello, World!</h1>', content_type='text/html')

app_routes = [
	Path('/', helloWorld)
]
		
app.set_routes(app_routes)

# Only Development Not Use Production
from wsgiref.simple_server import make_server	
make_server('localhost', 8000, app).serve_forever()
```

## 'Simple Rest API' Application

```
from pythonidae import Pythonidae, Path, JsonResponse

app = Pythonidae()

def helloWorld(req):

return JsonResponse(req, {
	'user':  'thehelkaproject',
	'github':  'https://github.com/thehelkaproject'
})

app_routes = [
	Path('/', helloWorld)
]

app.set_routes(app_routes)

# Only Development Not Use Production
from wsgiref.simple_server import make_server
make_server('localhost', 8000, app).serve_forever()
```

### Contributing
#### [github](https://github.com/thehelkaproject/pythonidae)

### License
[Python License](https://raw.githubusercontent.com/thehelkaproject/pythonidae/master/python.licence)
[Pythonidae License](https://raw.githubusercontent.com/thehelkaproject/pythonidae/master/pythonidae.licence)

![python powered](https://www.python.org/static/community_logos/python-powered-w-200x80.png)
