<?php

// If the Token Parameter is Not Set, Set it to Blank
if(isset($_REQUEST['Token'])){$Token = $_REQUEST['Token'];}else{$Token = "";}

// If the Token is Not Yours, an Attacker or Web Crawler Can't Trigger Your Door Remotely
if($Token == "YOUR-GUID-HERE"){

// Execute the Python Script with Elevated Rights
exec("sudo python /var/www/html/GarageDoor.py");

// Output to the Web API
echo "Toggling Garage Door..";

}

?>