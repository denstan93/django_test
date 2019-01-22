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
});