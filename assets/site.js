(function () {
  var menu = document.getElementById('menu'), openBtn = document.getElementById('menu-open'), closeBtn = document.getElementById('menu-close');
  if (!menu || !openBtn) return;
  function open() {
    menu.hidden = false;
    requestAnimationFrame(function () { menu.classList.add('is-open'); });
    document.body.classList.add('pc-locked');
    openBtn.setAttribute('aria-expanded', 'true');
    closeBtn.focus();
  }
  function close(returnFocus) {
    menu.classList.remove('is-open');
    document.body.classList.remove('pc-locked');
    openBtn.setAttribute('aria-expanded', 'false');
    setTimeout(function () { menu.hidden = true; }, 300);
    if (returnFocus) openBtn.focus();
  }
  openBtn.addEventListener('click', open);
  closeBtn.addEventListener('click', function () { close(true); });
  menu.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { close(true); return; }
    if (e.key !== 'Tab') return;
    var f = menu.querySelectorAll('a[href], button');
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
  menu.addEventListener('click', function (e) { var a = e.target.closest('a[href]'); if (a) close(false); });
})();
