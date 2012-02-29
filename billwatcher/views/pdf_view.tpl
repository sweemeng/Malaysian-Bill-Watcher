$('#next').click(function(){
    next_page = cur_page + 1;
	cur_page = next_page;
    $("#page_div").load('/html/',{'filename':{{filename}},'page':next_page});
});