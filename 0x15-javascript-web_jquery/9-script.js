/*JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
 displays the value of hello from that fetch in the HTML tag DIV#hello
 The translation of “hello” must be displayed in the HTML tag DIV#hello
 can’t use document.querySelector to select the HTML tag*/
$.getJSON('https://fourtonfish.com/hellosalut/?lang=' + document.documentElement.lang, function (data) {
  $('#hello').text(data.hello);
});
