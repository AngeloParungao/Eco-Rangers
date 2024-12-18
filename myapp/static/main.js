const navFullScreen = document.getElementById("navigation-full-screen");
const welcomeText = document.getElementById("welcome-text");
const elfContainer = document.getElementById("elf-container");
const arrowIndicator = document.getElementById("arrow-indicator");
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
    
    const girlMessage = document.getElementById("girl-message");
    const boyMessage = document.getElementById("boy-message");

    const girlMessageText = [
        "This is some articles",
        "That will help you",
        "Learn more about",
        "Our planet",
        "As we grow",
        "Together",
    ];

    const boyMessageText = [
        "Let's play some fun games!",
        "With our friends!",
        "And our cats!",
        "Together!",
    ]

    let girlMessageIndex = 0;
    let boyMessageIndex = 0;

    if (girlMessage) {
        setInterval(() => {
            // Update the text
            girlMessage.innerText = girlMessageText[girlMessageIndex];
            // Increment index and loop back to the start
            girlMessageIndex = (girlMessageIndex + 1) % girlMessageText.length;
        }, 2000); // Update every 2 seconds
    }
    if (boyMessage) {
        setInterval(() => {
            // Update the text
            boyMessage.innerText = boyMessageText[boyMessageIndex];
            // Increment index and loop back to the start
            boyMessageIndex = (boyMessageIndex + 1) % boyMessageText.length;
        }, 2000); // Update every 2 seconds
    }


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
        arrowIndicator.classList.add("hidden");
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

 function filterVideos() {
    const selectedCategory = document.getElementById("video_category").value;
    const videos = document.querySelectorAll("#video_container > div");

    videos.forEach(video => {
      const category = video.getAttribute("data-category");
      if (selectedCategory === "all" || category === selectedCategory) {
        video.style.display = "flex"; // Show the video
      } else {
        video.style.display = "none"; // Hide the video
      }
    });
  }

function openModal(src) {
    const modal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');
    const downloadButton = document.getElementById('downloadButton');

    modalImage.src = src; // Set the modal image source
    downloadButton.href = src; // Set the download button link to the image source

    modal.classList.remove('hidden');
}

function closeModal() {
    const modal = document.getElementById('imageModal');
    modal.classList.add('hidden');
}
