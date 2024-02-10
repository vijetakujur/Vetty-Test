# Flask File Viewer

This is a simple Flask web application that allows you to view the contents of text files. It provides the following features:

- Ability to view the contents of different text files.
- Optional URL query parameters to specify start and end line numbers.
- Preserving markup in the text files.
- Graceful handling of exceptions.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/vijetakujur/Vetty-Test.git

2. Set up a virtual environment:

python -m venv env

3. Activate the virtual environment:

  On Windows: .\env\Scripts\activate
  On macOS/Linux: source env/bin/activate

4. Install the required dependencies:

pip install -r requirements.txt

## Usage

1.Run the Flask Application

flask run

2. Open a web browser and navigate to `http://127.0.0.1:5000` to view the application.
3. You can specify the target file name and optional start/end line numbers in the URL:

- To view a specific file: http://127.0.0.1:5000/filename
- To specify start and end line numbers: http://127.0.0.1:5000/filename?start=1&end=10
