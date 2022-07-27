<!DOCTYPE html>
<html lang="en">
<head>
    <title>Successful Sign Up</title>
</head>
<body>
    <h1>Successful Sign Up</h1>
    <?php 
        $host = "localhost:4306";
        $user = "mainlogin";
        $pwd = "123";
        $sql_db = "signup";
        $conn = @mysqli_connect($host,$user,$pwd, $sql_db);
        $sql_table = "sign_up";
        if (isset($_POST["email"]) && isset($_POST["password"]) && isset($_POST["name"])) {
            $email = trim(htmlspecialchars($_POST["email"]));
            $name = trim(htmlspecialchars($_POST["name"]));
            $passwo = trim(htmlspecialchars($_POST["password"]));
        }
        $query = "INSERT INTO $sql_table(email,passw,name) VALUES ('$email','$passwo','$name');";
        $result = mysqli_query($conn, $query);
    ?>
</body>
</html>