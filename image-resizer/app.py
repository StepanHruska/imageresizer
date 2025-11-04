from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resize', methods=['POST'])
def resize():
    file = request.files['image']
    width = int(request.form['width'])
    height = int(request.form['height'])

    image = Image.open(file)
    resized = image.resize((width, height))

    buf = io.BytesIO()
    resized.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=True, download_name='resized.png')

if __name__ == '__main__':
    app.run(debug=True)

🎨 Krok 4️⃣: Udělej jednoduchý frontend

Vytvoř složku templates/ → uvnitř index.html:

<!DOCTYPE html>
<html>
<head>
    <title>Image Resizer</title>
</head>
<body>
    <h1>Resize Your Image</h1>
    <form action="/resize" method="POST" enctype="multipart/form-data">
        <label>Upload image:</label>
        <input type="file" name="image" accept="image/*" required><br><br>

        <label>Width:</label>
        <input type="number" name="width" required><br><br>

        <label>Height:</label>
        <input type="number" name="height" required><br><br>

        <button type="submit">Resize</button>
    </form>
</body>
</html>
