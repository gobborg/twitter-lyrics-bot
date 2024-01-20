<?php

$usableLyrics = file("sorted-lyrics.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$usedLyrics = file("used-lyrics.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

$lastModified = filemtime("used-lyrics.txt");
$currentTime = time();
if ($currentTime - $lastModified > 86400) {

do{
	$randomIndex = array_rand($usableLyrics);
	$lineOfTheDay = $usableLyrics[$randomIndex];
} while(in_array($lineOfTheDay, $usedLyrics)); 

# append a new line to the output file
$used_append = file_put_contents("used-lyrics.txt", $lineOfTheDay."\n", FILE_APPEND);
} else {
	$lineOfTheDay = end($usedLyrics);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p style="text-align:center;"><?php echo $lineOfTheDay; ?></p>
</body>
</html>

