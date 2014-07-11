$(document).ready(function() {
	$("#univform").validate({
        rules: {
        	name: {
        		required: true
        	},
        	short_name: {
        		required: true
        	},
        	country: {
        		required: true
        	},
        	state: {
        		required: true
        	},
        	calendar: {
        		required: true
        	},
            modules: {
                required: true,
                url: true
            },
            img: {
            	required: true,
            	accept: "image/*"
            },
            abtschool: {
            	required: true
            }
        },
        messages: {
        	name: {
        		required: "Please enter name of university."
        	},
        	short_name: {
        		required: "Please enter short name of university. This must be unique."
        	},
        	country: {
        		required: "Please enter country of university."
        	},
        	state: {
        		required: "Please enter state."
        	},
        	calendar: {
        		required: "Please enter academic calendar."
        	},
        	modules: {
        		required: "Please enter url of university page of offered modules.",
        		url: "Please enter valid URL for modules offered."
        	},
        	img: {
        		required: "Please upload image of university."
        	},
        	abtschool: {
        		required: "Please enter an introduction to the school."
        	}
        },
        errorPlacement: function(error, element) {
        	error.appendTo($("#errorContainer"));
        },
        errorElement: "li"/*
        errorLabelContainer: $("#errorContainer"),
        wrapper:"li"*/
        /*ighlight: function(element, errorClass) {
        	$(element).fadeOut(function() {
        		$(element).fadeIn();
        	});
        }*/
    });
});
