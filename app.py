from flask import Flask, request, send_file, render_template
import qrcode
import io
import urllib.parse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("qr.html")

@app.route("/generate_qr")
def generate_qr():
    text = request.args.get("text", "")

    # 入力文字をURLエンコードしてURLに埋め込む
    encoded_text = urllib.parse.quote(text)
    url = f"http://localhost:5000/show?text={encoded_text}"

    qr = qrcode.make(url)
    img_io = io.BytesIO()
    qr.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

@app.route("/show")
def show_text():
    text = request.args.get("text", "")
    return f"<h1>{text}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
