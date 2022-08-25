<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
    <?php
      //<!--php부분 form에 입력한 내용을 데이터베이스와 비교해서 로그인 여부를 알려준다.-->
      if(isset($_POST['signinID'])&&isset($_POST['signinPW'])){//post방식으로 데이터가 보내졌는지?
        $username=$_POST['signinID'];//post방식으로 보낸 데이터를 username이라는 변수에 넣는다.
        $userpw=$_POST['signinPW'];//post방식으로 보낸 데이터를 userpw라는 변수에 넣는다.
        //mysql root계정으로 접속.
        //비밀번호는 123456이다.
        //study라는 데이터베이스에 접근.
        $conn= mysqli_connect('localhost', 'hollin', '123456', 'userinfo');
        if($conn->connect_error) echo "<h2> 접속에 실패하였습니다</h2>";
        else echo "<h2> 접속에 성공하였습니다</h2>";
        //sql문을 sql변수에 저장해놓는다.
        $sql="SELECT * FROM blogin where login_id='$username'&&login_pw='$userpw'";
        if($result=mysqli_fetch_array(mysqli_query($conn,$sql))){//쿼리문을 실행해서 결과가 있으면 로그인 성공
          echo "사용자 이름= $username";
          echo "</br>".$result['created'];
          echo "</br>로그인 성공";
        }
        else{//쿼리문의 결과가 없으면 로그인 fail을 출력한다.
          echo "login fail";
        }
      }
    ?>
</head>
<body>
    <section class="login-form">
        <h1>NUGUNA</h1>
        <form action="">
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
                <button type="button" onclick="location.href='signup.html'">Sign Up</button>
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

   <!--  <script type="module">
        // Import the functions you need from the SDKs you need
        import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.0/firebase-app.js";
        import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.9.0/firebase-analytics.js";
        // TODO: Add SDKs for Firebase products that you want to use
        // https://firebase.google.com/docs/web/setup#available-libraries
      
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {
          apiKey: "AIzaSyCwwLm0D1fCWchXpuNigdPzkmK-awiRqWo",
          authDomain: "nuguna1-e84f8.firebaseapp.com",
          projectId: "nuguna1-e84f8",
          storageBucket: "nuguna1-e84f8.appspot.com",
          messagingSenderId: "827689316231",
          appId: "1:827689316231:web:48a5c69d816345741aed22",
          measurementId: "G-0SDD2DDTGR"
        };
      
        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const analytics = getAnalytics(app);

        import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.9.0/firebase-auth.js";


        document.getElementById('btn').addEventListener('click', (event) => {
            event.preventDefault()
            const email = document.getElementById('signinID').value
            const password = document.getElementById('signinPW').value
            const auth = getAuth();
            signInWithEmailAndPassword(auth, email, password)
                .then((userCredential) => {
                console.log(userCredential)
                // Signed in
                const user = userCredential.user;
                location.href='Mainpage.html'
                // ...
                })
                .catch((error) => {
                console.log('failed log in')
                const errorCode = error.code;
                const errorMessage = error.message;
                });
        })

        console.log('hello world')
        console.log(app)
    </script> -->


</body>
</html>
