function analyzeEmotion() {
    const text = document.getElementById("textToAnalyze").value;
    const outputDiv = document.getElementById("output");

    if (!text.trim()) {
        outputDiv.textContent = "Invalid text! Please try again!";
        return;
    }

    const url = "/emotionDetector?textToAnalyze=" + encodeURIComponent(text);

    fetch(url)
        .then(response => response.text())
        .then(data => {
            outputDiv.textContent = data;
        })
        .catch(error => {
            outputDiv.textContent = "Error: " + error;
        });
}
