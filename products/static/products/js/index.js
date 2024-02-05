
let button = document.getElementById("discoveryButton")
let url = document.getElementById("discoveryButton").getAttribute('data-static-url')
button.addEventListener("click", function() {
    window.open(url, '_self')
});


let aboutbtn = document.getElementById("aboutButton")
let url_about = document.getElementById("aboutButton").getAttribute('data-static-url')

aboutbtn.addEventListener("click", function() {
    window.open(url_about, '_self')
});
