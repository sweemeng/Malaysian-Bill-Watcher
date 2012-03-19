<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Organization">

<head>
    <!-- Add the following three tags inside head -->
    <meta itemprop="name" content="Malaysian Bill Watcher">
    <meta itemprop="description" content="This is where we can see bills being debated in Malaysian Parliament">
    <title>Malaysian Bill Watcher</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
    <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
    %include css
    %include google_analytics
</head>
<body>
<div id='header'>
</div>
<body>
    %include facebook_js
    %include header links=[]
    <div class="container-fluid">
        <div class="sidebar">
            <div class="well">
                <p>This project is created to create an awareness of law enacted, by your MP's</p>
            </div>
        </div>
        <div class="content">
        <div class="container">
           <div class="row">
               <div class="span12">
               %for bill in bills:
                   <div class="bill_item">
                       <h5><a href="/detail/{{bill.id}}/">{{bill.bill.long_name}}</a></h5>
                        Revision: {{bill.year}}
                        <br>Status  : {{bill.status}}</br>
                   </div>
                   <div class="separator"></div>
               %end
               <div class='pagination' id='pages'>
                  <ul>
                      %if pages.page_no != pages.page_list[0]:
                          <li class="prev"><a href="/?page_no={{pages.page_list[0]}}">First</a></li>
                          <li class="prev"><a href='/?page_no={{pages.prev_page}}'>prev</a></li>
                      %else:
                          <li class="prev disabled"><a href="/?page_no={{pages.page_list[0]}}">First</a></li>
                          <li class="prev disabled"><a href="#">prev</a></li>
                      %end
                      %for i in pages.active_list:
                          %if i == pages.page_no:
                              <li class="active"><a href="#">{{i}}</a></li>
                          %else:
                              <li><a href='/?page_no={{i}}'>{{i}}</a></li>
                          %end
                      %end
                      %if pages.page_no != pages.page_list[-1]:
                          <li class="next"><a href='/?page_no={{pages.next_page}}'>next</a></li>
                          <li class="next"><a href="/?page_no={{pages.page_list[-1]}}">Last</a></li>
                      %else:
                          <li class="next disabled"><a href="#">next</a></li>
                          <li class="next disabled"><a href="/?page_no={{pages.page_list[-1]}}">Last</a></li>
                      %end
                  </ul>
               </div>
               </div>
           </div>
        </div>
    </div>
        
</body>
</body>
</html>
