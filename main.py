import os
import socket
import uuid
import time
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = None  # No size limit
app.config['UPLOAD_FOLDER'] = Path(__file__).parent / 'uploads'

app.config['UPLOAD_FOLDER'].mkdir(exist_ok=True)


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400

    files = request.files.getlist('files')
    uploaded = []

    for file in files:
        if file.filename == '':
            continue

        filename = secure_filename(file.filename)
        if not filename:
            filename = f"file_{uuid.uuid4().hex[:8]}"

        save_path = app.config['UPLOAD_FOLDER'] / filename
        file.save(save_path)
        uploaded.append({
            'name': filename,
            'size': save_path.stat().st_size,
            'sizeFormatted': format_size(save_path.stat().st_size),
            'id': uuid.uuid4().hex
        })

    return jsonify({'uploaded': uploaded, 'count': len(uploaded)})


@app.route('/api/files')
def list_files():
    files = []
    for f in app.config['UPLOAD_FOLDER'].iterdir():
        if f.is_file():
            files.append({
                'name': f.name,
                'size': f.stat().st_size,
                'sizeFormatted': format_size(f.stat().st_size),
                'modified': f.stat().st_mtime,
                'id': uuid.uuid4().hex
            })
    files.sort(key=lambda x: x['modified'], reverse=True)
    return jsonify({'files': files})


@app.route('/api/download/<path:filename>')
def download_file(filename):
    return send_from_directory(
        str(app.config['UPLOAD_FOLDER']),
        filename,
        as_attachment=True
    )


@app.route('/api/delete/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = app.config['UPLOAD_FOLDER'] / filename
    if file_path.exists() and file_path.is_file():
        file_path.unlink()
        return jsonify({'deleted': filename})
    return jsonify({'error': 'File not found'}), 404


if __name__ == '__main__':
    ip = get_local_ip()
    port = 8081
    print(f"\n{'='*50}")
    print(f"  LocalShare - File Sharing Server")
    print(f"{'='*50}")
    print(f"  Local:   http://127.0.0.1:{port}")
    print(f"  Network: http://{ip}:{port}")
    print(f"{'='*50}")
    print(f"  Open the Network URL on any device")
    print(f"  connected to the same WiFi/network.\n")
    app.run(host='0.0.0.0', port=port, debug=False)
