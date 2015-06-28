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
<p><input type="radio" name="song" value="1"/>Title 1</p>
<p><input type="radio" name="song" value="2"/>Title 2</p>
<p><input type="radio" name="song" value="3"/>Title 3</p>
<p><input type="radio" name="song" value="4"/>Title 4</p>
<p><input type="radio" name="song" value="5"/>Title 5</p>
<input type="submit" value="Submit" />
</form>
