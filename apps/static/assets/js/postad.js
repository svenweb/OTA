

$(".inputOption").on('click', function(event){
    console.log($(this).text());
    var dropdownBtn = $(this).parents(':eq(1)').find('.btn');
    dropdownBtn.text($(this).text() + '  ⌄');
    event.preventDefault();
    //(... rest of your JS code)
});

function setSelectedAttr(btn, inputId) {
    document.getElementById(inputId).value = btn.textContent;
    console.log(document.getElementById(inputId).value + ' yes')
}
