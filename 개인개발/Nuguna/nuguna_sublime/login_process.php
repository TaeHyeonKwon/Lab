<?php
    if(isset($_POST['id'])&&isset($_POST['pw'])){
        $useremail = $_POST['id'];
        $userpw = $_POST['pw'];


        $conn=mysqli_connect('localhost','root','123456','nuguna');
        $sql="SELECT * FROM userinfo where email='$useremail'&& pw='$userpw'";
        
  }
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
            if($result=mysqli_fetch_array(mysqli_query($conn,$sql))){
              // echo '로그인 성공 <br><a href="mainpage.php">메인페이지로 들어가기</a>';
                header( 'Location: mainpage.php' );
            }
            else{
              echo '로그인 실패 <br><a href="login.php">로그인페이지로 돌어가기</a>';
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
