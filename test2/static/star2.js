$(document).ready(function (e) {

    $('#barbershop1').click(function (e) {
        $('#barbershop2').toggle();
        $('#master2').hide();
        $('#client2').hide();
//        $('#barbershop2').attr();

    });

    $('#master1').click(function (e) {
        $('#master2').toggle();
        $('#barbershop2').hide();
        $('#client2').hide();
//        $('#master2').enable();
    });

    $('#client1').click(function (e) {
        $('#client2').toggle();
        $('#master2').hide();
        $('#barbershop2').hide();
//        $('#client2').toggleClass();
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

})

