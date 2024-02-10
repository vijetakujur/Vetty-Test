from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Read the content of file4.txt using utf-16-le encoding
    with open("files/file4.txt", "r", encoding="utf-16-le") as file:
        file_content = file.read()

    # Pass the file content to the HTML template
    return render_template("index.html", content=file_content)


if __name__ == "__main__":
    app.run(debug=True)
