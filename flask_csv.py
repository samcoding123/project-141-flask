from flask import Flask, jsonify, request
import csv

all_movies=[]
with open ('articles.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_articles=[]
not_liked_articles=[]
did_not_read=[]

app=Flask(__name__)
@app.route("/get-article")

def get_movies():
    return jsonify({
        "data": all_movies[0],
        "status": "sucess"
    })

@app.route("/liked-get", methods=["POST"])
def liked_movie():
    global all_movies
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_articles.append(movie)
    return jsonify({
        "status": "sucess"
    })

@app.route("/notliked-get", methods=["POST"])
def unliked_article():
    global all_movies
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_articles.append(movie)
    return jsonify({
        "status": "sucess"
    })

@app.route("/did-read-articles", methods=["POST"])
def not_watched():
    global all_movies
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_read.append(movie)
    return jsonify({
        "status": "sucess"
    })

if __name__ == "__main__":
    app.run()