document.addEventListener("DOMContentLoaded", function() {
  var departmentLink = document.querySelector(".header_content_inner .main_nav .active");
  var dropdown = departmentLink.querySelector(".dropdown");

  departmentLink.addEventListener("mouseenter", function() {
    dropdown.style.display = "block";
  });

  departmentLink.addEventListener("mouseleave", function() {
    dropdown.style.display = "none";
  });
});
