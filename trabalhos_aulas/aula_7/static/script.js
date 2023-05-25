$(document).ready(function () {
    $('#example').DataTable();
});

function handleDeleteTerm(term) {
    $.ajax("term/"+term, {
        type: "DELETE"
    })
    .then((response) => {
        console.log(response);
        window.location.reload();
    })
}