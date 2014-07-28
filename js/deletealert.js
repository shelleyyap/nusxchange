$(document).ready(function(){
	$('#dialog-confirm').hide();
	function openDialog(){
		$('#dialog-confirm').dialog({
			resizable: false,
			modal: true,
			title: "Delete Confirmation",
			height: 250,
			width: 400,
			buttons: {
				"Yes": function () {
						$(this).dialog('close');
						var url = $('.url').attr('value')
						$(location).attr('href', url);
				         },
				"No": function () {
						$(this).dialog('close');
					}
			}
		});
	}
	$("#dialog-confirm").html("Content to be deleted. Continue?");
	$("#del").click(openDialog);
})
