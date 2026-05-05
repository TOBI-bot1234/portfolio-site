(function () {
  /* Sparkle effect on mouse hold.
     Small particles appear at the cursor when holding the mouse button
     on non-interactive surfaces. Respects prefers-reduced-motion. */

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) return;

  var MAX_PARTICLES = 24;
  var SPAWN_MS = 60;
  var interactiveTags = /^(A|BUTTON|INPUT|TEXTAREA|SELECT|LABEL|SUMMARY)$/;
  var active = false;
  var timer = null;
  var lastX = 0;
  var lastY = 0;
  var count = 0;
  var container = document.createElement('div');

  container.setAttribute('aria-hidden', 'true');
  container.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;overflow:hidden;';
  document.body.appendChild(container);

  function isInteractive(el) {
    while (el && el !== document.body) {
      if (interactiveTags.test(el.tagName)) return true;
      if (el.getAttribute('role') === 'button') return true;
      el = el.parentElement;
    }
    return false;
  }

  function spawn(x, y) {
    if (count >= MAX_PARTICLES) return;

    var el = document.createElement('span');
    el.className = 'sparkle';

    var angle = Math.random() * Math.PI * 2;
    var dist = 12 + Math.random() * 28;
    var dx = Math.cos(angle) * dist;
    var dy = Math.sin(angle) * dist;
    var size = 2 + Math.random() * 3;
    var rotation = Math.random() * 180 - 90;

    el.style.left = x + 'px';
    el.style.top = y + 'px';
    el.style.width = size + 'px';
    el.style.height = size + 'px';
    el.style.setProperty('--dx', dx + 'px');
    el.style.setProperty('--dy', dy + 'px');
    el.style.setProperty('--rot', rotation + 'deg');

    container.appendChild(el);
    count++;

    el.addEventListener('animationend', function () {
      el.remove();
      count--;
    });
  }

  function onDown(e) {
    if (e.button !== 0) return;
    if (isInteractive(e.target)) return;
    active = true;
    lastX = e.clientX;
    lastY = e.clientY;
    spawn(lastX, lastY);

    timer = setInterval(function () {
      spawn(lastX, lastY);
    }, SPAWN_MS);

    document.addEventListener('mousemove', onMove);
    document.addEventListener('pointerup', onUp);
    document.addEventListener('pointerleave', onUp);
  }

  function onMove(e) {
    if (!active) return;
    lastX = e.clientX;
    lastY = e.clientY;
    spawn(lastX, lastY);
  }

  function onUp() {
    active = false;
    if (timer) { clearInterval(timer); timer = null; }
    document.removeEventListener('mousemove', onMove);
    document.removeEventListener('pointerup', onUp);
    document.removeEventListener('pointerleave', onUp);
  }

  document.addEventListener('pointerdown', onDown);
})();
