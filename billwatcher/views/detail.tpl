<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Organization">
<head>
    <!-- Add the following three tags inside head -->
    <meta itemprop="name" content="{{rev.bill.long_name}}">
    <meta itemprop="description" content="{{rev.bill.long_name}}">
    <title>{{rev.bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="/css/bootstrap.css">
    <link rel="stylesheet" href="/css/bootstrap-responsive.css">
    <script src='/js/jquery.js' type="text/javascript"></script>
    <script src="/js/bootstrap-modal.js" type="text/javascript"></script>
    <script src="/js/bootstrap-scrollspy.js" type="text/javascript"></script>
    <script src="https://raw.github.com/pipwerks/PDFObject/master/pdfobject.min.js" type="text/javascript"></script>
    <style type="text/css">
        #pdfview{
            position:relative;
            height:500px;
            width:750px;
        }
		
    	
    </style>
    <script type="text/javascript">
        $(function(){
            $(".navbar").scrollspy();
            var pdfview = new PDFObject({url:"{{rev.url}}"}).embed("pdfview");
        });
    </script>
    %include google_plus_js
    %include google_analytics
</head>
<body>
   %include facebook_js

    %include header links=[("bills_link","#bills","Current Bill"),("comment_link","#comment","Comment On This Bill")],query=""
    
    <div class="container-fluid">
        <div class="sidebar span3">
            <div class="well">
                <h5>Detail</h5>
                <p>
                <dl>
                <dt>Code:</dt><dd> {{rev.bill.name}}</dd>
                <dt>Name:</dt><dd> {{rev.bill.long_name}}</dd>
                <dt>Revision:</dt><dd> {{rev.year}}</dd>
                <dt>Status:</dt><dd> {{rev.status}}</dd>
                </dl>
                </p>
                <p>
                <dl>
                    <dt>Previous revision:</dt>
                    %for r in rev.bill.bill_revs:
                        <dd><a href='/detail/{{r.id}}/'>{{r.year}}</a></dd>
                    %end
                </dl>
                %include twitter_js
                %include facebook_div
                %include google_plus
                </p>
           </div>
        </div>
        <div class="content span9">
                 <div>
                     <section id="bills">
                     <div class="page-header">
                         <h1>
                             {{rev.bill.long_name}}
                         </h1>
                     </div>
                     <div class="row">
                        <div class="span9 columns">
                          <!--<iframe src="{{rev.url}}"></iframe>-->
                          <p>
                          <div id="pdfview"> 
                              <a href="{{rev.url}}">Can't view? Download it!!!</a>
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
                         <div class="span9 columns">
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
