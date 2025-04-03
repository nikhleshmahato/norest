// Global variable to store response data
let responseData = {};

// Load JSON data when page loads
document.addEventListener('DOMContentLoaded', async function() {
    try {
        const response = await fetch('responses.json');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        responseData = await response.json();
        setupEventListeners();
    } catch (error) {
        console.error('Error loading JSON file:', error);
        document.getElementById('responseArea').textContent = 
            "Sorry, I couldn't load my response data. Please try again later.";
    }
});

function setupEventListeners() {
    // Button click event
    document.getElementById('submitBtn').addEventListener('click', getResponse);
    
    // Enter key event
    document.getElementById('inputBox').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            getResponse();
        }
    });
}

function getResponse() {
    const inputText = document.getElementById('inputBox').value.toLowerCase().trim();
    const responseArea = document.getElementById('responseArea');
    
    if (!inputText) {
        responseArea.textContent = "Please type something first!";
        return;
    }
    
    // Check for exact matches first
    if (responseData[inputText]) {
        responseArea.textContent = responseData[inputText];
        return;
    }
    
    // Check for partial matches
    for (const key in responseData) {
        if (inputText.includes(key)) {
            responseArea.textContent = responseData[key];
            return;
        }
    }
    
    // Default response if no matches found
    responseArea.textContent = responseData.default;
}