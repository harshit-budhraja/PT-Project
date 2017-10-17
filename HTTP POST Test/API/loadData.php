<?php
    include "db.php";
    $sql="select * from data ORDER BY timestamp DESC";
    $result=mysqli_query($con,$sql);
    if($result)
    {
        while($row=mysqli_fetch_array($result))
        {
            $temp = $row['timestamp']." - ".$row['Name']."<br>";
            echo "<p>".$temp."</p>";
        }
    }
    mysqli_close($con);
?>
