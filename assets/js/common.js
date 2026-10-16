$(document).ready(function() {
    $('button.abstract, button.bibtex').click(function() {
        var target = document.getElementById(this.getAttribute('aria-controls'));
        if (target) {
            target.classList.toggle('open');
            this.setAttribute('aria-expanded', target.classList.contains('open'));
        }
    });
    $('a').removeClass('waves-effect waves-light');
});
