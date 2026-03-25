const searchInput = document.getElementById("searchInput");
const trendingBox = document.getElementById("trendingBox");

// open on click
searchInput.addEventListener("click", (e) => {
    e.stopPropagation();
    trendingBox.style.display = "block";
});

// prevent close when clicking inside list
trendingBox.addEventListener("click", (e) => {
    e.stopPropagation();
});

// close when clicking outside
document.addEventListener("click", () => {
    trendingBox.style.display = "none";
});
