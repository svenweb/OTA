$(document).ready(function(){


});

function deleteListing(elem){
    $('#deleteModalText').text("Are you sure you want to delete " + $(elem).closest('tr').children('td.postTitle').text() + " ?");
    post_id = $(elem).closest('tr').children('td.postID').text()
    $(document).on("click", "#deleteModalBtn", function(){
        fetch('/deletepost/' + post_id, {
            method: 'DELETE'
        })
        
        $(elem).parents("tr").remove();
        $('#exampleModal').modal('hide');

        

        
    })
}