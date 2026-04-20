from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

# Vercel용 핸들러
def handler(request, context):
    return app(request.environ, lambda status, headers: None)
