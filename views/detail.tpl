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
    <script type="text/javascript">
        var page_no = 1;
        function viewer(page_no){
            PDFJS.getPdf('/pdf/{{bill.url.split("/")[-1]}}',function (data){
     	    var pdf = new PDFJS.PDFDoc(data);
	
	    var page = pdf.getPage(page_no);
            //console.log(page);
	    var scale = 1.5;
	
	    var canvas = document.getElementById("pdf_canvas");
	    var context = canvas.getContext('2d');
	    canvas.height = page.height * scale;
	    canvas.width = page.width * scale;
	//alert(pdf.numPages);
	    page.startRendering(context,null,$('.textLayer')[0]);
        });
        }
        $(function(){
             viewer(page_no);
             $('#next').click(function(){
                 page_no = page_no + 1;
                 viewer(page_no);
             });
             $('#prev').click(function(){
                 page_no = page_no - 1
                 viewer(page_no);
             });
             $('#pdf_viewer').load('/viewer/{{bill.url.split("/")[-1]}}/?page=1 div > div',function(){
                 //img_tag = $('#pdf_viewer > div > img')[0]
                 //old_img = img_tag.src.split('/');
                 //console.log(old_img[old_img.length-1]);
                 //img_name = old_img[old_img.length-1]
                 //img_tag.src = '/viewer/{{bill.url.split("/")[-1]}}/'+img_name
                 $('#pdf_viewer > div').css('position','relative');
             });
        });
        PDFJS.workerSrc = '/js/pdf.js';
    </script>
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
                          <iframe src="/viewer/{{bill.url.split('/')[-1]}}/?page=1"></iframe>
                        </div>
                     </div>
                 </div>
        </div>
    </div>
</body>
</html>
