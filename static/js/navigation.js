function setActive(element) {
    document.querySelectorAll('nav a').forEach(link => {
        link.classList.remove('active');
    });

    element.classList.add('active');
}