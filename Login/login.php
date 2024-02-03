// This file handles the form submission and interacts with the database

<?php
$servername = "your_database_server";
$username = "your_database_username";
$password = "your_database_password";
$database = "login_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process login form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $enteredUsername = $_POST["Username"];
    $enteredPassword = $_POST["Password"];

    // Perform authentication
    $sql = "SELECT * FROM users WHERE username='$enteredUsername' AND password='$enteredPassword'";
    $result = $conn->query($sql);

    if ($result->num_rows == 1) {
        // Authentication successful, redirect to a welcome page or perform other actions
        echo "Login successful!";
    } else {
        // Authentication failed
        echo "Invalid username or password";
    }
}

// Close connection
$conn->close();
?>
