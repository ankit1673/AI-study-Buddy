async function explain() {
    let topic = document.getElementById("topic").value;

    let res = await fetch("/explain", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({topic})
    });

    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}

async function summarize() {
    let text = document.getElementById("notes").value;

    let res = await fetch("/summarize", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}

async function quiz() {
    let topic = document.getElementById("quizTopic").value;

    let res = await fetch("/quiz", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({topic})
    });

    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}
