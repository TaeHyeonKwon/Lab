<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>signup</title>
    <link rel="stylesheet" href="style2.css">
</head>
<body>
    <section class="signup-form">
        <form action="signup_process.php" method="post">
            <h1>SIGN UP</h1>
            <div class="int-area">
                <input type="email" name="signUpEmail"  autocomplete="off" required>
                <label for="signUpEmail">EMAIL</label>
            </div>
            <div class="int-area">
                <input type="password" name="signUpPassword"  autocomplete="off" required>
                <label for="signUpPassword">PASSWORD</label>
            </div>
            <div class="btn-area-register">
                <button id='signUpButton' type="submit">Register</button>
            </div>
            <div class="btn-area-gotosignin">
                <button type="button" onclick="location.href='login.php'">Go to Sign In</button>
            </div>
        </form>
    </section> 
</body>
</html>