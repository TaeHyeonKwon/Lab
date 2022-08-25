<?php
	$conn=mysqli_connect('localhost','root','123456','awscop');

	settype($_GET['id'], 'integer');
	$a=$_GET['id'];
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
			$sql="SELECT * FROM 월급관리 WHERE id=$a";
			$result=mysqli_query($conn, $sql);
			$row = mysqli_fetch_array($result);
			$filtered = array(
				'이름' => htmlspecialchars($row['이름']),
				'직급' => htmlspecialchars($row['직급']),
				'기본급' => htmlspecialchars($row['기본급']),
				'수당' => htmlspecialchars($row['수당'])
			);
		?>
		<form action="update_process.php?id=<?php echo $_GET['id'] ?>" method="post">
			<p><input type="text" name="name" placeholder="이름" value="<?= $filtered['이름'] ?>"></p>
			<p><input type="text" name="rank" placeholder="직급" value="<?= $filtered['직급'] ?>"></p>
			<p><input type="text" name="basic" placeholder="기본급" value="<?= $filtered['기본급'] ?>"></p>
			<p><input type="text" name="extra" placeholder="수당" value="<?= $filtered['수당'] ?>"></p>
			<p><input type="submit" value="수정"></p>
		</form>
	</div>
	<div>
		<h4>AWSCOP</h4>
		<p>TEL : 0212345678</p>
		<p>E-MAIL : aws123@gmail.com</p>
	</div>
</body>
</html>