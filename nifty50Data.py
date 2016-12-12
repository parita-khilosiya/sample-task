
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

    # def POST(self, length=8):
    #     some_string = ''.join(random.sample(string.hexdigits, int(length)))
    #     cherrypy.session['mystring'] = some_string
    #     return some_string

    # def PUT(self, another_string):
    #     cherrypy.session['mystring'] = another_string

    # def DELETE(self):
    #     cherrypy.session.pop('mystring', None)

