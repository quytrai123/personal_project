<!DOCTYPE html>
<html lang="en">
<head>
    <title>Successful Login</title>
</head>
<body>
    <h1>Successful Login</h1>
    <?php 
        $host = "localhost:4306";
        $user = "mainlogin";
        $pwd = "123";
        $sql_db = "login";
        $conn = @mysqli_connect($host,$user,$pwd, $sql_db);
        $sql_table = "testlogin";
        if (isset($_POST["email"]) && isset($_POST["password"])) {
            $email = trim(htmlspecialchars($_POST["email"]));
            $passwo = trim(htmlspecialchars($_POST["password"]));
        }
        $query = "INSERT INTO $sql_table(email,passw) VALUES ('$email','$passwo');";
        $result = mysqli_query($conn, $query);
    ?>
</body>
</html>