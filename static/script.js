document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll("section");

  const revealSection = () => {
    sections.forEach((section) => {
      const sectionTop = section.getBoundingClientRect().top;
      if (sectionTop < window.innerHeight - 100) {
        section.classList.add("visible");
      }
    });
  };

  revealSection();
  window.addEventListener("scroll", revealSection);
});
