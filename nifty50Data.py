
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
        conn = redis.Redis(host="pub-redis-13650.us-east-1-2.1.ec2.garantiadata.com", port=13650, password="redis1234")
        data = conn.get("nifty50Data")        
        return data
