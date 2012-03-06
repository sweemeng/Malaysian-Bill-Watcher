<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Organization">

<head>
    <!-- Add the following three tags inside head -->
    <meta itemprop="name" content="Malaysian Bill Watcher">
    <meta itemprop="description" content="This is where we can see bills being debated in Malaysian Parliament">

    <title>About Us</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
   
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' type="text/javascript"></script>
    <script src="http://twitter.github.com/bootstrap/1.4.0/bootstrap-modal.js" type="text/javascript"></script>
    <script src="http://twitter.github.com/bootstrap/1.4.0/bootstrap-scrollspy.js" type="text/javascript"></script>
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
            $(".topbar").scrollSpy();
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

    %include header links=[("who_link","#who","Who We Are"),("contact_link","#contacts","Contacts")]
    
    <div class="container-fluid">
        <div class="sidebar">
            <div class="well">
                <h5>The Team</h5>
                <p>programmer: sweemeng</p>
                <p>
                <!--%include twitter_js-->
                <!--%include facebook_div-->
                </p>
           </div>
        </div>
        <div class="content">
                 <div class="container">
                     <section id="who">
                     <div class="page-header">
                         <h1>
                             Who We Are
                         </h1>
                     </div>
                     <div class="row">
                        <div class="span12 columns">
                          <p>
                             We are a group of concerned Citizen that hope to see more transparency in govt. 
                          </p>
                        </div>
                     </div>
                     </section>
                     <section id="contacts">
                     <div class="page-header">
                         <h2>
                             Contacts
                         </h2>
                     </div>
                     <div class="row">
                         <div class="span12 columns">
                             <div id="contactview">
                                 <p>Email: sinarproject@gmail.com</p>
                                 <p>Twitter: @sinarproject</p>
                             </div>
                         </div>
                     </div>
                     </section>
                 </div>
        </div>
    </div>
</body>
</html>
