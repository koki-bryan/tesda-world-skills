// Target all elements we need to interact with
const welcomeSection = document.getElementById("main-section-heading");
const chatMessagesContainer = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");
const sendButton = document.querySelector(".send-btn");

// Helper function to render a chat bubble (React Component equivalent)
const appendMessage = (text, sender) => {
  const isUser = sender === "user";

  // Tailwind layout classes based on who sent the message
  const bubbleHTML = `
    <div class="flex ${isUser ? "justify-end" : "justify-start"} w-full animate-fade-in">
      <div class="max-w-[70%] p-4 rounded-2xl shadow-md ${
        isUser
          ? "bg-blue-600 text-white rounded-br-none"
          : "bg-white text-black rounded-bl-none border border-slate-200"
      }">
        <p class="text-lg leading-relaxed whitespace-pre-wrap">${text}</p>
      </div>
    </div>
  `;

  // Inject the HTML string into the bottom of our chat box
  chatMessagesContainer.insertAdjacentHTML("beforeend", bubbleHTML);

  // Automatically scroll down to show the new message
  chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
};

const handleSend = async () => {
  const promptText = userInput.value.trim();
  userInput.value = "";

  if (!promptText) return;
  welcomeSection.classList.add("hidden");
  appendMessage(promptText, "user");
  appendMessage("Aida is thinking...", "ai");

  try {
    const response = await fetch("http://localhost:5000/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: promptText }),
    });

    const data = await response.json();

    // remove aida is thinking
    const lastMessage = chatMessagesContainer.lastElementChild;
    if (lastMessage && lastMessage.innerText.includes("Aida is thinking...")) {
      lastMessage.remove();
    }
    appendMessage(data.response, "ai");
  } catch (error) {
    console.error(error);
  }
};

// Event listener attached at the very bottom
sendButton.addEventListener("click", handleSend);
