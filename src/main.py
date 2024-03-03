import asyncio
import os, os.path
import tornado.web
import Sock
import Index, Quote, TemplateTest, Profile, Roulette

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href='/roulette.html'>The Casino is Live!</a>")


def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/quote",Quote.Handler),
        ("/fancy",TemplateTest.Handler),
        ("/profile/.*",Profile.Handler),
        ("/roulette",Roulette.Handler),
        ("/sock",Sock.Handler)
    ]
    app = tornado.web.Application(
        endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()