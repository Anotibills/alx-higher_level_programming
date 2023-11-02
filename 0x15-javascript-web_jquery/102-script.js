/*JavaScript script that fetches and prints how to say “Hello” depending on the language
 should use this API service: https://www.fourtonfish.com/hellosalut/hello/
 */
$(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.get(url + $.param({ lang: langCode }), function (data) {
      $('#hello').html(data.hello);
    });
  });
});
