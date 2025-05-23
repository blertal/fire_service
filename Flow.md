1. You run your .sh script
./run_fire_service.sh

- Activates your virtual environment (source ~/flask_env/bin/activate)
- Changes directory to your project folder (cd $HOME/ 
- Downloads/fire_service)
- Starts your Flask backend (python app.py)
- Flask now listens for HTTP requests at http://127.0.0.1:5000

2. You start your static server for the frontend
In a separate terminal:
cd $HOME/Downloads/fire_service/src
python -m http.server 8000
- This serves your HTML, CSS, and JS files at http://localhost:8000/index.html

3. You open the web app in your browser
- You visit: http://localhost:8000/index.html
- The browser loads your HTML, CSS, and JavaScript.

4. You click "Browse" and select an image
- The image is not uploaded anywhere yet.
- The selected image is stored in your browser’s memory (as a File object in the file input).

5. You click "Analyze"
- The JavaScript grabs the selected image from the file input.
- It creates a FormData object and appends the image file to it.
- It sends a POST request to your Flask backend at http://127.0.0.1:5000/analyze with the image in the request body.

6. Flask backend receives the image
- Flask receives the POST request at /analyze.
- The image is saved to a temporary location (e.g., /tmp/filename.png).
- The backend loads the image, runs the AI model, and generates a result (e.g., "Yes." or "No.").
- Flask sends a JSON response back to the frontend with the result.

7. Frontend displays the result
- The JavaScript receives the JSON response.
- It updates the web page to show the AI result under "Analysis Results".

Summary Table
| Step            | What Runs?           | Where?           | What Happens?                                 |
|-----------------|----------------------|------------------|-----------------------------------------------|
| 1. .sh script   | Flask backend        | Terminal 1       | Starts backend on port 5000                   |
| 2. Static server| Python HTTP server   | Terminal 2       | Serves frontend on port 8000                  |
| 3. Open web app | Browser              | localhost:8000   | Loads HTML/JS                                 |
| 4. Browse image | Browser              | Local memory     | Image selected, not uploaded yet              |
| 5. Analyze click| Browser JS → Flask   | HTTP POST        | Image sent to backend for analysis            |
| 6. Backend proc | Flask                | Server-side      | AI analyzes image, returns result             |
| 7. Show result  | Browser JS           | Web page         | Displays result to user                       |

Where does the image go?
- When you select it: Browser memory only
- When you click Analyze: Sent to Flask backend, saved temporarily, analyzed, then deleted or overwritten
