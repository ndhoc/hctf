from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>File Reader</title>
    </head>
    <body>
        <h3>File Reader</h3>
        <form action="/read" method="GET">
            <input type="text" name="file" placeholder="Enter filename" required>
            <button type="submit">Read</button>
        </form>
        <p>
        readme.txt<br>
        secret.txt<br>
        help.txt
        </p>
    </body>
    </html>
    '''

@app.route('/read')
def read_file():
    filename = request.args.get('file', '')
    

    try:
        file_path = os.path.join('files', filename)
        with open(file_path, 'r') as f:
            content = f.read()
        return f'<pre>{content}</pre><br><a href="/">Back</a>'
    except FileNotFoundError:
        print("Đường dẫn đang mở:", file_path)

        return f'Not found "{filename} {file_path}"<br><a href="/">Back</a>'
    except Exception as e:
        print("Đường dẫn đang mở:", file_path)
        return f'Error: {str(e)} {file_path}<br><a href="/">Back</a>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

