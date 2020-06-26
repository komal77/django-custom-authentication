$(window).on("load", function() {
    $('.delete').click(function() {
    	id = $(this).attr('value')
        var url = "/delete/"+id
        
        csrf = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: url,
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': csrf,
                'id': id
            },
            success: function(data) {
                console.log(data)
            }
        });

    });

});

