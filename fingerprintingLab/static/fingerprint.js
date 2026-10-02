const features = {
    language: navigator.language,
    cores: navigator.hardwareConcurrency,
    screen: screen.width + "x" + screen.height,
    window: window.innerWidth + "x" + window.innerHeight,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
};

document.getElementById("feature-output").textContent = JSON.stringify(features, null, 2);

fetch("/collect", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(features) });

// Fingerprint: SHA-256 of the features joined in a fixed order
const combined = Object.values(features).join(" | ");

crypto.subtle.digest("SHA-256", new TextEncoder().encode(combined)).then(function (buffer) {
    const hash = Array.from(new Uint8Array(buffer)).map(b => b.toString(16).padStart(2, "0")).join("");
    document.getElementById("fingerprint-output").textContent = "Fingerprint: " + hash;
    fetch("/collect", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ fp: hash }) });
});
