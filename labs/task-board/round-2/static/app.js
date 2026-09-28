const form = document.querySelector("#task-form");
const input = document.querySelector("#task-title");
const list = document.querySelector("#task-list");
const message = document.querySelector("#message");

async function loadTasks() {
  const response = await fetch("/api/tasks");
  const tasks = await response.json();
  list.replaceChildren();
  for (const task of tasks) {
    const item = document.createElement("li");
    item.textContent = task.title;
    list.append(item);
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  message.textContent = "";
  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: input.value }),
  });
  if (!response.ok) {
    message.textContent = "Task를 추가하지 못했습니다.";
    return;
  }
  input.value = "";
  await loadTasks();
});

loadTasks();
