<form method='GET' action='/search/' class="navbar-search pull-right">

%if defined('query'):
<input type="text" name="query" placeholder="Search" class="navbar-query" value="{{query}}"></input>
%else:
<input type="text" name="query" placeholder="Search" class="navbar-query"></input>
%end
</form>
