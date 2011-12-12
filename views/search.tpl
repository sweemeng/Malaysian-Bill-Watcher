<!DOCTYPE html>
<html>
<head>
    <title>Malaysian Bill Watcher</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <style type="text/css">
        body{
            padding-top: 60px;
        }
    </style>
</head>
<body>
<div id='header'>
</div>
<body>
    <div class="topbar">
        <div class="topbar-inner">
            <div class="container-fluid">
                <a class="brand" href="#">Malaysian Bill Watcher</a>
                <p class="pull-right">
                    %include search_box
                </p>
            </div>
        </div>
    </div>
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
                    <h5><a href="/detail/{{i['bill_id']}}/">{{i['long_name']}}</a></h5>
                    Revision: {{i['year']}}
                    <br>Status  : {{i['status']}}</br>
                    </div>
                %end
            %end
        </div>
    </div>

</body>
</html>
