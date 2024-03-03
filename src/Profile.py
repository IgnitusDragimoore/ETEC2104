import tornado.web
import os, os.path
import json
import base64

HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)

accountData= {
    "alice" : {
        "firstName": "Alice",
        "lastName" : "Smith",
        "dateOfBirth": "January 1st",
        "email" : "alice@example.com",
        "image" : "alice.png"
    },

    "bob" : {
        "firstName": "Bob",
        "lastName":  "Jones",
        "dateOfBirth": "December 31st",
        "email" : "bob@bob.xyz",
        "image" : "bob.png"
    },

    "carol" : {
        "firstName": "Carol",
        "lastName":  "Ling",
        "dateOfBirth": "July 17th",
        "email" : "carol@example.com",
        "image" : "carol.png"
    },

    "dave" : {
        "firstName": "Dave",
        "lastName": "N. Port",
        "dateOfBirth": "March 14th",
        "email" : "dave@dave.dave",
        "image" : "dave.png"
    }
}


class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path

        username = p.split("/")[2]
        firstName = accountData [username]["firstName"]
        lastName = accountData [username]["lastName"]
        birthDate = accountData [username]["dateOfBirth"]
        email = accountData [username]["email"]
        profPic = accountData [username]["image"]

        self.render("Profile.html",
                    user = username,
                    firstName = firstName,
                    lastName = lastName,
                    birthDate = birthDate,
                    email = email,
                    profPic = profPic
                    )

    def post(self):
        J=json.loads(self.request.body)
        firstName = J["firstName"]
        lastName = J["lastName"]
        dob = J["birthDate"]
        image = base64.b64decode(J["ppic"])
        print("WE GOT:",firstName,lastName,dob,image[:20])
        resp={"ok": True}
        self.write( json.dumps(resp) )
        
        requestBody = tornado.escape.json_decode(self.request.body)
        # Decode binary content from base64
        binary_data = base64.b64decode(requestBody[fileContent])
        # Open file in binary mode
        with open(requestBody["fileName"], "wb") as f:
            f.write(binary_data)