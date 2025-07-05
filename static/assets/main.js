// static/js/main.js
function toggleTheme() {
  const body = document.body;
  const button = document.querySelector('.toggle-btn');

  // Apply dark mode
  body.classList.toggle('dark-mode');

  // Animate the button (rotate)
  button.classList.add('animate');
  setTimeout(() => {
    button.classList.remove('animate');
  }, 500); // match transition time

  // Store preference
  localStorage.setItem("theme", body.classList.contains("dark-mode") ? "dark" : "light");
}

// Load stored theme and add fade-in effect
window.onload = () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
  }
  document.body.classList.add("fade-in");
}
