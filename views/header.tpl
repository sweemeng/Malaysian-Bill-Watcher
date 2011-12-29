    <div class="topbar">
        <div class="topbar-inner">
            <div class="container-fluid">
                <a class="brand" href="#">Malaysian Bill Watcher</a>
                <ul class="nav">
                    <li><a href="/">Home</a>
                    %if links:
                        %for i in links:
                            <li><a href="{{i[1]}}" id="{{i[0]}}">{{i[2]}}</a>
                        %end
                    %end
                    <li><a href="#">About Us</a>
                </ul>
                        %include search_box
                </div>
        </div>
    </div>
