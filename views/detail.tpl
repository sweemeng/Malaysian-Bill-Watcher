<!DOCTYPE html>
<html>
<head>
    <title>{{bill.long_name}}</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' type="text/javascript"></script>
    <script src="http://twitter.github.com/bootstrap/1.4.0/bootstrap-modal.js" type="text/javascript"></script>
    <style type="text/css">
        html,body{
            padding-top: 25px;
            height:100%
        }
		
    	
    </style>
    <script type="text/javascript">
        $(function(){
            $("#raise_issue").modal({
                keyboard:true,
                backdrop:true
            });
            $(".btn").click(function(event){
                $("#raise_issue").modal('show');
            });
            $("#bills").click(function(event){
                event.preventDefault();
                $("#commentview").hide();
                $("#pdfview").show();
                $("#bills").parent().attr("class","active");
                $("#comment").parent().removeClass("active");
            });
            $("#comment").click(function(event){
                event.preventDefault();
                $("#pdfview").hide();
                $("#commentview").show();
                $("#comment").parent().attr("class","active");
                $("#bills").parent().removeClass("active");
            });
            $("#bills").parent().attr("class","active");
        });
    </script>
</head>
<body>
    <!--%include facebook_js-->
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

    %include header links=[("bills","#bills","Current Bill"),("comment","#comment","Comment On This Bill")]
    
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
                <a class="btn" data-control-modal="raise_issue">Raise Issue</a>
                </p>
            </div>
        </div>
        <div class="content">
                 <div class="container">
                     <div class="row">
                        <div class="span12">
                          <!--<iframe src="{{bill.url}}"></iframe>-->
                          <div id="pdfview">
                              <object data="{{bill.url}}" type="application/pdf" width="100%" height="100%">
                                  Problem viewing pdf, you can download the pdf <a href="{{bill.url}}">here</a>
                              </object>
                          </div>
                          <div id="commentview" class="hide">this is where comment goes</div>
                        </div>
                     </div>
                 </div>
        </div>
    </div>
</body>
</html>
