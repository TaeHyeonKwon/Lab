<?php
	$conn=mysqli_connect('localhost','root','123456','awscop');
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
		<p>이름으로 검색하기</p>
		<p>
			<form action="search.php" method="post">
				<input type="text" name="name" placeholder="이름">
				<input type="submit" value="검색">
			</form>
		</p>
		<table>
			<thead>
				<tr>
					<th>id</th><th>이름</th><th>직급</th><th>기본급</th><th>수당</th><th>세율</th><th>월급</th><th></th><th></th>
				</tr>
			</thead>
			<tbody>

			<?php
				$filtered_name=mysqli_real_escape_string($conn,$_POST['name']);

				$sql = "SELECT * FROM 월급관리 WHERE 이름 LIKE '%{$filtered_name}%'";
				$result = mysqli_query($conn, $sql);
				while( $row = mysqli_fetch_array($result)) {
					$filtered = array(
						'id' => htmlspecialchars($row['id']),
						'이름' => htmlspecialchars($row['이름']),
						'직급' => htmlspecialchars($row['직급']),
						'기본급' => htmlspecialchars($row['기본급']),
						'수당' => htmlspecialchars($row['수당']),
						'세율' => htmlspecialchars($row['세율']),
						'월급' => htmlspecialchars($row['월급'])
					);
			?>
            
			<tr>
				<td><?= $filtered['id'] ?></td>
				<td><?= $filtered['이름'] ?></td>
				<td><?= $filtered['직급'] ?></td>
				<td><?= $filtered['기본급'] ?></td>
				<td><?= $filtered['수당'] ?></td>
				<td><?= $filtered['세율'] ?></td>
				<td><?= $filtered['월급'] ?></td>
				<td><a href="update.php?id=<?php echo $filtered['id'] ?>">수정</a></td>
				<td>
					<form action="delete.php" method="post" onsubmit="if(!confirm('정말 삭제하시겠습니까?')){return false;}">
						<input type="hidden" name="id" value="<?= $filtered['id'] ?>">
						<input type="submit" value="삭제">         
					</form>
				</td>
			</tr>
			<?php
				}
			?>
		</table>
	</div>
	<div>
		<h4>AWSCOP</h4>
		<p>TEL : 0212345678</p>
		<p>E-MAIL : aws123@gmail.com</p>
	</div>
</body>
</html>