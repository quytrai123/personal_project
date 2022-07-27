<!DOCTYPE html>
<html lang="en">
<head>
    <title>Webpage Design</title>
    <link rel="stylesheet" href="stylethk.css">
    <link rel="stylesheet" href="signup.css">
</head>
<body>
    <div id="backand">
        <div id="background">
            <div id="praroz">PraRoz</div>
        </div>
        <div id="menu">
            <a href="#">HOME</a>
            <a href="#">ABOUT</a>
            <a href="#">SERVICE</a>
            <a href="#">DESIGN</a>
            <a href="#">CONTACT</a>
        </div>
        <div id="search">
            <input type="text" placeholder="Type To text" id="srch">
            <a href="#"><button id="btnsrch" onclick="init()">Search</button></a>
        </div>
        <div id="content">
            <h1>Web Desgin &</h1>
            <h1 id="de">Development</h1>
            <h1>Course</h1>
            <p id="noidung">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus culpa<br>
                voluptatem vero laborum provident, sequi mollitia molestiae soluta totam aut voluptatum quod, laudantium<br>
                cum, iure alias pariatur quasi possimus.
            </p>
            <a href="#" id="joinus">JOIN US</a>
            <div id="dangnhap">
                <h2>Login Here</h2>
                <form action="newkk.php" method="POST">
                    <input type="email" placeholder="Enter Email Here" name="email" value="" required="required">
                    <input type="password" placeholder="Enter Password Here" id="pass" name="password" value="" required="required">
                    <button id="login">Login</button>
                </form>
                <p id="don">Don't have an account</p>
                <a onclick="signup()" id="signhere" href="#">Sign up</a>
                <p id="log">Log in with</p>
                <div id="icon">
                    <a href="https://www.facebook.com"><ion-icon name="logo-facebook""></ion-icon></a>
                    <a href="https://www.instagram.com"><ion-icon name="logo-instagram"></ion-icon></a>
                    <a href="https://twitter.com"><ion-icon name="logo-twitter"></ion-icon></a>
                    <a href="https://www.google.com.vn/?hl=vi"><ion-icon name="logo-google"></ion-icon></a>
                    <a href="https://www.skype.com/en/"><ion-icon name="logo-skype"></ion-icon></a>
                </div>
            </div>
        </div>
        <script src="https://unpkg.com/ionicons@5.4.0/dist/ionicons.js"></script>
    </div>
    <div id="wow"></div>
    <div id="signup2"></div>
    <script src="signup.js"></script>
</body>
</html>