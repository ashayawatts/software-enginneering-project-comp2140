// Touch/swipe photo gallery interactions for F-03 (Amanda Morgan)
// Swiping works natively (CSS scroll-snap); this script adds the prev/next buttons, the
// "Photo 2 of 3" counter, thumbnails, full-screen toggle and keyboard arrows.
(function () {
  "use strict";

  var gallery = document.getElementById("gallery");
  if (!gallery) { return; } // this vehicle has no photos

  var track = document.getElementById("gallery-track");
  var prevBtn = document.getElementById("gallery-prev");
  var nextBtn = document.getElementById("gallery-next");
  var expandBtn = document.getElementById("gallery-expand");
  var counter = document.getElementById("gallery-counter");
  var thumbs = Array.prototype.slice.call(document.querySelectorAll(".gallery-thumb"));
  var total = track.children.length;
  var index = 0;
  var settleTimer = null;

  function clamp(i) { return Math.max(0, Math.min(total - 1, i)); }

  function render(i) {
    index = clamp(i);
    counter.textContent = "Photo " + (index + 1) + " of " + total;
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === total - 1;
    thumbs.forEach(function (thumb, n) {
      thumb.classList.toggle("is-active", n === index);
    });
  }

  function scrollToSlide(i, smooth) {
    var left = clamp(i) * track.clientWidth;
    if (typeof track.scrollTo === "function") {
      track.scrollTo({ left: left, behavior: smooth ? "smooth" : "auto" });
    } else {
      track.scrollLeft = left;
    }
    render(i);
  }

  // After a swipe the browser snaps to a slide; read which one once scrolling settles.
  track.addEventListener("scroll", function () {
    window.clearTimeout(settleTimer);
    settleTimer = window.setTimeout(function () {
      render(Math.round(track.scrollLeft / track.clientWidth));
    }, 80);
  }, { passive: true });

  prevBtn.addEventListener("click", function () { scrollToSlide(index - 1, true); });
  nextBtn.addEventListener("click", function () { scrollToSlide(index + 1, true); });
  thumbs.forEach(function (thumb) {
    thumb.addEventListener("click", function () {
      scrollToSlide(parseInt(thumb.getAttribute("data-index"), 10), true);
    });
  });

  function setFullscreen(on) {
    gallery.classList.toggle("is-fullscreen", on);
    document.body.style.overflow = on ? "hidden" : "";
    expandBtn.setAttribute("aria-label", on ? "Close full screen" : "View photos full screen");
    expandBtn.innerHTML = on ? "&times;" : "&#10530;";
    // slide width changed, so line the current photo up again
    window.requestAnimationFrame(function () { scrollToSlide(index, false); });
  }

  expandBtn.addEventListener("click", function () {
    setFullscreen(!gallery.classList.contains("is-fullscreen"));
  });
  // tapping a photo opens it full screen; tapping again closes it
  Array.prototype.forEach.call(track.querySelectorAll("img"), function (img) {
    img.addEventListener("click", function () {
      setFullscreen(!gallery.classList.contains("is-fullscreen"));
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowLeft") { scrollToSlide(index - 1, true); }
    else if (event.key === "ArrowRight") { scrollToSlide(index + 1, true); }
    else if (event.key === "Escape" && gallery.classList.contains("is-fullscreen")) { setFullscreen(false); }
  });

  window.addEventListener("resize", function () { scrollToSlide(index, false); });

  render(0);
})();
