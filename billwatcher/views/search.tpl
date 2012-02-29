<!DOCTYPE html>
<html>
<head>
    <title>Malaysian Bill Watcher</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    %include css
</head>
<body>
<div id='header'>
</div>
<body>
    %include header links=[]
    <div class="container-fluid">
        <div class="sidebar">
            <div class="well">
                <p>This project is created to create an awareness of law enacted, by your MP's</p>
            </div>
        </div>
        <div class="content">
            %for i in bill:
                %if i:
                    <div class="bill_item">
                    <h5><a href="/detail/{{i.id}}/">{{i.long_name}}</a></h5>
                    Revision: {{i.year}}
                    <br>Status  : {{i.status}}</br>
                    </div>
                    <div class="separator"></div>
                %end
            %end
        </div>
    </div>

</body>
</html>
