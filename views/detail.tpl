<!DOCTYPE html>
<html>
<head>
    <title>{{bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' type="text/javascript"></script>
    <style type="text/css">
        body{
            padding-top: 60px;
            height:100%
        }
    </style>
    <script type="text/javascript">
        $(function(){
        });

    </script>
</head>
<body>
    %include facebook_js
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
                <h5>Detail</h5>
                <p>Code: {{bill.name}}</p>
                <p>Name: {{bill.long_name}}</p>
                <p>Revision: {{bill.year}}</p>
                <p>Status: {{bill.status}}</p>
                <p>
                %include twitter_js
                %include facebook_div
                </p>
            </div>
        </div>
        <div class="content">
            <div class='row' width="100%" height="100%">
                <iframe id='pdf' width="100%" height="100%" src="{{bill.url}}"></iframe>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
