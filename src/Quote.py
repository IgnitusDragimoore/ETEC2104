import tornado.web
import random

quotes = [
    "The only thing we have to fear is fear itself. And big hairy spiders.",
    "Fourscore and seven years ago was eighty seven years ago.",
    "We the People of the United States are the people of the Untied Skates."
]
class Handler(tornado.web.RequestHandler):
    def get(self):
        q = random.choice(quotes)
        self.write(
            f'<img src="/static/quotationmarks.png"><br>{q}'
        )
