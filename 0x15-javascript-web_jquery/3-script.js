/*a JavaScript script that adds the class red to the <header> element
 *can’t use document.querySelector to select the HTML tag
 */
$('#red_header').on('click', function () {
  $('header').addClass('red');
});

