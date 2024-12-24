from flask import Flask, render_template, request, jsonify
import tempfile
from calorie_counter import get_calories_and_glucose_from_image
from translations import TRANSLATIONS

app = Flask(__name__)

@app.route("/")
def index():
    lang = request.args.get('lang', 'en')
    if lang not in TRANSLATIONS:
        lang = 'en'
    return render_template(
        "index.html",
        translations=TRANSLATIONS[lang],
        lang=lang
    )

@app.route("/upload", methods=["POST"])
def upload():
    language = request.form.get('language', 'en')
    if language not in TRANSLATIONS:
        language = 'en'
    
    if "image" not in request.files:
        return {"error": TRANSLATIONS[language].get('error_no_image', "No image uploaded")}, 400

    image = request.files["image"]
    if image.filename == "":
        return {"error": TRANSLATIONS[language].get('error_no_selection', "No image selected")}, 400

    temp_file = tempfile.NamedTemporaryFile()
    image.save(temp_file.name)

    try:
        # Get analysis with dynamic health advice from GPT-4
        analysis = get_calories_and_glucose_from_image(temp_file.name, language)
        return jsonify(analysis)
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        temp_file.close()

if __name__ == "__main__":
    app.run(debug=True)