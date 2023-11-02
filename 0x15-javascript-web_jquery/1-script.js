/* script that updates the text color of the <header> element to red (#FF0000)
 * can’t use document.querySelector to select the HTML tag
 * must use the JQuery API
 */

$(document).ready(function () {
  $('header').addClass('red-text');
});
