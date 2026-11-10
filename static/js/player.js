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
