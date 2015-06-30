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
<p><input type="radio" name="song" value="Out of the Woods"/>Out of the Woods</p>
<p><input type="radio" name="song" value="Blank Space"/>Blank Space</p>
<p><input type="radio" name="song" value="Shake It Off"/>Shake It Off</p>
<input type="submit" value="Submit" />
</form>
