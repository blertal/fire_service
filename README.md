# Fire Detection System

> **Tip:** If you have issues, try using Firefox, clear your browser history, or use private browsing without ad blockers.

---

## Setting up a Local Virtual Environment

1. **Create a virtual environment (only needed once):**
   ```sh
   python3 -m venv ~/flask_env
   ```

2. **Activate the virtual environment:**
   ```sh
   source ~/flask_env/bin/activate
   ```

3. **Install the required packages:**
   ```sh
   pip install flask flask-cors pillow python-dotenv langchain-google-genai pydatalog
   ```

---

## Running the App

1. **Start the Flask backend:**
   ```sh
   $HOME/Downloads/fire_service/run_fire_service.sh
   ```
   (This activates the virtual environment and runs the backend on port 5000.)

2. **In a new terminal, serve the frontend:**
   ```sh
   cd $HOME/Downloads/fire_service/src
   python3 -m http.server 8000
   ```
   (This serves the frontend at [http://localhost:8000/index.html](http://localhost:8000/index.html).)

---

## Overview

The Fire Detection System is a web application that detects and analyzes fire hazards using image processing and AI (Gemini). It demonstrates how technology can enhance safety and awareness in fire-prone environments.

---

## Project Structure

```
fire_service
├── src
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── app.js
│   ├── images/
│   └── index.html
├── app.py
├── ai_agent.py
├── run_fire_service.sh
├── README.md
├── .gitignore
└── ... (other files)
```

---

## Features

- User-friendly interface for uploading images
- Real-time AI analysis of images to detect fire hazards
- Visual feedback on detection results
- Responsive design for accessibility on various devices

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/blertal/fire_service.git
   cd fire_service
   ```

2. **Set up your virtual environment and install dependencies** (see above).

3. **Add your `.env` file** with your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```
   *(Do not commit this file!)*

4. **Run the backend and frontend as described above.**

5. **Open** [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser.

---

## Technologies Used

- Python (Flask, Flask-CORS, Pillow, python-dotenv, langchain-google-genai, pyDatalog)
- HTML5, CSS3, JavaScript

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.