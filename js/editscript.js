/*$(document).ready(function(){
	if ($("#fac").val() != ("Faculty of Science" || "School of Computing")){

	}

});*/
$(document).ready(function(){
        /*$("#btn1").click(function(){
          $("select").append("<option value=0> Physics </option>");*/
         /* $("#maj").replaceWith("<select name="major" required>
                         <option value=0> Select Major </option><option value="Physics"> Physics </option>
                      </select>"); */
    CKEDITOR.replace('reviewcontents');
    $("select#fac").change(function() {
            /*if $("select#fac option:selected").text() == "Faculty of Science") {
              $("select#maj").append("<option value=0> Physics </option>");
            } else {
              $("select#maj").append("<option value=0> Computer science </option>");
            }*/
        if ($("select#fac option:selected").val() == "FoS") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Applied Mathematics'> Applied Mathematics </option>");
            $("select#maj").append("<option value='Chemistry'> Chemistry </option>");
            $("select#maj").append("<option value='Computational Biology'> Computational Biology </option>");
            $("select#maj").append("<option value='Food Science and Technology'> Food Science and Technology</option>");
            $("select#maj").append("<option value='Life Sciences'> Life Sciences </option>");
            $("select#maj").append("<option value='Mathematics'> Mathematics </option>");
            $("select#maj").append("<option value='Pharmacy'> Pharmacy </option>");
            $("select#maj").append("<option value='Physics'> Physics </option>");
            $("select#maj").append("<option value='Quantitative Finance'> Quantitative Finance</option>");
            $("select#maj").append("<option value='Statistics'> Statistics </option>");
        } else if ($("select#fac option:selected").val() == "SoC") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Business Analytics'> Business Analytics </option>");
            $("select#maj").append("<option value='Computational Biology'> Computational Biology</option>");
            $("select#maj").append("<option value='Computer Engineering'> Computer Engineering</option>");
            $("select#maj").append("<option value='Computer Science'> Computer Science </option>");
            $("select#maj").append("<option value='Electronic Commerce'> Electronic Commerce</option>");
            $("select#maj").append("<option value='Information Systems'> Information Systems </option>");
        } else {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
        }
            
    })

	$("select#specprog").change(function() {
		if ($("select#specprog option:selected").val() == "NIL") {
			$("select#fac2 option").remove();
			$("select#fac2").append("<option value='NIL'> NIL </option>");
			$("select#fac2").val("NIL");
			$("select#maj2 option").remove();
			$("select#maj2").append("<option value='NIL'> NIL </option>");
			$("select#maj2").val("NIL");
		} else if ($("select#specprog option:selected").val() == "USP") {
            $("select#fac2 option").remove();
            $("select#fac2").append("<option value='USP'> USP </option>");
            $("select#fac2").val("USP");
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value='USP'> USP </option>");
            $("select#maj2").val("USP");
        } else if ($("select#specprog option:selected").val() !== "") {
			$("select#maj2 option").remove();
			$("select#maj2").append("<option value=> Select Major/Minor </option>");
			$("select#fac2 option").remove();
			$("select#fac2").append("<option value=> Select Faculty </option>");
			$("select#fac2").append("<option value='FoS'> Faculty of Science </option>");
			$("select#fac2").append("<option value='SoC'> School of Computing </option>");
		} else {
			$("select#maj2 option").remove();
			$("select#maj2").append("<option value=> Select Major/Minor </option>");
			$("select#fac2 option").remove();
			$("select#fac2").append("<option value=> Select Faculty </option>");
		}
	})

	$("select#fac2").change(function() {
            /*if $("select#fac option:selected").text() == "Faculty of Science") {
              $("select#maj").append("<option value=0> Physics </option>");
            } else {
              $("select#maj").append("<option value=0> Computer science </option>");
            }*/
        if ($("select#fac2 option:selected").val() == "FoS") {
            $("select#maj2 option").remove();
			$("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Applied Mathematics'> Applied Mathematics </option>");
            $("select#maj2").append("<option value='Chemistry'> Chemistry </option>");
            $("select#maj2").append("<option value='Computational Biology'> Computational Biology </option>");
            $("select#maj2").append("<option value='Food Science and Technology'> Food Science and Technology</option>");
            $("select#maj2").append("<option value='Life Sciences'> Life Sciences </option>");
            $("select#maj2").append("<option value='Mathematics'> Mathematics </option>");
            $("select#maj2").append("<option value='Pharmacy'> Pharmacy </option>");
            $("select#maj2").append("<option value='Physics'> Physics </option>");
            $("select#maj2").append("<option value='Quantitative Finance'> Quantitative Finance</option>");
            $("select#maj2").append("<option value='Statistics'> Statistics </option>");
        } else if ($("select#fac2 option:selected").val() == "SoC") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Business Analytics'> Business Analytics </option>");
            $("select#maj2").append("<option value='Computational Biology'> Computational Biology</option>");
            $("select#maj2").append("<option value='Computer Engineering'> Computer Engineering</option>");
            $("select#maj2").append("<option value='Computer Science'> Computer Science </option>");
            $("select#maj2").append("<option value='Electronic Commerce'> Electronic Commerce</option>");
            $("select#maj2").append("<option value='Information Systems'> Information Systems </option>");
        } else {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
        }
            
    })
    

    $("#accomcost").change(function() {
        var accom = parseInt($("#accomcost").val(),10);
        var food = parseInt($("#foodcost").val(),10);
        var trans = parseInt($("#transportcost").val(), 10);
        var acad = parseInt($("#acadcost").val(),10);
        var others = parseInt($("#othercost").val(),10);
        var total = accom + food + trans + acad + others;
        $("span#totalcost").html(total);
    })
    
    $("#foodcost").change(function() {
        var accom = parseInt($("#accomcost").val(),10);
        var food = parseInt($("#foodcost").val(),10);
        var trans = parseInt($("#transportcost").val(), 10);
        var acad = parseInt($("#acadcost").val(),10);
        var others = parseInt($("#othercost").val(),10);
        var total = accom + food + trans + acad + others;
        $("span#totalcost").html(total);    
    })

    $("#transportcost").change(function() {
        var accom = parseInt($("#accomcost").val(),10);
        var food = parseInt($("#foodcost").val(),10);
        var trans = parseInt($("#transportcost").val(), 10);
        var acad = parseInt($("#acadcost").val(),10);
        var others = parseInt($("#othercost").val(),10);
        var total = accom + food + trans + acad + others;
        $("span#totalcost").html(total);
    })
    
    $("#acadcost").change(function() {
        var accom = parseInt($("#accomcost").val(),10);
        var food = parseInt($("#foodcost").val(),10);
        var trans = parseInt($("#transportcost").val(), 10);
        var acad = parseInt($("#acadcost").val(),10);
        var others = parseInt($("#othercost").val(),10);
        var total = accom + food + trans + acad + others;
        $("span#totalcost").html(total);    
    })
    
    $("#othercost").change(function() {
        var accom = parseInt($("#accomcost").val(),10);
        var food = parseInt($("#foodcost").val(),10);
        var trans = parseInt($("#transportcost").val(), 10);
        var acad = parseInt($("#acadcost").val(),10);
        var others = parseInt($("#othercost").val(),10);
        var total = accom + food + trans + acad + others;
        $("span#totalcost").html(total);
    })

    $("#reviewform").validate({
        rules: {
            year: {
                required: true,
                integer: true,
                min: 2000,
                max: 2100
            },
            accomcost: {
                integer:true,
                min:0
            },
            foodcost: {
                integer: true,
                min: 0
            },
            transportcost: {
                integer: true,
                min: 0
            },
            acadcost: {
                integer: true,
                min: 0
            },
            othercost: {
                integer: true,
                min: 0
            },
            cred1: {
                required: {
                    depends: function(element) {
                        return $("#mod1").val()!="";
                    }
                }
            },
            nmod1: {
                required: {
                    depends: function(element) {
                        return $("#mod1").val()!="";
                    }
                } 
            },
            mc1: {
                required: {
                    depends: function(element) {
                        return $("#mod1").val()!="";
                    }
                }
            },
            cred2: {
                required: {
                    depends: function(element) {
                        return $("#mod2").val()!="";
                    }
                }
            },
            nmod2: {
                required: {
                    depends: function(element) {
                        return $("#mod2").val()!="";
                    }
                } 
            },
            mc2: {
                required: {
                    depends: function(element) {
                        return $("#mod2").val()!="";
                    }
                }
            },
            cred3: {
                required: {
                    depends: function(element) {
                        return $("#mod3").val()!="";
                    }
                }
            },
            nmod3: {
                required: {
                    depends: function(element) {
                        return $("#mod3").val()!="";
                    }
                } 
            },
            mc3: {
                required: {
                    depends: function(element) {
                        return $("#mod3").val()!="";
                    }
                }
            },
            cred4: {
                required: {
                    depends: function(element) {
                        return $("#mod4").val()!="";
                    }
                }
            },
            nmod4: {
                required: {
                    depends: function(element) {
                        return $("#mod4").val()!="";
                    }
                } 
            },
            mc4: {
                required: {
                    depends: function(element) {
                        return $("#mod4").val()!="";
                    }
                }
            },
            cred5: {
                required: {
                    depends: function(element) {
                        return $("#mod5").val()!="";
                    }
                }
            },
            nmod5: {
                required: {
                    depends: function(element) {
                        return $("#mod5").val()!="";
                    }
                } 
            },
            mc5: {
                required: {
                    depends: function(element) {
                        return $("#mod5").val()!="";
                    }
                }
            },
            cred6: {
                required: {
                    depends: function(element) {
                        return $("#mod6").val()!="";
                    }
                }
            },
            nmod6: {
                required: {
                    depends: function(element) {
                        return $("#mod6").val()!="";
                    }
                } 
            },
            mc6: {
                required: {
                    depends: function(element) {
                        return $("#mod6").val()!="";
                    }
                }
            },
            cred7: {
                required: {
                    depends: function(element) {
                        return $("#mod7").val()!="";
                    }
                }
            },
            nmod7: {
                required: {
                    depends: function(element) {
                        return $("#mod7").val()!="";
                    }
                } 
            },
            mc7: {
                required: {
                    depends: function(element) {
                        return $("#mod7").val()!="";
                    }
                }
            },
            cred8: {
                required: {
                    depends: function(element) {
                        return $("#mod8").val()!="";
                    }
                }
            },
            nmod8: {
                required: {
                    depends: function(element) {
                        return $("#mod8").val()!="";
                    }
                } 
            },
            mc8: {
                required: {
                    depends: function(element) {
                        return $("#mod8").val()!="";
                    }
                }
            },
            cred9: {
                required: {
                    depends: function(element) {
                        return $("#mod9").val()!="";
                    }
                }
            },
            nmod9: {
                required: {
                    depends: function(element) {
                        return $("#mod9").val()!="";
                    }
                } 
            },
            mc9: {
                required: {
                    depends: function(element) {
                        return $("#mod9").val()!="";
                    }
                }
            },
            cred10: {
                required: {
                    depends: function(element) {
                        return $("#mod10").val()!="";
                    }
                }
            },
            nmod10: {
                required: {
                    depends: function(element) {
                        return $("#mod10").val()!="";
                    }
                } 
            },
            mc10: {
                required: {
                    depends: function(element) {
                        return $("#mod10").val()!="";
                    }
                }
            }
        },
        messages: {
            year: {
                integer: "Pls enter a valid year.",
                min: "Pls enter a valid year.",
                max: "Pls enter a valid year."
            },
            accomcost: {
                integer: "Pls enter an integer value.",
                min: "Pls enter an integer greater than or equal to 0."
            },
            transportcost: {
                integer: "Pls enter an integer value.",
                min: "Pls enter an integer greater than or equal to 0."
            },
            acadcost: {
                integer: "Pls enter an integer value.",
                min: "Pls enter an integer greater than or equal to 0."
            },
            foodcost: {
                integer: "Pls enter an integer value.",
                min: "Pls enter an integer greater than or equal to 0."
            },
            othercost: {
                integer: "Pls enter an integer value.",
                min: "Pls enter an integer greater than or equal to 0."
            }
        },
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
        }
    });
});
