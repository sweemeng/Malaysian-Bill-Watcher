<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Organization">

<head>
    <!-- Add the following three tags inside head -->
    <meta itemprop="name" content="{{bill.long_name}}">
    <meta itemprop="description" content="{{bill.long_name}}">
    <title>{{bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' type="text/javascript"></script>
    <script src="http://twitter.github.com/bootstrap/1.4.0/bootstrap-modal.js" type="text/javascript"></script>
    <script src="http://twitter.github.com/bootstrap/1.4.0/bootstrap-scrollspy.js" type="text/javascript"></script>
    <script src="https://raw.github.com/pipwerks/PDFObject/master/pdfobject.min.js" type="text/javascript"></script>
    <style type="text/css">
        html,body{
            padding-top: 25px;
            height:100%;
        }
        #pdfview{
            position:relative;
            height:500px;
            width:750px;
        }
		
    	
    </style>
    <script type="text/javascript">
        $(function(){
            $("#raise_issue").modal({
                keyboard:true,
                backdrop:true
            });
            $(".topbar").scrollSpy();
            var pdfview = new PDFObject({url:"{{bill.url}}"}).embed("pdfview");
        });
    </script>
    %include google_plus_js
</head>
<body>
   %include facebook_js
    <div id="raise_issue" class="modal hide fade">
        <div class="modal-header">
            <a href="#" class="close">x</a>
            <h3>Raise Issue to your MP</h3>
        </div>
        <div class="modal-body">
            <p>The form will goes here</p>
        </div>
        <div class="modal-footer">
            <a href="#" class="btn danger">Send</a>
        </div>
    </div>

    %include header links=[("bills_link","#bills","Current Bill"),("comment_link","#comment","Comment On This Bill")]
    
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
                %include twitter_js
                %include facebook_div
                %include google_plus
                </p>
           </div>
        </div>
        <div class="content">
                 <div class="container">
                     <section id="bills">
                     <div class="page-header">
                         <h1>
                             {{bill.long_name}}
                         </h1>
                     </div>
                     <div class="row">
                        <div class="span12 columns">
                          <!--<iframe src="{{bill.url}}"></iframe>-->
                          <p>
                          <div id="pdfview"> 
                              <!--<object data="{{bill.url}}" type="application/pdf" width="100%" height="100%">
                                  <embed width="100%" height="100%" type="application/pdf" src="{{bill.url}}">
                                  Problem viewing pdf, you can download the pdf <a href="{{bill.url}}">here</a>
                                  </embed>
                              </object>-->
                          </div>
                          </p>
                        </div>
                     </div>
                     </section>
                     <section id="comment">
                     <div class="page-header">
                         <h1>
                             "Comments"
                         </h1>
                     </div>
                     <div class="row">
                         <div class="span12 columns">
                             <div id="commentview">
                                 <!--%include disqus-->
                             </div>
                         </div>
                     </div>
                     </section>
                 </div>
        </div>
    </div>
</body>
</html>
