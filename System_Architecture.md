# Fire Detection System – System Architecture Overview

## Components

- **Frontend:**  
  Static HTML/CSS/JS served by Python’s HTTP server (`python -m http.server 8000`).
- **Backend:**  
  Flask app (`app.py`) running on port 5000, providing the `/analyze` API endpoint.
- **AI Agent:**  
  `ai_agent.py` handles image encoding and communication with Gemini (Google Generative AI).
- **Logic Layer:**  
  Uses pyDatalog for simple logic rules (e.g., fire/smoke → emergency).

---

## Data Flow

1. **User opens** `http://localhost:8000/index.html` in a browser.
2. **User selects an image** (remains in browser memory).
3. **User clicks "Analyze":**
    - JS sends a POST request with the image to `http://127.0.0.1:5000/analyze`.
4. **Flask backend**:
    - Receives the image.
    - Saves it temporarily.
    - Loads it with PIL.
    - Passes it to the AI agent for analysis.
5. **AI agent (`ai_agent.py`):**
    - Encodes the image to base64.
    - Sends it to Gemini LLM with a prompt.
    - Receives and returns the result (e.g., "Yes."/"No." and/or a caption).
6. **Backend returns** the result as JSON.
7. **Frontend JS displays** the result to the user.

---

## Key Files

- `app.py` – Flask backend
- `src/index.html`, `src/js/app.js` – Frontend
- `ai_agent.py` – AI and logic utilities
- `.env` – API keys (never committed)
- `run_fire_service.sh` – Script to start backend

---

## Example Sequence

1. User runs `run_fire_service.sh` (starts Flask backend).
2. User runs `python -m http.server 8000` in `src/` (serves frontend).
3. User opens browser, uploads image, clicks Analyze.
4. Image is POSTed to Flask, analyzed by Gemini, result shown in browser.

---

## Security

- `.env` is ignored by git (contains secrets).
- No sensitive data is exposed in the repo.

---

*For more details, see the code and README.md.*