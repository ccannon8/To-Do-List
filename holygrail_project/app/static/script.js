document.addEventListener("DOMContentLoaded", function () {
  loadTasks();

  document.getElementById("taskForm").addEventListener("submit", function (e) {
    e.preventDefault();
    addTask();
  });
});

function loadTasks() {
  fetch("/api/tasks")
    .then((response) => response.json())
    .then((tasks) => {
      const tbody = document.getElementById("taskTableBody");
      tbody.innerHTML = "";
      tasks.forEach((task, index) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
                    <td>${task.task}</td>
                    <td>${task.due_date}</td>
                    <td>${getPriorityText(task.priority)}</td>
                    <td>${task.done ? "Done" : "Not Done"}</td>
                    <td>
                        <button onclick="markDone(${index})">Mark Done</button>
                        <button onclick="deleteTask(${index})">Delete</button>
                    </td>
                `;
        tbody.appendChild(tr);
      });
    });
}

function getPriorityText(priority) {
  switch (priority) {
    case 1:
      return "High";
    case 2:
      return "Medium";
    case 3:
      return "Low";
    default:
      return "Unknown";
  }
}

function addTask() {
  const formData = {
    task: document.getElementById("task").value,
    due_date: document.getElementById("due_date").value,
    priority: document.getElementById("priority").value,
  };

  fetch("/api/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        document.getElementById("taskForm").reset();
        loadTasks();
      }
    });
}

function markDone(index) {
  fetch(`/api/tasks/${index}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ done: true }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        loadTasks();
      }
    });
}

function deleteTask(index) {
  if (confirm("Are you sure you want to delete this task?")) {
    fetch(`/api/tasks/${index}`, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          loadTasks();
        }
      });
  }
}
