document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.carousel-image');
    let currentIndex = 0;

    function showImage(index) {
        images.forEach((img, i) => {
            img.classList.toggle('active', i === index);
        });
    }

    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }

    showImage(currentIndex);
    setInterval(nextImage, 4000); // Cambia cada 4 segundos
});

document.addEventListener('DOMContentLoaded', () => {
  const buyButtons = document.querySelectorAll('.buy-btn');

  buyButtons.forEach(button => {
    button.addEventListener('click', () => {
      alert('Función en desarrollo');
    });
  });
});

