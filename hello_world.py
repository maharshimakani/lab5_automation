from flask import Flask

app = Flask(__name__)


def greet() -> str:
    """Return the greeting message used in the app."""
    return "Welcome to CI/CD 101 using GitHub Actions!"


def generate_html(message: str) -> str:
    """Wrap a message in a simple HTML page."""
    return f"""
<html>
  <head>
    <title>Greeting</title>
  </head>
  <body>
    <h1>{message}</h1>
    <img
      src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
      alt="GitHub logo"
    >
  </body>
</html>
"""


@app.route("/greeting")
def greeting():
    """Flask route that returns the greeting page."""
    message = greet()
    return generate_html(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4049)
