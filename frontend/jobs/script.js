fetch("http://127.0.0.1:8000/api/summaries/")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("summary-container");
    container.innerHTML = "";
    
    // Loop through keys (URLs)
    for (const [url, summary] of Object.entries(data)) {
      const div = document.createElement("div");
      div.className = "summary";
      div.innerHTML = `
        <a href="${url}" target="_blank">${url}</a>
        <p>${summary}</p>
      `;
      container.appendChild(div);
    }
  })
  .catch(error => {
    document.getElementById("summary-container").innerText = "Failed to load summaries.";
    console.error("Fetch error:", error);
  });