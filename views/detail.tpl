<!DOCTYPE html>
<html>
<head>
    <title>{{bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' type="text/javascript"></script>
    <script src='/js/pdf.js' type='text/javascript'></script>
    <style type="text/css">
        body{
            padding-top: 60px;
            height:100%
        }
		
        iframe{
	    margin:0;
	    padding:0;
	    height:100%;
	    width:100%;
	    border:none;
	}
	[ hidden ]{
	    display:none;
	}
        .textLayer{
            position:absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
	    color: #000;
            border:1px solid black;
        }
	.textLayer > div {
            color: transparent;
            position: absolute;
            line-height:1.5;
            
            font-size: 16px
        }
        .canvas_container{
            position:absolute;
            margin: auto;
	    display: block;
            height:100%;
        }
        #pdf_viewer{
            position:relative;
            display:block;
        }
        

		
    </style>

</head>
<body>
    <!--%include facebook_js-->
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
                <p>Previous revision:</p>
                %for i in revision[1:]:
                    <p><a href='/detail/{{i.id}}/'>i.year</a></p>
                %end
                <!--%include twitter_js-->
                <!--%include facebook_div-->
                </p>
            </div>
        </div>
        <div class="content">
                 <div class="container">
                     <div class="row" height="100%" width="100%">
                        <div class="span12">
                          <iframe src="{{bill.url}}"></iframe>
                        </div>
                     </div>
                 </div>
        </div>
    </div>
</body>
</html>
