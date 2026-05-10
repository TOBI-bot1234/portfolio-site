(function () {
  if (document.querySelector('.site-footer')) return;

  var footer = document.createElement('footer');
  footer.className = 'site-footer';
  footer.setAttribute('role', 'contentinfo');

  var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('class', 'site-footer-mark');
  svg.setAttribute('viewBox', '0 0 24 12');
  svg.setAttribute('width', '18');
  svg.setAttribute('height', '9');
  svg.setAttribute('fill', 'none');
  svg.setAttribute('stroke', 'currentColor');
  svg.setAttribute('stroke-width', '1.6');
  svg.setAttribute('stroke-linecap', 'round');
  svg.setAttribute('aria-hidden', 'true');
  svg.setAttribute('focusable', 'false');

  var paths = [
    'M2 9 C 5 4, 7 9, 10 5',
    'M12 8 C 14 5, 16 9, 18 6',
    'M20 7 L 22 5'
  ];

  for (var i = 0; i < paths.length; i++) {
    var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', paths[i]);
    svg.appendChild(path);
  }

  var text = document.createElement('span');
  text.className = 'site-footer-text';
  text.textContent = 'made by hand \u00b7 ' + new Date().getFullYear();

  footer.appendChild(svg);
  footer.appendChild(text);
  document.body.appendChild(footer);
})();
