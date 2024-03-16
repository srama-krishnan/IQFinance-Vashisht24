document.addEventListener('mousemove', function(e) {
    var x = e.clientX;
    var y = e.clientY;
    document.body.style.setProperty('--cursor-x', x + 'px');
    document.body.style.setProperty('--cursor-y', y + 'px');
  });