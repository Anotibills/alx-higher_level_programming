/*JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
 The new element is: <li>Item</li>
 The new element added to UL.my_list
 the user clicks on DIV#add_item: a new element is added to the list
 the user clicks on DIV#remove_item: the last element is removed from the list
 the user clicks on DIV#clear_list: all elements of the list are removed*/
$(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
