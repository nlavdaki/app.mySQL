$(document).on('click', '.edit-btn', function() {
    var photographerId = $(this).data('id');

    $.ajax({
        url: '/api/photographers/' + photographerId,
        method: 'GET',
        success: function(photographer) {
            // Update the form values
            $('#edit-id').val(photographerId);
            $('#edit-name').val(photographer.name);
            $('#edit-surname').val(photographer.surname);
            $('#edit-birthday').val(new Date(photographer.birthday).toISOString().split('T')[0]);
            $('#edit-deathday').val(photographer.deathday ? new Date(photographer.deathday).toISOString().split('T')[0] : '');
            $('#edit-cv').val(photographer.cv);

            // Show the edit form
            $('#edit-form').show();
            // Hide the search form
            $('#search-form').hide();
        }
    });
});

$('#edit-form').submit(function(event) {
    event.preventDefault();

    var id = $('#edit-id').val();
    var name = $('#edit-name').val();
    var surname = $('#edit-surname').val();
    var birthday = $('#edit-birthday').val();
    var deathday = $('#edit-deathday').val();
    var cv = $('#edit-cv').val();

    $.ajax({
        url: '/api/photographers/' + id,
        method: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify({
            name: name,
            surname: surname,
            birthday: birthday,
            deathday: deathday,
            cv: cv
        }),
        success: function(response) {
            $('#edit-form').hide(); // Hide the edit form
            $('#search-form').show(); // Show the search form again
            $('#search-form').submit(); // Submit the search form to refresh the results
            alert(response.message);
        }
    });
});

$('#cancel-btn').click(function() {
    // Hide the edit form
    $('#edit-form').hide();
    // Show the search form
    $('#search-form').show();
});
