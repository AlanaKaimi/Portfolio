$('.moreless-button').click(function () {
  $('.moretext').slideToggle()
  if ($('.moreless-button').text() == '+') {
    $(this).text('-')
  } else {
    $(this).text('+')
  }
})
