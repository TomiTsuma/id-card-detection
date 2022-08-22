import json
from flask import Flask
from flask import Flask, request, jsonify
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

my_env_var = os.getenv('.env')

app = Flask(__name__)

import detect_id_in_image


@app.route('/find_id', methods=["POST"])
def detect():
    s3_url = request.get_json()['img_path']
    prediction = detect_id_in_image.detect_id(s3_url)
    return jsonify(prediction)
    


