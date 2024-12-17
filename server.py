from flask import Flask, render_template, request
import tempfile

from calorie_counter import get_calories_and_glucose_from_image  # Updated import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    image = request.files["image"]

    if image.filename == "":
        return {
            "error": "No image uploaded",
        }, 400

    temp_file = tempfile.NamedTemporaryFile()
    image.save(temp_file.name)

    analysis = get_calories_and_glucose_from_image(temp_file.name)  # Updated function call
    temp_file.close()

    return analysis

if __name__ == "__main__":
    app.run(debug=True)
