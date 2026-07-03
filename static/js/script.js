// This file is for small front-end interactivity.
// Bootstrap's own JS handles the carousel auto-scroll,
// so we don't need extra code for that.

// Example: pause the carousel when the user hovers over it,
// so they can read the card without it sliding away.
document.addEventListener('DOMContentLoaded', function () {
    const carouselEl = document.getElementById('projectsCarousel');

    if (carouselEl) {
        const carousel = bootstrap.Carousel.getOrCreateInstance(carouselEl);

        carouselEl.addEventListener('mouseenter', function () {
            carousel.pause();
        });

        carouselEl.addEventListener('mouseleave', function () {
            carousel.cycle();
        });
    }
});
