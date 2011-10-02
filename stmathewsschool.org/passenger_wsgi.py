# Using paste
import sys, os
cwd = os.getcwd()
myapp_directory = cwd + '/stmathews'
sys.stdout = sys.stderr
sys.path.insert(0,myapp_directory)
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "stmathews.settings"
from paste.exceptions.errormiddleware import ErrorMiddleware
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
 # To cut django out of the loop, comment the above application = ... line ,
 # and remove "test" from the below function definition.
def testapplication(environ, start_response):
	status = '200 OK'
	output = 'Hello World! Running Python version ' + sys.version + '\n\n'
	response_headers = [('Content-type', 'text/plain'),
				('Content-Length', str(len(output)))]
   # to test paste's error catching prowess, uncomment the following line
   # while this function is the "application"
   #raise("error")
	start_response(status, response_headers)    
	return [output]
application = ErrorMiddleware(application, debug=True)

# normal method - 500 internal error
#import sys, os
#sys.path.append('~/stmathewsschool.org/')

# virtualenv method
#INTERP = "/home/davkutalek/local/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path
#if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)


#os.environ['DJANGO_SETTINGS_MODULE'] = "stmathews.settings"
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

# test method
#def application(environ, start_response):
#    start_response('200 OK', [('Content-type', 'text/plain')])
#    return ["Hello, world!"]
