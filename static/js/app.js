document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    const currentPage = window.location.pathname;

    navLinks.forEach(function(link) {
      if (link.getAttribute("href") === currentPage) {
        link.classList.add("active");
      }

      link.addEventListener("click", function(event) {
        navLinks.forEach(function(navLink) {
          navLink.classList.remove("active");
        });

        this.classList.add("active");
      });
    });
  });