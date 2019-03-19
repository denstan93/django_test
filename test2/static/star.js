$(document).ready(function (e) {

    $('#barbershop1').click(function (e) {
        $('#barbershop2').toggle();
        $('#master2').hide();
        $('#client2').hide();
        $('#name_barbershop').prop('disabled',false);
        $('#address').prop('disabled',false);
        $('#working_hours').prop('disabled',false);
    });

    $('#master1').click(function (e) {
        $('#master2').toggle();
        $('#barbershop2').hide();
        $('#client2').hide();
        $('#name_master').prop('disabled',false);
        $('#work_place').prop('disabled',false);
        $('#experience').prop('disabled',false);
        $('#experience').prop('required', false)
    });

    $('#client1').click(function (e) {
        $('#client2').toggle();
        $('#master2').hide();
        $('#barbershop2').hide();
        $('#name_client').prop('disabled',false);
    });

    $('#qwe').click(function (e) {
        $.post(
            "ajax_path",
            {
                'a': 'hello'
            },
            function (response) {
                alert(response.message)
            }
        );
    })

});

