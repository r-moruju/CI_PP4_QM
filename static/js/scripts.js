// Automatically dismiss messages as in CI Django 'code-star' project
setTimeout(function () {
    let message = document.getElementById('msg');
    let feedback = new bootstrap.Alert(message);
    feedback.close();
}, 3000);


// Activates Bootstarp Carousel as in Bootstrap documentation
const bookingsCarousel = document.querySelector('#bookings_carousel')
const carousel = new bootstrap.Carousel(bookingsCarousel, {
  ride: false
})


// Code from https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
// Use user rating and update average by calling 'rate' view
const rate = (rating, site_id) => {
  fetch(`/rate/${site_id}/${rating}/`, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json'
      }
  }).then(rest => {
      window.location.reload();
  })
}