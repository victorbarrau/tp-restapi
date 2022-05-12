from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from multiprocessing.spawn import import_main_path
from ariadne import gql,QueryType,MutationType,make_executable_schema,graphql_sync
from ariadne.constants import PLAYGROUND_HTML


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://root:root@localhost:5432/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# Create a GraphQL Playground UI for the GraphQL schema
@app.route("/graphql", methods=["GET"])
def graphql_playground():
   return PLAYGROUND_HTML

db=SQLAlchemy(app)

type_defs=gql(
    """
    type Query {
        movies:[Movie]
    }
    type Movie {
        id:ID!
        title:String!
        genre:String!
        lead_studio:String!
        audience_score:String!
        profitability:Float!
        rotten_tomatoes:Float!
        worldwide_gross:String!
        year:Int!
    }
"""
)

class Movie(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    genre=db.Column(db.String(100))
    lead_studio=db.Column(db.String(100))
    audience_score=db.Column(db.Integer())
    profitability=db.Column(db.Float())
    rotten_tomatoes=db.Column(db.Float())
    worldwide_gross=db.Column(db.Integer)
    year=db.Column(db.Integer())

    def __init__(self,title,genre,lead_studio,audience_score,profitability,rotten_tomatoes,worldwide_gross,year):

        self.title = title
        self.genre = genre
        self.lead_studio =lead_studio
        self.audience_score=audience_score
        self.profitability =profitability
        self.audience_score =audience_score
        self.worldwide_gross =worldwide_gross
        self.year =year


    def to_json(self):
        return{
            "id":self.id,
            "title":self.title,
            "lead_studio":self.lead_studio,
            "genre":self.genre,
            "audience_score":self.audience_score,
            "profitability":self.profitability,
            "worldwide_gross":self.worldwide_gross,
            "year":self.year,
         }


def populate_movies():
    with open("./movies.csv") as file:
        lines = file.readlines()
    for line in lines:
        print(lines)



if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    populate_movies()
    app.run(host='0.0.0.0', port=8080,debug=True)
