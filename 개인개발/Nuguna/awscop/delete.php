<?php
	$conn=mysqli_connect('localhost','root','123456','awscop');

	settype($_POST['id'], 'integer');
	$filtered = array(
		'id' => mysqli_real_escape_string($conn, $_POST['id'])
	);

	$sql = "
		DELETE FROM 월급관리 WHERE id = '{$filtered['id']}'
		";

	$result = mysqli_multi_query($conn, $sql);
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
			if($result === false) {
				echo '삭제하는 과정에서 오류가 발생하였습니다. 관리자에게 문의하세요.';
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