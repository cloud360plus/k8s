from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def pod_info():
    pod_name = os.environ.get('HOSTNAME', 'Unknown')
    pod_ip = socket.gethostbyname(socket.gethostname())

    return f"""
    <h2>Pod Information</h2>
    <ul>
        <li><strong>Pod Name:</strong> {pod_name}</li>
        <li><strong>Pod IP:</strong> {pod_ip}</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
