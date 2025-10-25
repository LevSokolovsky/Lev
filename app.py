from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/explore")
def explore():
    creators = [
        {"name": "Ava Sol", "initials": "AS", "bio": "Sci-fi dreamer · 12 new prompts this week"},
        {"name": "Noah Rivers", "initials": "NR", "bio": "Mythology enthusiast · Collaboration open"},
        {"name": "Lena Coast", "initials": "LC", "bio": "Writes micro essays · #30DayChallenge"},
        {"name": "Kai Bloom", "initials": "KB", "bio": "Illustrated tales · Accepting commissions"},
    ]
    return render_template("explore.html", creators=creators)


@app.route("/profile")
def profile():
    profile_data = {
        "name": "Nova Scribbles",
        "initials": "NS",
        "bio": "Story architect · Visual storyteller",
        "about": "I create interactive fiction experiences inspired by urban legends and everyday magic.",
        "story_count": 13,
        "followers": 482,
        "drafts": 7,
    }
    return render_template("profile.html", profile=profile_data)


@app.route("/create")
def create_post():
    return render_template("create_post.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


@app.route("/help")
def faq():
    return render_template("faq.html")


if __name__ == "__main__":
    app.run(debug=True)
