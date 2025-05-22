# Fire Detection System


## Setting up a Local Virtual Environment

1. **Create a virtual environment (only needed once):**
   ```
   python -m venv ~/flask_env
   ```

2. **Activate the virtual environment:**
   ```
   source ~/flask_env/bin/activate
   ```

3. **Install the required packages:**
   ```
   pip install flask flask-cors pillow python-dotenv langchain-google-genai pydatalog
   ```

# To run in local virtual environment
source ~/flask_env/bin/activate

# Install these
In your activated virtual environment, run:

```
pip install flask flask-cors pillow python-dotenv langchain-google-genai pydatalog
```

## TO RUN THE APP -- use the folder where you installed virtual env. ##
1. run in your terminal: 
source ~/flask_env/bin/activate

2. run in your terminal (flask_env): 
$HOME/Downloads/fire_service/run_fire_service.sh

3. run in another terminal
source ~/flask_env/bin/activate

and in the same terminal (flask_env): 
python -m http.server 8000

## Overview
The Fire Detection System is a web application designed to detect and analyze fire hazards using image processing and machine learning techniques. This project serves as a demonstration of how technology can be leveraged to enhance safety and awareness in environments prone to fire risks.

## Project Structure
```
fire-detection-system
├── src
│   ├── css
│   │   └── styles.css        # Styles for the web application
│   ├── js
│   │   └── app.js           # JavaScript code for handling interactions
│   ├── images                # Directory for storing images
│   └── index.html            # Main HTML file for the application
├── README.md                 # Documentation for the project
```

## Features
- User-friendly interface for uploading images.
- Real-time analysis of images to detect fire hazards.
- Visual feedback on the detection results.
- Responsive design for accessibility on various devices.

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fire-detection-system
   ```

2. **Open the project in your preferred web server or IDE.**

3. **Run the application:**
   - Open `src/index.html` in a web browser to view the application.

## Technologies Used
- HTML5
- CSS3
- JavaScript
- Image Processing Libraries (if applicable)

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.