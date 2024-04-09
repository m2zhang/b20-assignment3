// Function to check if the user has scrolled to the bottom of the page
function isScrolledToBottom() {
    return window.innerHeight + window.scrollY >= document.body.offsetHeight;
}

// Function to show or hide the footer based on scroll position
function toggleFooterVisibility() {
    var footer = document.getElementById("myFooter");
    if (isScrolledToBottom()) {
        footer.style.position = "relative"; // Or whatever position you want when at the bottom
    } else {
        footer.style.position = "fixed";
        footer.style.bottom = "0";
        footer.style.left = "0";
        footer.style.width = "100%";
        footer.style.display = "inline"
    }
}

// Event listener for scroll events
window.addEventListener("scroll", function() {
    toggleFooterVisibility();
});

// Call the function initially to check the scroll position on page load
toggleFooterVisibility();
