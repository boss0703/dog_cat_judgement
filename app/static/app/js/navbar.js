document.querySelector('.navbar-toggler').onclick = function() {
    // if menu is opening, close menu
    if(document.getElementById('navbarNav').classList.contains('show')) {
        document.querySelector('#navbarNav').classList.remove('show');
    } else {
      document.querySelector('#navbarNav').classList.add('show');
    }
}