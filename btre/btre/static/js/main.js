const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $('#messages').fadeOut('slow');
}, 3000);