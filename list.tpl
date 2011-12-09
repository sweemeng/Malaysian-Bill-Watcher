<html>
<head>
    <title>Malaysian Bill Watcher</title>
    <link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
    <link rel="stylesheet" type="text/css" media="all" href="/css/bills.css" />
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
            <p>This project is created to create an awareness of law enacted, by your MP's</p>
        </div>
        <div class="grid_9">
            %for i in bill:
                <div class="bill_item">
                <p><a href="/detail/{{i.id}}/">{{i.long_name}}</a></p>
                </div>
            %end
        </div>
    </div>
</body>
</body>
</html>