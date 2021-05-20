<?php

    $to = "faicel.ghozzi@esprit.tn"; //Resived mail here
    $from = $_REQUEST['email'];
    $name = $_REQUEST['name'];
    $phone = $_REQUEST['phone'];
    $headers = "From: $from";
    $subject = "You have a message from Financini";

    $fields = array();
    $fields{"name"} = "Name";
    $fields{"email"} = "Email";
    $fields{"phone"} = "Phone";
    $fields{"message"} = "Message";

    $body = "Here is what was sent:\n\n"; foreach($fields as $a => $b){   $body .= sprintf("%20s: %s\n",$b,$_REQUEST[$a]); }

      $send = mail($to, $subject, $body, $headers);
if(empty($from)){
     echo "<script type='text/javascript'>alert('Thank you for contacting us!')</script>";
     header("Location: 127.0.0.1:8000"); 
}
?>
