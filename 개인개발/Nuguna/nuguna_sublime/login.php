

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="style1.css">
    <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>

</head>
<body>
    <section class="login-form">
        <h1>NUGUNA</h1>
        <form action="login_process.php" method="post">
            <div class="int-area">
                <input type="email" name="id" id="signinID" autocomplete="off" required>
                <label for="signinID">USER NAME</label>
            </div>
            <div class="int-area">
                <input type="password" name="pw" id="signinPW" autocomplete="off" required>
                <label for="signinPW">PASSWORD</label>
            </div>
            <div class="btn-area-signin">
                <button id='btn' type="submit">Sign In</button>
            </div>
            <div class="btn-area-signup">
                <button type="button" onclick="location.href='signup.php'">Sign Up</button>
            </div>
        </form>
        <div class="caption">
            <a href="">Forgot Password?</a>
        </div>
    </section>

    <script>
        let id = $('#id');
        let pw = $('#pw');
        let btn = $('#btn');

        $(btn).on('click',function(){
            if($(id).val() == ""){
                $(id).next('label').addClass('warning');
                setTimeout(function(){
                    $('label').removeClass('warning');
                },1500)
            }
            else if($(pw).val ==""){
                $(pw).next('label').addClass('warning');
                setTimeout(function(){
                    $('label').removeClass('warning');
                },1500)
            }
        });
    </script>
</body>
</html>
