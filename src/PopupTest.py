import tornado.web
import random
import os, os.path

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)



class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path

        self.render("PopupTest.html")
