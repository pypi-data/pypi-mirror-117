import tornado.ioloop
import tornado.web
from tornado.escape import json_decode 
import json

class NNRunner:
    def run(self, port=80):
        app = make_app()
        app.listen(port)
        tornado.ioloop.IOLoop.current().start()

class MainHandler(tornado.web.RequestHandler):
    parsed_body = None

    # def prepare(self):
    #     data = json_decode(self.request.body)
    #     # TODO: validation
    #     self.parsed_body = data

    def get(self):
        self.write("Hello, pidor")
    
    def post(self):
        print("self.parsed_body: ", self.parsed_body)

        self.write("wtf")

def make_app():
    return tornado.web.Application([
        (r"/api/v1/process", MainHandler),
    ])
