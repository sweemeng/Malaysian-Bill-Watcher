<html>
<head>
    <title>Malaysian Bill Watcher</title>
    <link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
</head>
<body>
<div id='header'>
</div>
<body>
    <div class="container_12">
        <div class="grid_12 header">
            <h1>Malaysian Bill Watcher</h1>
        </div>
        <div class="clear"></div>
        <div class="grid_3">
            
        </div>
        <div class="grid_9">
            %for i in bill:
                <p><a href="/detail/{{i.id}}/">{{i.long_name}}</a></p>
            %end
        </div>
    </div>
</body>
</body>
</html>