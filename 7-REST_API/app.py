from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
import random

app = Flask(__name__)
api = Api(app)

class foo(Resource):
    def get(self):
        return {"foo" : "bar"}

categories = {"programming", "dark", "pun"}

jokes = {
    1 : {"category" : "programming", "joke" : "Why did the Python programmer not respond to the foreign mails he got? ----> Because his interpreter was busy collecting garbage."},
    2 : {"category" : "programming", "joke" : "The glass is neither half-full nor half-empty, the glass is twice as big as it needs to be."},
    3 : {"category" : "programming", "joke" : "If Bill Gates had a dime for every time Windows crashed ... Oh wait, he does."},
    4 : {"category" : "dark", "joke" : "I was going to tell a dead baby joke. But I decided to abort."},
    5 : {"category" : "dark", "joke" : "Stop being homophobic and rude to the LGBTQ+ community. You should be thanking them for saving us plenty of room in heaven."},
    6 : {"category" : "dark", "joke" : "I didn't vaccinate my 10 kids and the one that survived is fine!"},
    7 : {"category" : "pun", "joke" : "To whoever stole my copy of Microsoft Office, I will find you. You have my Word!"},
    8 : {"category" : "pun", "joke" : "Oysters hate to give away their pearls because they are shellfish."}
}

joke_put_args = reqparse.RequestParser()
joke_put_args.add_argument("id", type=int, help="Please provide a id", required=True)
joke_put_args.add_argument("category", type=str, help="Please provide a category", required=True)
joke_put_args.add_argument("joke", type=str, help="Please provide a joke", required=True)

class joke(Resource):
    def get(self,category):
        if category == "any":
            id = random.choice(list(jokes))
            return jokes[id]
        elif category in categories:
            temp = []
            for i in jokes:
                if jokes[i]["category"] == category:
                    temp.append(jokes[i])
            if len(temp) == 0:
                abort(200, message="Currently no jokes of the given category available.")                
            return random.choice(temp)

        else :
            abort(404, message="Given category does not exist.")
    def put(self,category):
        args = joke_put_args.parse_args()
        jokes[args["id"]] = {"category" : args["category"], "joke" : args["joke"]}
        return args

class jokebyid(Resource):
    def get(self,id):
        if id in jokes:
            return jokes[id]
        else :
            abort(404, message="Joke with given id does not exist.")

api.add_resource(foo, "/foo")
api.add_resource(joke, "/joke/<string:category>")
api.add_resource(jokebyid, "/jokebyid/<int:id>")

if __name__ == "__main__":
    app.run(debug = True)