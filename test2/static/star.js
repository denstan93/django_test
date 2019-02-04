$(document).ready(function () {
    $('#registration').click(function (e) {
        username = $('#input_user').val()
        password = $('#input_pass').val()
        if (username.length < 5 || password.length < 5) {
            alert('Введите имя пользователя или пароль корректно, больше 5 символов!')
            e.preventDefault()
        }
        else {
            alert('Hello ' + $('#input_user').val() + '!!!')
        }
    })


    $('#qwe').click(function (e) {

        $.post(
            "ajax_path",
            {
                'a' : 'Hello'
            },
            function (response) {
                alert(response.message)
            }
        );
    })


    $('#barbershop1').click(function (e) {
        $('form1').toggle();
        $('form2').hide();
        $('form1').enable();

    })

    $('#master1').click(function (e) {
        $('form2').toggle();
        $('form1').hide();
        $('form2').enable();
    })

});
