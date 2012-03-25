    <div class="navbar" data-scrollspy="scrollspy">
        <div class="navbar-inner">
            <div class="container-fluid">
                <a class="brand" href="/">Malaysian Bill Watcher</a>
                <ul class="nav">
                    %if links:
                        %for i in links:
                            <li><a href="{{i[1]}}" id="{{i[0]}}">{{i[2]}}</a>
                        %end
                    %end
                    <li><a href="/about/">About Us</a>
                </ul>
                        %include search_box query=query
                </div>
        </div>
    </div>
