import tornado.web
import random

accountData= {
    "alice" : {
        "name": "Alice Smith",
        "dateOfBirth": "January 1st",
        "email" : "alice@example.com"
    },

    "bob" : {
        "name": "Bob Jones",
        "dateOfBirth": "December 31st",
        "email" : "bob@bob.xyz"
    },

    "carol" : {
        "name": "Carol Ling",
        "dateOfBirth": "July 17th",
        "email" : "carol@example.com"
    },

    "dave" : {
        "name": "Dave N. Port",
        "dateOfBirth": "March 14th",
        "email" : "dave@dave.dave"
    }
}


class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        username = p.split("/")[2]
        realName = accountData [username]["name"]
        birthDate = accountData [username]["dateOfBirth"]
        email = accountData [username]["email"]

        self.render("Profile.html",
                    realName = realName,
                    birthDate = birthDate,
                    email = email
                    )


 
