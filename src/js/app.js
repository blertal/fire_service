<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Fire Detection AI Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div class="neon-glow"></div>
  <header>
    <h1><span class="ai">AI</span> Fire Detection <span class="pulse">●</span></h1>
    <p class="subtitle">Real-time Hazard Analysis &amp; Alerts</p>
  </header>
  <main>
    <div class="iphone-frame">
      <div class="iphone-notch"></div>
      <div class="iphone-inner">
        <section class="upload-section">
          <label for="imageUpload" class="upload-label">
            <span>Upload Surveillance Images</span>
            <input type="file" id="imageUpload" multiple accept="image/*">
          </label>
          <button id="analyzeBtn">Analyze</button>
        </section>
        <section class="results-section" id="resultsSection">
          <h2>Analysis Results</h2>
          <div id="results"></div>
        </section>
      </div>
      <div class="iphone-home"></div>
    </div>
  </main>
  <footer>
    <p>Powered by <span class="ai">AI</span> &amp; Gemini | <span class="year"></span></p>
  </footer>
  <script src="js/app.js"></script>
</body>
</html>

// This file contains the JavaScript code for the Fire Detection System application.
// It handles user interactions, processes data, and communicates with any backend services if necessary.

document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('imageUpload');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resultsDiv = document.getElementById('results');

    analyzeBtn.addEventListener('click', () => {
        const files = imageInput.files;
        if (!files.length) {
            resultsDiv.innerHTML = '<span style="color:#ff003c;">Please upload an image.</span>';
            return;
        }
        resultsDiv.innerHTML = '<span style="color:#00ffe7;">Analyzing image with AI...</span>';

        const formData = new FormData();
        formData.append('file', files[0]);

        fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                resultsDiv.innerHTML = `<span style="color:#00ffe7;">Result: ${data.result}</span>`;
            } else if (data.error) {
                resultsDiv.innerHTML = `<span style="color:#ff003c;">Error: ${data.error}</span>`;
            } else {
                resultsDiv.innerHTML = `<span style="color:#ff003c;">Unknown error.</span>`;
            }
        })
        .catch(error => {
            resultsDiv.innerHTML = `<span style="color:#ff003c;">Error: ${error}</span>`;
        });
    });
});