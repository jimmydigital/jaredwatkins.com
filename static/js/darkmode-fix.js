// Sync the darkmode class on <html> whenever the theme toggles it on <body>.
// This is needed because the inline anti-FOUC script sets the class on <html>
// (the only element available synchronously in <head>), but the theme's
// script.js toggles it on document.body. We keep both in sync so the toggle
// correctly removes the dark scheme.
(function () {
  var html = document.documentElement;
  var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (m) {
      if (m.attributeName === 'class') {
        // body class changed — mirror darkmode onto <html>
        if (document.body.classList.contains('darkmode')) {
          html.classList.add('darkmode');
        } else {
          html.classList.remove('darkmode');
        }
      }
    });
  });

  document.addEventListener('DOMContentLoaded', function () {
    observer.observe(document.body, { attributes: true });
    // Initial sync in case deferred script already ran
    if (document.body.classList.contains('darkmode')) {
      html.classList.add('darkmode');
    } else {
      html.classList.remove('darkmode');
    }
  });
})();
