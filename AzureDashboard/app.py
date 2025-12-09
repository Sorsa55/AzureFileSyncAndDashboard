from flask import Flask, render_template, send_file, request
from azure.storage.fileshare import ShareFileClient, ShareDirectoryClient
import os

app = Flask(__name__)

conn_str="YOUR_ACCESS_KEY"#Put in .env
share_name="YOUR_FILESHARE_NAME" #You should put these in .env

@app.route("/")
def index():
    directory = ShareDirectoryClient.from_connection_string(conn_str, share_name, "")
    files = [f.name for f in directory.list_directories_and_files()]
    return render_template("index.html", files=files)

@app.route("/download/<filename>")
def download(filename):
    file_client = ShareFileClient.from_connection_string(conn_str, share_name, filename)
    data = file_client.download_file().readall()
    temp_path = f"temp_{filename}"
    with open(temp_path, "wb")as f:
        f.write(data)
    return send_file(temp_path, as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file_bytes = file.read()
    file_client = ShareFileClient.from_connection_string(conn_str, share_name, file.filename)
    file_client.create_file(len(file_bytes))
    file_client.upload_file(file_bytes)
    return "file uploaded succsesfully! <br><a href = '/'>Back</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
