function generateQRCode() {
  const name = document.getElementById("nameInput").value.trim();
  const img = document.getElementById("qrImage");

  if (name === "") {
    alert("名を入力せよ、勇者よ！");
    return;
  }

  img.style.display = "none";
  img.src = `/generate_qr?name=${encodeURIComponent(name)}&t=${Date.now()}`; // キャッシュ防止
  img.onload = () => {
    img.style.display = "block";
  };
}
