<?php
	include "dbconnect.php";
	$admin_check = "SELECT id FROM member WHERE id = 'admin' ";
    $result = @mysqli_fetch_array(mysqli_query($db,$admin_check));
    if(!$result['id'])
    {
    	$sql = "INSERT INTO member VALUES('admin','dnjs6033^^','admin','1')";
    	$db->query($sql);
    }
    include "check.php";
    if($chk == True)
    {
    	$user_check = "SELECT id FROM member WHERE id = '{$_SESSION["username"]}' ";
    	$res = @mysqli_fetch_array(mysqli_query($db,$user_check));
    	if($res['id'])
    	{
    		if($_SESSION['username']=='admin')
    		{
    			header("Location: /admin.php");
    		}
    		else
    		{
    			header("Location: /user.php");
    		}
    	}
    }
?>

<!DOCTYPE html>
<html>
<head>
	<title>Main Page</title>
	<link rel="stylesheet" href="bootstrap/css/bootstrap1.min.css">
</head>

<body>

<div class="container">
	<p>
	<h2 align="center">Comibear's Website</h2><hr><hr>
	<br><br><br><br><br><br><br><br>
	<form class="form-horizontal" method="POST">
		<div class="form-group" style="text-align:center">
			<label for="user_name">ID</label><br>
			<input type="text" name="user_name"  class="form-control" id="inputID" placeholder="Input your ID"
				required autocomplete="off" readonly onfocus="this.removeAttribute('readonly');" /><br>
		</div>
		<br>
		<div class="form-group" style="text-align:center">
			<label for="user_password">Password</label><br>
			<input type="password" name="user_password" class="form-control" id="inputPassword" placeholder="Input your password"
				required  autocomplete="off" readonly onfocus="this.removeAttribute('readonly');" /><br>
		</div>
		<br>
		<div class="checkbox" style="text-align:center">
			<label><input type="checkbox">remember your ID?</label>
		</div>
		</br>
		<div class="form-group" style="text-align:center">
			<button type="submit" name="login" class="btn btn-success">Login</button>
			<a class="btn btn-success" href="register.php" style="margin-left: 50px">
			<span class="glyphicon glyphicon-user"></span>&nbsp;Register</a>
		</div>
		</br>
	</form>
</div>
</body>
</html>

<?php
	echo "<script>alert('wow')</script>";
	if ( ($_SERVER['REQUEST_METHOD'] == 'POST') and isset($_POST['login']) )
	{
		$username=$_POST['user_name'];
		$userpassowrd=$_POST['user_password'];
		echo "<script>alert('wow1')</script>";
		if(empty($username))
		{
			$errMSG = "아이디를 입력하세요.";
		}
		else if(empty($userpassowrd))
		{
			$errMSG = "패스워드를 입력하세요.";
		}
		else
		{
			echo "<script>alert(11111)</script>";
			$user_check = "SELECT id FROM member WHERE id = '{$id}' ";
			$res = @mysqli_fetch_array(mysqli_query($db,$user_check));
			if($res['id'] && $res['password'] == $userpassowrd)
			{
				echo "<script>alert('wow')</script>";
				$_SESSION['username'] = "{$username}";
				$_SESSION['logined'] = "True";
				$_SESSION['enc'] = hash('sha256', '{$username}');
			}
			else
			{
				header("Location: /");
			}
		}
	}

	if(isset($errMSG))
		echo "<script>alert('$errMSG')</script>";
	echo "<script>alert('end')</script>";
?>
