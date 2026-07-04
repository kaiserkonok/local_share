# LocalShare

A simple, self-hosted file sharing app for your local network. Share files between any devices (phone, laptop, desktop) connected to the same WiFi/network — no internet required.

## Features

- Drag & drop or click to upload
- Multiple file upload with progress tracking
- Download files from any device
- Delete files
- Responsive dark UI (works on mobile, tablet, desktop)
- Auto-detects your local IP address
- Zero dependencies beyond Python

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd local_share

# Create virtual environment and install Flask
python3 -m venv .venv
source .venv/bin/activate
pip install flask

# Run the server
python main.py
```

The server will print two URLs:
- **Local**: `http://127.0.0.1:8081` (use on the same machine)
- **Network**: `http://<your-ip>:8081` (use on other devices)

Open the **Network URL** on any device connected to the same network.

## Requirements

- Python 3.7+
- Flask

## How It Works

1. Start the server on one device
2. Open the network URL on any other device
3. Upload and download files — everything is shared across all connected devices

## License

MIT
