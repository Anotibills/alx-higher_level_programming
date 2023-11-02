/*JavaScript script that fetches and prints how to say “Hello” depending on the language
 API service: https://www.fourtonfish.com/hellosalut/hello/
 */
$(function () {
  $('#btn_translate').click(translate);
  $('#language_code').on('keydown', function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
    $('#hello').html(data.hello);
  });
}
