$(document).ready(function() {
    CKEDITOR.replace('abtschool');
    
    $('#select_all').click(function(event) {
        if(this.checked) {
      // Iterate each checkbox
            $(':checkbox').each(function() {
                this.checked = true;
            });
        } else {
            $(':checkbox').each(function() {
                this.checked = false;
            });
        }
    });
    
    jQuery.validator.addMethod("lettersandspace", function(value, element) {
        return this.optional(element) || /^[a-z," "]+$/i.test(value);
    }, "Letters and spaces only please"); 
    
    jQuery.validator.addMethod("lettersonly", function(value, element) {
        return this.optional(element) || /^[a-z]+$/i.test(value);
    }, "Letters only please. No spaces, symbols and digits allowed.");

    jQuery.validator.addMethod("lettersnumspace", function(value, element) {
        return this.optional(element) || /^[a-z0-9\:\;," "]+$/i.test(value);
    }, "Letters, numbers, colons, semicolons and spaces only please.");

	$("#univform").validate({
        rules: {
        	name: {
        		required: true,
                lettersandspace: true
        	},
        	country: {
        		required: true
        	},
        	state: {
        		required: true,
                lettersandspace: true
        	},
        	calendar: {
        		required: true,
                lettersnumspace: true
        	},
            exchange_type: {
                lettersnumspace: true
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
