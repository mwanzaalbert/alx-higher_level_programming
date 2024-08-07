$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation.');
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when Enter is pressed in the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });
});
