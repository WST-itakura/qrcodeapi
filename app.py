from flask import Flask, request, send_file, render_template
import qrcode
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("qr.html")

@app.route("/generate_qr")
def generate_qr():
    name = request.args.get("name", "名無し")
    data = f"Name: {name}"
    qr = qrcode.make(data)
    img_io = io.BytesIO()
    qr.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")

# if __name__ == "__main__":
#     app.run(debug=True)
