(function () {
  "use strict";
  document.documentElement.classList.add("js");

  function init() {
    var menu = document.querySelector(".main_menu");
    var toggles = document.querySelectorAll(".navbar-toggle");
    var primaryToggle = document.querySelector('.navbar-toggle[data-target=".main_menu.wsc_main"], .navbar-toggle:not(.wsc-offscreen-toggle)');

    if (menu && primaryToggle) {
      primaryToggle.setAttribute("aria-controls", "primary-navigation");
      menu.id = menu.id || "primary-navigation";
      primaryToggle.setAttribute("aria-expanded", "false");
      primaryToggle.addEventListener("click", function () {
        var open = menu.classList.toggle("is-open");
        primaryToggle.setAttribute("aria-expanded", String(open));
        document.body.classList.toggle("menu-open", open);
      });
    }

    // Mobile dropdowns: first tap opens, second tap follows the link.
    if (menu) {
      menu.querySelectorAll("li.sub > a, li.root.sub > a, li.category.sub > a").forEach(function (link) {
        link.addEventListener("click", function (event) {
          if (window.innerWidth > 991) return;
          var li = link.parentElement;
          if (!li.classList.contains("is-open")) {
            event.preventDefault();
            li.classList.add("is-open");
          }
        });
      });
      menu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
          if (window.innerWidth < 992 && !link.parentElement.classList.contains("sub")) {
            menu.classList.remove("is-open");
            document.body.classList.remove("menu-open");
            if (primaryToggle) primaryToggle.setAttribute("aria-expanded", "false");
          }
        });
      });
    }

    var top = document.querySelector(".go-top");
    if (top) {
      top.setAttribute("role", "button");
      top.setAttribute("tabindex", "0");
      var go = function () { window.scrollTo({ top: 0, behavior: "smooth" }); };
      top.addEventListener("click", function (e) { e.preventDefault(); go(); });
      top.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); } });
    }

    // Reveal a back-to-top control after scrolling.
    if (top) {
      window.addEventListener("scroll", function () {
        top.classList.toggle("is-visible", window.scrollY > 500);
      }, { passive: true });
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
