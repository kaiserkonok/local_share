<div align="center">

# `⚡ LocalShare`

**Share files across devices on your local network.**

No cloud. No internet. Just your WiFi.

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

### What is this?

Drop a file on one device, grab it on another. Works between **phone ↔ laptop ↔ desktop** — anything with a browser. Runs entirely on your local network, so your files never leave your house.

---

### Features

<table>
<tr>
<td width="50%">

**🚀 Instant Setup**
One command to run. No config, no database, no Docker.

**📱 Any Device**
Open the URL on any device — phone, tablet, laptop, smart fridge, whatever.

**🎨 Clean Dark UI**
Minimal, responsive interface that looks good everywhere.

</td>
<td width="50%">

**📁 Multi-File Upload**
Drag & drop multiple files at once with progress bars.

**🔍 Auto Discovery**
Server prints the network URL — just open it on other devices.

**⬇️ One-Click Download**
Tap a file to download it instantly.

</td>
</tr>
</table>

---

### Quick Start

```bash
git clone <repo-url> && cd local_share

python3 -m venv .venv
source .venv/bin/activate
pip install flask

python main.py
```

```
==================================================
  LocalShare - File Sharing Server
==================================================
  Local:   http://127.0.0.1:8081
  Network: http://192.168.0.192:8081
==================================================
```

Open the **Network URL** on any device. Done.

---

### How it works

```
┌──────────┐         ┌──────────────┐         ┌──────────┐
│  Phone   │◄───────►│   Server     │◄───────►│  Laptop  │
│  (WiFi)  │   LAN   │  (Python)    │   LAN   │  (WiFi)  │
└──────────┘         └──────────────┘         └──────────┘
                           │
                      uploads/
```

1. Start the server on any machine on your network
2. Open the printed URL on any other device
3. Upload files → they appear for everyone
4. Download files → saved to your device

---

### Tech Stack

- **Backend:** Python, Flask
- **Frontend:** Vanilla HTML/CSS/JS (no build step)
- **Storage:** Local filesystem (`uploads/`)

---

### License

[MIT](LICENSE) — do whatever you want with it.
