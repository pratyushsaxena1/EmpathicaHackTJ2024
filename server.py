from flask import Flask, render_template, jsonify, request
import os
import signal
import subprocess

app = Flask(__name__)


@app.route('/')
def serve():
    return render_template('index.html')

@app.route('/start_recording')
def start_server():
    print("starting process")
    pro = subprocess.Popen("python main.py", shell=True)
    return jsonify({"pid": pro.pid})

@app.route('/stop_recording')
def stop():
    pid = int(request.args.get('pid'))
    print(pid)
    os.killpg(os.getpgid(pid), signal.SIGTERM)
    return True