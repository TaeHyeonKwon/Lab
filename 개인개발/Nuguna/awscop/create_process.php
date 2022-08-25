<?php
	$conn=mysqli_connect('localhost','root','123456','awscop');

	$basic=$_POST['basic'];
	$extra=$_POST['extra'];

	if ($basic <=2000000){
		$tax=0.01;
	}
	elseif ($basic<=4000000) {
		$tax=0.02;
	}
	else {
		$tax=0.03;
	}

	$salary=($basic+$extra)*(1-$tax);

	$filtered=array(
		'name' => mysqli_real_escape_string($conn, $_POST['name']),
		'rank' => mysqli_real_escape_string($conn, $_POST['rank']),
		'basic' => mysqli_real_escape_string($conn, $basic),
		'extra' => mysqli_real_escape_string($conn, $extra)
	);

	$sql="
		INSERT INTO 월급관리 (이름, 직급, 기본급, 수당, 세율, 월급)
		VALUES (
			'{$filtered['name']}',
			'{$filtered['rank']}',
			'{$filtered['basic']}',
			'{$filtered['extra']}',
			$tax,
			$salary
		)"
	;

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>AWSCOP</title>
</head>
<body>
	<div>
		<h1><a href="index.php">AWSCOP</a></h1>
	</div>
	<div>
		<?php
			$result=mysqli_query($conn, $sql);
			if($result === false) {
				echo '글 등록 오류가 발생하였습니다. 관리자에게 문의하세요.';
				echo error_log(mysqli_error($conn));
			} else {
			echo '정상적으로 등록되었습니다.<br><a href="index.php">메인 페이지로 돌아가기</a>';
			}
		?>
	</div>
	<div>
		<h4>AWSCOP</h4>
		<p>TEL : 0212345678</p>
		<p>E-MAIL : aws123@gmail.com</p>
	</div>
</body>
</html>