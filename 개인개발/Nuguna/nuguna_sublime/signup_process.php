<?php
    $conn=mysqli_connect('localhost','root','123456','nuguna');


    $filtered=array(
        'signUpEmail' => mysqli_real_escape_string($conn, $_POST['signUpEmail']),
        'signUpPassword' => mysqli_real_escape_string($conn, $_POST['signUpPassword'])
    );


    $sql="
        INSERT INTO userinfo (email,pw)
        VALUES (
            '{$filtered['signUpEmail']}',
            '{$filtered['signUpPassword']}'
        )"
    ;

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>NUGUNA</title>
</head>
<body>
    <div>
        <h1><a href="login.php">NUGUNA</a></h1>
    </div>
    <div>
        <?php
            $result=mysqli_query($conn, $sql);
            if($result === false) {
                echo '글 등록 오류가 발생하였습니다. 관리자에게 문의하세요.';
                echo error_log(mysqli_error($conn));
            } else {
            echo '정상적으로 등록되었습니다.<br><a href="login.php">로그인 페이지로 돌아가기</a>';
            }
        ?>
    </div>
    <div>
        <h4>NUGUNA</h4>
        <p>TEL : 0212345678</p>
        <p>E-MAIL : hollin@gmail.com</p>
    </div>
</body>
</html>