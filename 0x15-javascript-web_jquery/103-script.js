const url = 'https://hellosalut.stefanbohacek.dev/';
$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    $.getJSON(url, { lang: langCode }, (data) => {
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

/* $(document).ready(function() {
  function fetchTranslation() {
    var langCode = $('#language_code').val();
    var proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(proxyUrl + apiUrl, { lang: langCode }, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error fetching translation.');
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });
});
 */