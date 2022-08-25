<?php
	$conn=mysqli_connect('localhost','root','123456','awscop');

	settype($_GET['id'], 'integer');

	$basic=$_POST['basic'];
	$extra=$_POST['extra'];

	if ($basic <= 2000000){
		$tax=0.01;
	}
	elseif ($basic <= 4000000) {
		$tax=0.02;
	}
	else {
		$tax=0.03;
	}

	$salary=($basic+$extra)*(1-$tax);

	$filtered=array(
		'id' => mysqli_real_escape_string($conn, $_GET['id']),
		'name' => mysqli_real_escape_string($conn, $_POST['name']),
		'rank' => mysqli_real_escape_string($conn, $_POST['rank']),
	);

	$sql="
		UPDATE 월급관리
		SET 이름='{$filtered['name']}',직급='{$filtered['rank']}',기본급=$basic,수당=$extra,세율=$tax,월급=$salary
		WHERE id='{$filtered['id']}';
		"
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
				echo '글 수정 오류가 발생하였습니다. 관리자에게 문의하세요.';
				echo error_log(mysqli_error($conn));
			} else {
				header('Location: print.php');
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