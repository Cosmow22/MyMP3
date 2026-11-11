const audio = document.getElementById("audio-player");
const playBtn = document.getElementById("play-btn");

playBtn.addEventListener("click", () => {
    if (audio.paused) {
        audio.play();
        playBtn.innerHTML = '<i class="ph-fill ph-pause"></i>';
    } else {
        audio.pause();
        playBtn.innerHTML = '<i class="ph-fill ph-play"></i>';
    }
});


const progress = document.getElementById("progress");
const currentTime = document.getElementById("current-time");

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);

    return `${minutes}:${String(remainingSeconds).padStart(2, "0")}`;
}


audio.addEventListener("loadedmetadata", () => {
    duration.textContent = formatTime(audio.duration);
});

audio.addEventListener("timeupdate", () => {
    progress.value = (audio.currentTime / audio.duration) * 100;
    currentTime.textContent = formatTime(audio.currentTime);
});

progress.addEventListener("input", () => {
    audio.currentTime = (progress.value / 100) * audio.duration;
});

const volumeSlider = document.getElementById("volume-slider");
const volumeValue = document.getElementById("volume-value");
const volumeBtn = document.getElementById("volume-btn");  

volumeSlider.addEventListener("input", () => {
    const value = volumeSlider.value;

    // Modifier le volume (0 à 1)
    audio.volume = value / 100;

    // Afficher la valeur
    volumeValue.textContent = value;

});