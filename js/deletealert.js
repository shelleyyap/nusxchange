$(document).ready(function(){
	$("#del").click(function(){
		if (!confirm("Content to be deleted. Continue"?)){
			return false;
		}
	});
})
