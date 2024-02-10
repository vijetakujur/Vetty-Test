from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/<filename>")
def index(filename="file1.txt"):
    start_line = request.args.get("start")
    end_line = request.args.get("end")

    try:
        with open(f"files/{filename}", "r", encoding="utf-8") as file:
            lines = file.readlines()

            if start_line is not None and end_line is not None:
                try:
                    start_line = int(start_line)
                    end_line = int(end_line)
                    file_content = "".join(lines[start_line - 1 : end_line])
                except ValueError:
                    return "Invalid start or end line number", 400
            else:
                file_content = "".join(lines)

    except FileNotFoundError:
        return "File not found", 404

    return render_template("index.html", content=file_content)


if __name__ == "__main__":
    app.run(debug=True)
