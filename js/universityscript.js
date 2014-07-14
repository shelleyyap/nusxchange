$(document).ready(function() {
	$("#univform").validate({
        rules: {
        	name: {
        		required: true
        	},
        	short_name: {
        		required: true,
                remote: {
                    url: "/check_name",//?short_name=" + $("#short_name").val(),
                    async: "false",
                    type: "post",
                    data: {
                        short_name: function() {
                            return $("#short_name").val();
                        }
                    }
                }
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
            },
            faculty: {
                required: true
            }
        },
        messages: {
            modules: {
                url: "Please enter a valid URL. e.g. http://www.google.com"
            },
            img: {
                accept: "Please upload an image."
            },
            short_name: {
                remote: "This name is taken. Please choose another."
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
        },
        errorPlacement: function(error, element) {
        	if (element.attr("name")=="faculty") {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }/*,
        errorElement: "li"*//*
        errorLabelContainer: $("#errorContainer"),
        wrapper:"li"*/
        /*highlight: function(element, errorClass) {
        	$(element).addClass(errorClass);
        	});
        }*/

    });
});
