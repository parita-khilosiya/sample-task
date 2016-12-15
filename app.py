import cherrypy
import os
from nifty50Data import *
# from getData import *
from threading import Thread


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/getdata': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/json')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    # background_thread = Thread(target=scrapData)
    # background_thread.start()

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': process.env.PORT || 8080})


    webapp = Nifty50Diplay()
    webapp.getdata = Nifty50WebService()
    cherrypy.quickstart(webapp, '/', conf)
