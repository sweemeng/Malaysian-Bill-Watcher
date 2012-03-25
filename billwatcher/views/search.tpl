<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Organization">

<head>
    <!-- Add the following three tags inside head -->
    <meta itemprop="name" content="Malaysian Bill Watcher">
    <meta itemprop="description" content="This is where we can see bills being debated in Malaysian Parliament">
    <title>Malaysian Bill Watcher</title>
    <link rel="alternate" type="application/rss+xml" title="RSS feed" href="/feeds/" />
    <link rel="stylesheet" href="/css/bootstrap.css">
    <link rel="stylesheet" href="/css/bootstrap-responsive.css">
    %include css
    %include google_analytics
</head>
<body>
<div id='header'>
</div>
<body>
    %include header links=[]
    <div class="container-fluid">
        <div class="sidebar span3">
            <div class="well">
                <p>This project is created to create an awareness of law enacted, by your MP's</p>
            </div>
        </div>
        <div class="content span9">
            %for i in bill:
                %if i:
                    <div class="bill_item">
                    <h5><a href="/detail/{{i.id}}/">{{i.bill.long_name}}</a></h5>
                    Revision: {{i.year}}
                    <br>Status  : {{i.status}}</br>
                    </div>
                    <div class="separator"></div>
                %end
            %end
            <div class='pagination' id='pages'>
               <ul>
                  %if pages.page_no != pages.page_list[0]:
                      <li class="prev"><a href="/search/?page_no={{pages.page_list[0]}}&query={{query}}">First</a></li>
                      <li class="prev"><a href='/search/?page_no={{pages.prev_page}}'>prev</a></li>
                  %else:
                      <li class="prev disabled"><a href="/search/?page_no={{pages.page_list[0]}}"&query={{query}}>First</a></li>
                      <li class="prev disabled"><a href="#">prev</a></li>
                  %end
                  %for i in pages.active_list:
                      %if i == pages.page_no:
                          <li class="active"><a href="#">{{i}}</a></li>
                      %else:
                          <li><a href='/search/?page_no={{i}}&query={{query}}'>{{i}}</a></li>
                      %end
                  %end
                  %if pages.page_no != pages.page_list[-1]:
                      <li class="next"><a href='/search/?page_no={{pages.next_page}}&query={{query}}'>next</a></li>
                      <li class="next"><a href="/search/?page_no={{pages.page_list[-1]}}&query={{query}}">Last</a></li>
                  %else:
                      <li class="next disabled"><a href="#">next</a></li>
                      <li class="next disabled"><a href="#">Last</a></li>
                  %end
               </ul>
            </div>

        </div>
    </div>

</body>
</html>
