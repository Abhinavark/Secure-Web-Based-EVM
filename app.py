from flask import Flask, render_template, request, redirect
import json
from utils import hash_vote, verify_hash
from elgamal import encrypt_vote   

app = Flask(__name__)

with open("voters.json") as f:
    VOTERS = json.load(f)

def load_votes():
    with open("votes.json") as f:
        return json.load(f)

def save_votes(votes):
    with open("votes.json", "w") as f:
        json.dump(votes, f, indent=2)

def has_voted(voter, votes):
    return any(v["voter"] == voter for v in votes)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        voter = request.form["voter"]
        password = request.form["password"]

        if VOTERS.get(voter) == password:
            return redirect(f"/vote/{voter}")
        else:
            return "Authentication failed"

    return render_template("login.html")

@app.route("/vote/<voter>", methods=["GET", "POST"])
def vote(voter):
    if request.method == "POST":
        candidate = request.form["candidate"]
        votes = load_votes()

        if has_voted(voter, votes):
            return "Duplicate vote prevented"

        vote_data = f"{voter}:{candidate}"

        cipher = encrypt_vote(candidate)
        vote_hash = hash_vote(str(cipher))

        votes.append({
            "voter": voter,
            "cipher": cipher,
            "hash": vote_hash
        })

        save_votes(votes)
        return render_template("success.html")

    return render_template("vote.html", voter=voter)

if __name__ == "__main__":
    app.run(debug=True)
