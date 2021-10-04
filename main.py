from bottle import template, run, get, post, request, redirect
import utilities
import socket
import os

HOSTname = socket.gethostname()
HOSTdir = os.getcwd()
STATICdir = os.path.join(HOSTdir, 'static')

WEBhost = "0.0.0.0"
WEBsrvr = 'cherrypy'
if HOSTdir == '/var/www':
    WEBport = '80'
    HOSTurl = 'NewFeatures'
else:
    WEBport = '8080'
    HOSTurl = 'http://localhost:8080'


@get('/')
def home():
    home_template = 'templates/homepage.tpl'
    data, chart = utilities.db_call()
    return template(home_template, data=data, chart=chart)


@post('/submit')
def submit():
    a = request.forms.allitems()
    rows = dict(a)
    utilities.db_insert(rows)
    redirect('/')


@post('/delete')
def delete():
    a = request.forms.allitems()
    rows = dict(a)
    utilities.db_insert(rows)
    redirect('/')


# Web Server Start and Database initial build
if __name__ == '__main__':
    utilities.database_reset()
    serverurl = 'http://localhost:8080'
    print(HOSTurl)
    run(host=WEBhost, server=WEBsrvr, port=WEBport, debug=True)
