
import cherrypy
import redis


class Nifty50Diplay(object):
    @cherrypy.expose
    def index(self):
        return open("public/index.html")


@cherrypy.expose
class Nifty50WebService(object):

    # @cherrypy.tools.accept(media='text/json')
    def GET(self):
        conn = redis.Redis('localhost')
        data = conn.get("nifty50Data")        
        return data
