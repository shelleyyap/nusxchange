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
            modules: {
                url: "Please enter a valid URL. e.g. http://www.google.com"
            },
            img: {
                accept: "Please upload an image."
            }

        },
        /*invalidHandler: function(event, validator) {
            var errors = validator.numberOfInvalids();
            if (errors) {
                $("div#errorContainer").html("Please complete all fields");
                $("div#errorContainer").show();
            } else {
                $("div#errorContainer").hide();
            }
        },*/
        
        /*showErrors: function(errorMap, errorList) {
            $("#errorContainer").html("All fields must be completed before you submit the form");
        },*/
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        }, 
        unhighlight: function(element, errorClass, validClass) {
            $(element).closest('.form-group').removeClass('has-error');
        }
        /*errorPlacement: function(error, element) {
        	error.appendTo($("#errorContainer"));
        },
        errorElement: "li"*//*
        errorLabelContainer: $("#errorContainer"),
        wrapper:"li"*/
        /*highlight: function(element, errorClass) {
        	$(element).addClass(errorClass);
        	});
        }*/

    });
});
