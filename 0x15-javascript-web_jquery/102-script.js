const url = 'https://hellosalut.stefanbohacek.dev/';

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.getJSON(url, { lang: langCode }, (data) => {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation.');
    });
  });
});
