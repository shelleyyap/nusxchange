$(document).ready(function() {
	$('#asia').click(function(event) {
        if(this.checked) {
      		$('#China').prop('checked', true);
      		$('#HongKong').prop('checked', true);
      		$('#Japan').prop('checked', true);
      		$('#Singapore').prop('checked', true);
      		$('#SouthKorea').prop('checked', true);
      		$('#Taiwan').prop('checked', true);
        } else {
            $('#China').prop('checked', false);
            $('#HongKong').prop('checked', false);
            $('#Japan').prop('checked', false);
            $('#Singapore').prop('checked', false);
            $('#SouthKorea').prop('checked', false);
            $('#Taiwan').prop('checked', false);
        }
    });
    $('#americas').click(function(event) {
    	if (this.checked) {
    		$('#Canada').prop('checked', true);
    		$('#Mexico').prop('checked', true);
    		$('#USA').prop('checked', true);
    	} else {
            $('#Canada').prop('checked', false);
            $('#Mexico').prop('checked', false);
            $('#USA').prop('checked', false);
    	}
    });
    $('#europe').click(function(event) {
    	if (this.checked) {
    		$('#Austria').prop('checked', true);
    		$('#Belgium').prop('checked', true);
    		$('#Croatia').prop('checked', true);
    		$('#Denmark').prop('checked', true);
    		$('#Estonia').prop('checked', true);
    		$('#Finland').prop('checked', true);
    		$('#France').prop('checked', true);
    		$('#Germany').prop('checked', true);
    		$('#Hungary').prop('checked', true);
    		$('#Ireland').prop('checked', true);
    		$('#Lithuania').prop('checked', true);
    		$('#Latvia').prop('checked', true);
    		$('#Netherlands').prop('checked', true);
    		$('#Norway').prop('checked', true);
    		$('#Poland').prop('checked', true);
            $('#Romania').prop('checked', true);
    		$('#Spain').prop('checked', true);
    		$('#Sweden').prop('checked', true);
    		$('#Switzerland').prop('checked', true);
    		$('#Turkey').prop('checked', true);
    		$('#UK').prop('checked', true);
    	} else {
            $('#Austria').prop('checked', false);
            $('#Belgium').prop('checked', false);
            $('#Croatia').prop('checked', false);
            $('#Denmark').prop('checked', false);
            $('#Estonia').prop('checked', false);
            $('#Finland').prop('checked', false);
            $('#France').prop('checked', false);
            $('#Germany').prop('checked', false);
            $('#Hungary').prop('checked', false);
            $('#Ireland').prop('checked', false);
            $('#Lithuania').prop('checked', false);
            $('#Latvia').prop('checked', false);
            $('#Netherlands').prop('checked', false);
            $('#Norway').prop('checked', false);
            $('#Poland').prop('checked', false);
            $('#Romania').prop('checked', false);
            $('#Spain').prop('checked', false);
            $('#Sweden').prop('checked', false);
            $('#Switzerland').prop('checked', false);
            $('#Turkey').prop('checked', false);
            $('#UK').prop('checked', false);
        }
    });
})

 
