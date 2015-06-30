<?php
$msg = $_GET['msg'];

echo '<p>DECMOCRATIC DJ </p></p>';

if ( $msg == '1' ) {
	echo '<p>Your information was submitted successfully.</p>';
}
else {
	echo '<p>Let your voice be heard!</p>';
}
?>

<form action="formprocessor.php" method="post" />
<input type="submit" value="Submit" />
</form>
