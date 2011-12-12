<!DOCTYPE html>
<html>
<head>
    <title>{{bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <style type="text/css">
        body{
            padding-top: 60px;
        }
    </style>
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
                <p>Revision: {{revision[0].year}}</p>
                <p>Status: {{revision[0].status}}</p>
                <p>
                %include twitter_js
                %include facebook_div
                </p>
            </div>
        </div>
        <div class="content">
            <iframe width="100%" height="100%" src="{{revision[0].url}}"></iframe>
        </div>
    </div>
</body>
</html>
