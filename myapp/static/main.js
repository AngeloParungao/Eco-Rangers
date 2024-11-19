const navFullScreen = document.getElementById("navigation-full-screen");
const welcomeText = document.getElementById("welcome-text");
const elfContainer = document.getElementById("elf-container");
const elfButton = document.getElementById("elf-button");
const globeContainer = document.getElementById("globe-container");
const globeImage = document.getElementById("globe-image");
const elfMessage = document.getElementById("elf-message");

const elfMessageText = [
    "Welcome to the planet Earth!",
    "The planet Earth is a wonderful place to live and explore!",
    "But the earth is being destroyed by climate change!",
    "We need to save our planet!",
    "Join us on this exciting journey!",
];

let messageIndex = 0; // Keep track of the current message index
let initialLoad = sessionStorage.getItem("initialLoad") === "true"; // Retrieve state

// Initialize elements based on `initialLoad`
window.addEventListener("DOMContentLoaded", () => {
    if (initialLoad) {
        // When `initialLoad` is true
        welcomeText.classList.remove("opacity-0");
        elfButton.classList.remove("hidden");
        elfContainer.classList.add("hidden"); // Ensure elfContainer is hidden
        globeContainer.classList.add("h-[100%]");
        globeContainer.classList.remove("translate-y-[40%]");
        globeImage.classList.add("animate-spin");
        document.body.style.overflow = "auto";
    } else {
        // When `initialLoad` is false
        navFullScreen.classList.add("translate-y-[-100%]");
        welcomeText.classList.add("hidden");
        welcomeText.classList.add("opacity-0");
        elfButton.classList.add("hidden");
        elfContainer.classList.remove("hidden"); // Ensure elfContainer is visible
        globeContainer.classList.add("translate-y-[40%]");
        globeContainer.classList.remove("h-[100%]");
        globeImage.classList.remove("animate-spin");
        document.body.style.overflow = "hidden";
    }
});

// Display the next message on elfContainer click
elfContainer.addEventListener("click", () => {
    if (messageIndex < elfMessageText.length) {
        elfMessage.innerText = elfMessageText[messageIndex];
        messageIndex++;
    }
    if (messageIndex === elfMessageText.length) {
        elfButton.classList.remove("hidden");
    }
});


// Handle first-time load
function toggleLoad() {
    initialLoad = true;
    sessionStorage.setItem("initialLoad", "true"); // Save state in sessionStorage
    navFullScreen.classList.remove("translate-y-[-100%]");
    welcomeText.classList.remove("hidden");
    welcomeText.classList.remove("opacity-0");
    navFullScreen.classList.remove("hidden");
    elfContainer.classList.add("hidden");
    globeContainer.classList.add("h-[100%]");
    globeContainer.classList.remove("translate-y-[40%]");
    globeImage.classList.add("animate-spin");
    document.body.style.overflow = "auto";
}

// Toggle the menu on small screens
function toggleMenu() {
    const nav = document.getElementById("navigation");
    nav.classList.toggle("left-[0]");
}

// Toggle the topics
function toggleTopics(articleId) {
    const seeTopics = document.getElementById(`see-topics-${articleId}`);
    const closeTopics = document.getElementById(`close-topics-${articleId}`);
    const topics = document.getElementById(`topics-${articleId}`);

    // Toggle visibility of the 'see' and 'close' buttons
    seeTopics.classList.toggle("hidden");
    closeTopics.classList.toggle("hidden");

    // Toggle visibility and transition for topics
    if (topics.classList.contains("max-h-0")) {
        topics.classList.remove("max-h-0");
        topics.classList.add("max-h-screen");
    } else {
        topics.classList.remove("max-h-screen");
        topics.classList.add("max-h-0");
    }
}



