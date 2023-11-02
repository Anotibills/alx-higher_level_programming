/* a JavaScript script that toggles the class of the <header> element
 * The <header> element must always have one class: red or green
 * If the current class is red, when the user click on DIV#toggle_header
 * can’t use document.querySelector to select the HTML tag
 */
$('#toggle_header').on('click', function () {
  $('header').toggleClass('green red');
});
