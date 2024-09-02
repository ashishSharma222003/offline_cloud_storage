# P2P Messaging Application

## Overview

This project is a peer-to-peer (P2P) messaging application developed in Python. The application allows users to send and receive messages directly between peers without relying on a central server. This can be useful for creating decentralized communication systems or for educational purposes to understand P2P networking concepts.

## Features

- **Decentralized Communication:** No central server; messages are sent directly between peers.
- **Real-time Messaging:** Immediate message delivery to connected peers.
- **Simple User Interface:** Basic command-line interface for ease of use.
- **Scalable:** Can be extended with additional features like encryption or file transfer.

## Requirements

- Python 3.x
- `socket` library (included in the Python Standard Library)
- `threading` library (included in the Python Standard Library)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ashishSharma222003/offline_cloud_storage.git


# File Upload and Download App

## Overview

This Streamlit application allows users to upload and download files directly from a web interface. It supports various file types, including text, CSV, images, videos, and PDFs. The app is designed to facilitate simple and efficient file sharing in a peer-to-peer (P2P) manner.

## Features

- **File Upload:** Upload files of different types such as text, CSV, images, and videos.
- **File Download:** Download previously uploaded files.
- **Interactive Interface:** User-friendly web interface provided by Streamlit.
- **LAN Access:** Accessible over a local network for file sharing between devices.

## Requirements

- Python 3.x
- Streamlit library (`streamlit`)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ashishSharma222003/offline_cloud_storage.git
2. **Navigate to the project directory:**

   ```sh
   cd file-upload-download-app
3. **Install dependencies:**

   ```sh
   pip install streamlit
5. **Start the Streamlit application:**

   ```sh
   streamlit run streamlitdrive.py

## Access the Application

### Access Locally

To use the application on your local machine:

1. Open your web browser.
2. Navigate to `http://localhost:8501`.

### Access Over LAN

To make the application accessible to other devices on the same local network:

1. **Find Your Local IP Address:**
   - On Windows, open Command Prompt and run:
     ```sh
     ipconfig
     ```
   - On Linux/Mac, open a terminal and run:
     ```sh
     ifconfig
     ```
     or
     ```sh
     ip a
     ```

2. **Start the Streamlit Application:**
   - Open a terminal and run the following command, replacing `192.168.1.100` with your actual local IP address:
     ```sh
     streamlit run app.py --server.address 192.168.1.100
     ```

3. **Ensure Port Accessibility:**
   - Make sure that port `8501` is open and accessible through your firewall settings.

4. **Access from Other Devices:**
   - On other devices connected to the same LAN, open a web browser.
   - Navigate to `http://<your-local-ip>:8501`, replacing `<your-local-ip>` with the IP address of the machine running the app.



