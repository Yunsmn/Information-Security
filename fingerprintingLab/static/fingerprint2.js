const sentence = document.getElementById("target-sentence").textContent;
const input = document.getElementById("typing-input");

let startTime = null;
let corrections = 0;

input.addEventListener("keydown", function (event) {
    if (startTime === null) {
        startTime = performance.now();
    }
    if (event.key === "Backspace") {
        corrections = corrections + 1;
    }
});

input.addEventListener("input", function () {
    if (input.value !== sentence) {
        return;
    }

    // Speed in words per minute, one word = 5 characters
    const seconds = (performance.now() - startTime) / 1000;
    const speed = (sentence.length / 5) / (seconds / 60);

    document.getElementById("typing-time").textContent = "Time: " + seconds.toFixed(2) + " s";
    document.getElementById("typing-speed").textContent = "Speed: " + speed.toFixed(2) + " wpm";
    document.getElementById("typing-corrections").textContent = "Corrections: " + corrections;

    const typing = { time: seconds.toFixed(2), speed: speed.toFixed(2), corrections: corrections };
    fetch("/collect", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(typing) });
});

document.getElementById("restart-button").addEventListener("click", function () {
    startTime = null;
    corrections = 0;
    input.value = "";
});
