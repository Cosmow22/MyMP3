const root   = document.getElementById('volume');
const btn    = document.getElementById('volume-btn');
const slider = document.getElementById('volume-slider');
const value  = document.getElementById('volume-value');
const wave1  = document.getElementById('wave-1');
const wave2  = document.getElementById('wave-2');
const mute   = document.getElementById('mute');

function setOpen(open) {
root.classList.toggle('is-open', open);
btn.setAttribute('aria-expanded', String(open));
}

function update() {
const v = Number(slider.value);
slider.style.setProperty('--v', v + '%');
value.textContent = v;
wave1.style.display = v > 0 ? '' : 'none';
wave2.style.display = v > 50 ? '' : 'none';
mute.style.display  = v === 0 ? '' : 'none';
// Ici : audio.volume = v / 100;
}

btn.addEventListener('click', () => setOpen(!root.classList.contains('is-open')));
slider.addEventListener('input', update);

// Fermer au clic à l’extérieur ou avec Échap
document.addEventListener('click', e => { if (!root.contains(e.target)) setOpen(false); });
document.addEventListener('keydown', e => {
if (e.key === 'Escape') { setOpen(false); btn.focus(); }
});

update();