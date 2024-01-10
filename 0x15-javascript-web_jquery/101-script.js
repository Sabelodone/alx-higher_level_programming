// This line adds an event listener to wait for the DOM content to be loaded before executing the enclosed function.
// This line selects the first 'HEADER' element in the document and changes its text color to red (#FF0000).

$('document').ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
