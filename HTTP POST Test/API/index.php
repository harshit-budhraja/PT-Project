<?php
    include "db.php";
    if(isset($_POST['Name']))
    {
        $name=$_POST['Name'];
        $sql="insert into data(Name) values('".$name."')";
        $result=mysqli_query($con,$sql);
        if($result)
        {
            $sql2="select * from data where Name='".$name."'";
            $result2=mysqli_query($con,$sql2);
            if($result2)
            {
                $records=mysqli_num_rows($result2);
                if($records > 0)
                {
                    success();
                }
                else
                {
                    failure();
                }
            }
        }
    }
    else if(isset($_GET['action']))
    {
        if($_GET['action']=="list")
        {
            $page = "https://apps.arachnis.org/pt-project/?action=list";
            $sec = "5";
            echo "
            <html>
            <head>
            <!--<meta http-equiv=\"refresh\" content=\"".$sec.";URL='".$page."'\">-->
            <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js\"></script>
            </head>
            <title>List of all requests</title>
            <body>
            <script>
                $(document).ready(function(){
                  refreshOutput();
                });
            
                function refreshOutput(){
                    $('#output').load('loadData.php', function(){
                       setTimeout(refreshOutput, 5000);
                    });
                }
            </script>
            <h1>[TESTING] Server POST logs</h1><br>
            <div id=\"output\"></div>";
            echo "
            </body>
            </html>";
        }
    }
    
    function success()
    {
        echo json_encode(['response'=>'success']);
    }
    
    function failure()
    {
        echo json_encode(['response'=>'failure']);
    }
    mysqli_close($con);
?>