import tornado.web
import random
import os, os.path

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

accountData= {
    "alice" : {
        "name": "Alice Smith",
        "dateOfBirth": "January 1st",
        "email" : "alice@example.com",
        "image" : "alice.png"
    },

    "bob" : {
        "name": "Bob Jones",
        "dateOfBirth": "December 31st",
        "email" : "bob@bob.xyz",
        "image" : "bob.png"
    },

    "carol" : {
        "name": "Carol Ling",
        "dateOfBirth": "July 17th",
        "email" : "carol@example.com",
        "image" : "carol.png"
    },

    "dave" : {
        "name": "Dave N. Port",
        "dateOfBirth": "March 14th",
        "email" : "dave@dave.dave",
        "image" : "dave.png"
    }
}


class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        username = p.split("/")[2]
        realName = accountData [username]["name"]
        birthDate = accountData [username]["dateOfBirth"]
        email = accountData [username]["email"]
        profPic = accountData [username]["image"]

        self.render("Profile.html",
                    realName = realName,
                    birthDate = birthDate,
                    email = email,
                    profPic = profPic
                    )


 
