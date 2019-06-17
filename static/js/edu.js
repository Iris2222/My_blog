$(function () {
  $(document).scroll(function () {
    var $nav = $("nav");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    var $link = $(".nav-link");
    $link.toggleClass('scrolled', $(this).scrollTop() > $link.height());
    var $linkv = $(".linkv");
    $linkv.toggleClass('scrolled', $(this).scrollTop() > $linkv.height());
  });
});
