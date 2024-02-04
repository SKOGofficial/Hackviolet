<?php
// This file handles the form submission and interacts with the database
$servername = "localhost";
$username = "root";
$password = "root";
$database = "login_system";

// Create new connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process login form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $enteredUsername = $_POST["Username"];  //get data
    $enteredPassword = $_POST["Password"];  //get data

    // Perform authentication
    $sql = "SELECT * FROM users WHERE username='$enteredUsername' AND password='$enteredPassword'";     //query
    $result = $conn->query($sql);   //

    if ($result->num_rows == 1) {   // if username == username, pw == pw 
        // Authentication successful, redirect to a welcome page or perform other actions
        header("Location: http://localhost:8888"); 
    } else {
        // Authentication failed
        echo "Invalid username or password";
    }
} else {
    echo "fail";
}

// Close connection
$conn->close();
?>
