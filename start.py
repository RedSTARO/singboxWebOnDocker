from flask import Flask, request, jsonify, render_template_string, redirect
import json
import os
import subprocess
import threading
import time
from urllib.parse import urlparse

app = Flask(__name__)

# HTML template for the home page with a form
HOME_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Subscription</title>
</head>
<body>
    <h2>Update Subscription URL</h2>
    <form method="post" action="/update">
        <label for="url">Subscription URL:</label><br>
        <input type="text" id="url" name="url"><br><br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
'''

# HTML template for the result page
RESULT_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Result</title>
</head>
<body>
    <h2>Result</h2>
    <p>{{ message }}</p>
    <a href="/">Go Back</a>
</body>
</html>
'''

def updateNodes(url):
    with open("./config_template/providers.json") as prov:
        data = json.load(prov)
    for subscribe in data['subscribes']:
        if subscribe['tag'] == 'tag_1':
            subscribe['url'] = url
            break
    with open("./providers.json", "w") as prov:
        json.dump(data, prov, indent=4, ensure_ascii=False)

def run_sing_box():
    subprocess.run(["./sing-box", "version"])
    subprocess.run(["./sing-box", "run"])

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HOME_PAGE_TEMPLATE)

@app.route('/update', methods=['POST'])
def update():
    # Extract the subscription URL from the form
    url = request.form['url']
    if not url:
        return render_template_string(RESULT_PAGE_TEMPLATE, message="URL is required"), 400

    # Update the subscription URL
    updateNodes(url)

    # Run the commands using subprocess
    try:
        subprocess.run(["python3", "main.py", "--template_index=0"], check=True)
        threading.Thread(target=run_sing_box, daemon=True).start()

        # Redirect user to the sing-box service running on port 9090
        domain = urlparse(request.host_url).netloc.split(":")[0]
        return redirect(f"http://{domain}:9090/")

    except subprocess.CalledProcessError as e:
        message = f"Command execution failed: {str(e)}"

    # return render_template_string(RESULT_PAGE_TEMPLATE, message=message)

app.run(debug=True, host="::", port="5000")
