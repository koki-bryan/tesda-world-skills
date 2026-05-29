console.log("chat.js loaded successfully");

const sendButton = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const modelPersonality = document.getElementById("ai-personality-select");
const chatWindow = document.getElementById("chat-window");

const conversation = [];
conversation.push({
  role: "system",
  content:
    "Always include a confidence score at each response, indicate whether it is HIGH/MED/LOW",
});
sendButton.addEventListener("click", async () => {
  conversation.push({ role: "user", content: userInput.value });

  chatWindow.innerHTML += `<div class='flex  mx-auto p-6 bg-neutral-300 max-w-4xl rounded-br-none rounded-lg'>${userInput.value} </div>`;
  chatWindow.innerHTML += `<div class='mx-auto p-6 bg-blue-100 max-w-4xl rounded-bl-none rounded-lg'>Loading: ${modelPersonality.value}...</div>`;

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: modelPersonality.value,
      messages: conversation,
    }),
  });

  //returns the {content:--, role:"assistant"}
  data = await res.json();

  //fields are accessible via data.data.field because flask sends data: reponse
  conversation.push({ role: data.data.role, content: data.data.content });
  console.log(conversation);

  chatWindow.innerHTML += `<div class='mx-auto p-6 bg-blue-100 w-fit rounded-bl-none rounded-lg'>${data.data.content}</div>`;

  userInput.value = "";
});
