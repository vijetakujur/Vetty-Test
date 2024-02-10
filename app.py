from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/<filename>")
def index(filename="file1.txt"):
    try:
        with open(f"files/{filename}", "r", encoding="utf-8") as file:
            file_content = file.read()
    except FileNotFoundError:
        return "File not found", 404

    return render_template("index.html", content=file_content)


if __name__ == "__main__":
    app.run(debug=True)
