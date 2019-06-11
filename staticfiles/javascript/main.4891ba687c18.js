// functions that create shortcuts:
function qS(selector) {
  return document.querySelector(selector)
}

function qSA(selector) {
  return document.querySelectorAll(selector)
}

// more/less Button toggle

$('.more').click(function () {
  if ($(this).text() === '+') {
    $(this).text('-')
  } else {
    $(this).text('+')
  }
})