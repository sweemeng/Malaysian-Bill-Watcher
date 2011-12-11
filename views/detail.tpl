<html>
<head>
    <title>{{bill.long_name}}</title>
    <link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
</head>
<body>
<div id='header'>
</div>
<body>
    %include facebook_js
    <div class="container_12">
        <div class="grid_12 header">
            <h1>Malaysian Bill Watcher</h1>
        </div>
        <div class="clear"></div>
        <div class="grid_3">
            <p>Code: {{bill.name}}</p>
            <p>Name: {{bill.long_name}}</p>
            <p>Revision: {{revision[0].year}}</p>
            <p>Status: {{revision[0].status}}</p>
            <p>
            %include twitter_js
            %include facebook_div
            </p>
        </div>
        <div class="grid_9">
            <iframe width="100%" height="100%" src="{{revision[0].url}}"></iframe>
        </div>
    </div>
</body>
</body>
</html>
