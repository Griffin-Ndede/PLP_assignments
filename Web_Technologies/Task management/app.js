firebase.initializeApp({
    apiKey: "AIzaSyCLNj3G_O6YMMqU2lfG6Mshwh_YBonndGk",
    authDomain: "to-do-42ecd.firebaseapp.com",
    projectId: "to-do-42ecd",
});

const db = firebase.firestore();

function addTask() {
    const taskInput = document.getElementById("task-input");
    const task = taskInput.value.trim();
    if (task !== "") {
        db.collection("tasks").add({
            task: task,
            timestamp: firebase.firestore.FieldValue.serverTimestamp(),
        });
        taskInput.value = "";
    }
}

function renderTasks(doc) {
    const taskList = document.getElementById("task-list");
    const taskItem = document.createElement("li");
    taskItem.className = "task-item";
    taskItem.innerHTML = `
    <span>${doc.data().task}</span>
    <button onclick='deleteTask("${doc.id}")'>Delete</button>
    `;
    taskList.appendChild(taskItem);
}

db.collection("tasks")
    .orderBy("timestamp", "desc")
    .onSnapshot(snapshot => {
        const changes = snapshot.docChanges();
        changes.forEach(change => {
            if (change.type === "added") {
                renderTasks(change.doc);
            }
        });
    });

function deleteTask(id) {
    db.collection("tasks").doc(id).delete();
}
