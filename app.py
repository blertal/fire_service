from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import ai_agent
import os

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)
    try:
        img = Image.open(filepath)
        # You can change the prompt as needed
        result = ai_agent.generate_pil_image_caption(
            ai_agent.llm_model,
            img,
            prompt="Is there a fire emergency in this image? Answer yes or no."
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)