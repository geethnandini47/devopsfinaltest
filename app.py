from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Wild Rydes</title></head>
      <body style="font-family:Arial;margin:40px">
        <h1>Wild Rydes</h1>
        <h3>Developer: Geeth Nandini Chukka</h3>
        <h3>Student ID: 101001858</h3>
        <p>Deployed on Amazon ECS via GitHub Actions CI/CD.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
