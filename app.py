import os
from subprocess import call
from flask import Flask, request, Response

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    file = request.files['file']
    sheet = request.form.get('sheet', 1, type=int)
    if not file:
        return "`file` must be included", 400

    input = os.path.join(UPLOAD_FOLDER, "a.xls")
    medium = os.path.join(UPLOAD_FOLDER, "a.xlsx")
    output = os.path.join(UPLOAD_FOLDER, "a.csv")
    file.save(input)
    call(["libreoffice", "--headless", "--convert-to", "xlsx", "--outdir", UPLOAD_FOLDER, input])
    call(["xlsx2csv", "--sheet", str(sheet), medium, output])
    with open(output, 'r') as f:
        return Response(f.read(), mimetype="text/csv")