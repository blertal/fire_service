from PIL import Image
from io import BytesIO
import os
import base64
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from pyDatalog import pyDatalog

# Load .env from a custom location
load_dotenv(dotenv_path="$HOME/Downloads/.env")

# --- Image utilities ---

def encode_image(image_path):
    """Encodes an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def encode_pil_image(pil_image):
    """Encodes a PIL image to base64."""
    im_file = BytesIO()
    pil_image.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64.decode("utf-8")

# --- Gemini LLM utilities ---

api_key = os.getenv("GEMINI_API_KEY")

llm_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.0,
    max_tokens=None,
    timeout=None,
    max_retries=1,
    google_api_key=api_key,
)

def generate_pil_image_caption(model, pil_image, prompt="What is in this image?"):
    try:
        base64_image = encode_pil_image(pil_image)
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            ]
        )
        response = model.invoke([message])
        return response.content
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

def generate_answer_to_prompt(model, prompt):
    try:
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
            ]
        )
        response = model.invoke([message])
        return response.content
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

# --- pyDatalog logic example ---

pyDatalog.clear()
pyDatalog.create_terms('Fire, Smoke, Emergency, X')

# Rule: If there is fire, there is an emergency
Emergency(X) <= Fire(X)
# Rule: If there is smoke, there is an emergency
Emergency(X) <= Smoke(X)

def analyze_label_with_logic(label):
    pyDatalog.clear()
    pyDatalog.create_terms('Fire, Smoke, Emergency, X')
    Emergency(X) <= Fire(X)
    Emergency(X) <= Smoke(X)
    # Add facts based on label
    if label.lower() == 'fire':
        +Fire('scene')
    elif label.lower() == 'smoke':
        +Smoke('scene')
    # Query
    result = Emergency('scene')
    return bool(result)

# Example usage:
# is_emergency = analyze_label_with_logic('fire')  # True
# is_emergency = analyze_label_with_logic('smoke') # True
# is_emergency = analyze_label_with_logic('default') # False