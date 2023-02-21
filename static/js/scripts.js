setTimeout(function () {
    let message = document.getElementById('msg');
    let alert = new bootstrap.Alert(message);
    alert.close();
}, 3000);


const bookingsCarousel = document.querySelector('#bookings_carousel')
const carousel = new bootstrap.Carousel(bookingsCarousel, {
  ride: false
})

