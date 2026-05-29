// Get necessary DOM elements
const outputAreaDiv = document.getElementById("outputArea");
const form = document.getElementById("emailForm");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = {
    recipient: document.getElementById("recipient").value,
    subject: document.getElementById("subject").value,
    tone: document.getElementById("tone").value,
    key_points: document.getElementById("key_points").value,
  };

  try {
    // 3. Perform the Fetch API call
    const response = await fetch("/api/email", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData), // Convert JS object to JSON string
    });

    // 4. Check if the HTTP response was successful (status code 200-299)
    if (!response.ok) {
      // Handle HTTP errors (e.g., 404, 500)
      const errorBody = await response
        .json()
        .catch(() => ({ error: "Unknown server error" }));
      throw new Error(
        `Server responded with status ${response.status}: ${errorBody.error || "Failed to process request"}`,
      );
    }

    // 5. Parse the JSON response from the Flask backend
    const data = await response.json();

    // 6. Display the received data in the output area
    if (data.email_draft) {
      // Use innerHTML to render the potentially multi-line draft content
      outputAreaDiv.innerHTML = `
            <div style="border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9;">
                <p><strong>To:</strong> ${data.recipient}</p>
                <p><strong>Subject:</strong> ${data.subject}</p>
                <hr>
                <pre style="white-space: pre-wrap; font-family: monospace;">${data.email_draft}</pre>
            </div>
          `;
    } else {
      outputAreaDiv.innerHTML =
        '<p style="color: orange;">Success, but no draft was returned from the server.</p>';
    }
  } catch (err) {
    // 7. Handle network errors or errors thrown above
    console.error("Fetch Error:", err);
    outputAreaDiv.innerHTML = `<p style="color: red;">Error generating draft: ${err.message}</p>`;
  }
});
