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
                <p>This project is created to create an awareness of law enacted, by your MP's</p>
            </div>
        </div>
        <div class="content">
            %for i in bill:
                <div class="bill_item">
                <h5><a href="/detail/{{i.bill_id}}/">{{i.long_name}}</a></h5>
                Revision: {{i.year}}
                <br>Status  : {{i.status}}</br>
                </div>
            %end
            <div class='pagination' id='pages'>
                <ul>
            %if page_no != page_list[0]:
                    <li class="prev"><a href='/?page_no={{prev_page}}'>prev</a></li>
            %else:
                    <li class="prev disable"><a href="#">prev</a></li>
            %end
            %for i in page_list:
                %if i == page_no:
                    <li class="active"><a href="#">{{i}}</a></li>
                %else:
                    <li><a href='/?page_no={{i}}'>{{i}}</a></li>
                %end
            %end
            %if page_no != page_list[-1]:
                <li class="next"><a href='/?page_no={{next_page}}'>next</a></li>
            %else:
                <li class="next disable"><a href="#">next</a></li>
            %end
            </ul>
        </div>
    </div>
        
</body>
</body>
</html>
