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
        } else if ($("select#fac option:selected").val() == "FASS") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Chinese Language'> Chinese Language </option>");
            $("select#maj").append("<option value='Chinese Studies'> Chinese Studies </option>");
            $("select#maj").append("<option value='Communications and New Media'> Communications and New Media </option>");
            $("select#maj").append("<option value='Economics'> Economics </option>");
            $("select#maj").append("<option value='English Language'> English Language </option>");
            $("select#maj").append("<option value='English Literature'> English Literature </option>");
            $("select#maj").append("<option value='European Studies'> European Studies </option>");
            $("select#maj").append("<option value='Geography'> Geography </option>");
            $("select#maj").append("<option value='History'> History </option>");
            $("select#maj").append("<option value='Japanese Studies'> Japanese Studies </option>");
            $("select#maj").append("<option value='Malay Studies'> Malay Studies </option>");
            $("select#maj").append("<option value='Philosophy'> Philosophy </option>");
            $("select#maj").append("<option value='Political Science'> Political Science </option>");
            $("select#maj").append("<option value='Psychology'> Psychology </option>");
            $("select#maj").append("<option value='Social Work'> Social Work </option>");
            $("select#maj").append("<option value='Sociology'> Sociology </option>");
            $("select#maj").append("<option value='South Asian Studies'> South Asian Studies </option>");
            $("select#maj").append("<option value='Southeast Asian Studies'> Southeast Asian Studies </option>");
            $("select#maj").append("<option value='Theatre Studies'> Theatre Studies </option>");
        } else if ($("select#fac option:selected").val() == "Biz") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Business Administration'> Business Administration </option>");
            $("select#maj").append("<option value='Business Administration (Accountancy)'> Business Administration (Accountancy) </option>");
        } else if ($("select#fac option:selected").val() == "FoD") {
            $("select#maj option").remove();
            $("select#maj").append("<option value='Dentistry'> Dentistry </option>");
            $("select#maj").val("Dentistry");
        } else if ($("select#fac option:selected").val() == "SDE") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Architecture'> Architecture </option>");
            $("select#maj").append("<option value='Industrial Design'> Industrial Design </option>");
            $("select#maj").append("<option value='Project and Facilities Management'> Project and Facilities Management </option>");
            $("select#maj").append("<option value='Real Estate'> Real Estate </option>");
        } else if ($("select#fac option:selected").val() == "FoE") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Biomedical Engineering'> Biomedical Engineering </option>");
            $("select#maj").append("<option value='Chemical & Biomolecular Engineering'> Chemical & Biomolecular Engineering </option>");
            $("select#maj").append("<option value='Civil & Environmental Engineering'> Civil & Environmental Engineering </option>");
            $("select#maj").append("<option value='Electrical & Computer Engineering'> Electrical & Computer Engineering </option>");
            $("select#maj").append("<option value='Engineering & Technology Management'> Engineering & Technology Management </option>");
            $("select#maj").append("<option value='Industrial & Systems Engineering'> Industrial & Systems Engineering </option>");
            $("select#maj").append("<option value='Materials Science & Engineering'> Materials Science & Engineering </option>");
            $("select#maj").append("<option value='Mechanical Engineering'> Mechanical Engineering </option>");
        } else if ($("select#fac option:selected").val() == "Law") {
            $("select#maj option").remove();
            $("select#maj").append("<option value='Law'> Law </option>");
            $("select#maj").val("Law");
        } else if ($("select#fac option:selected").val() == "Med") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Medicine'> Medicine </option>");
            $("select#maj").append("<option value='Nursing'> Nursing </option>");
        } else if ($("select#fac option:selected").val() == "YSTCM") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=> Select Major </option>");
            $("select#maj").append("<option value='Performance'> Performance </option>");
            $("select#maj").append("<option value='Composition'> Composition </option>");
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
            $("select#fac2").append("<option value='FASS'> Faculty of Arts and Social Sciences </option>");
            $("select#fac2").append("<option value='Biz'> Business School </option>");
            $("select#fac2").append("<option value='SoC'> School of Computing </option>");
            $("select#fac2").append("<option value='FoD'> Faculty of Dentistry </option>");
            $("select#fac2").append("<option value='SDE'> School of Design and Environment</option>");
            $("select#fac2").append("<option value='FoE'> Faculty of Engineering </option>");
            $("select#fac2").append("<option value='Law'> Faculty of Law </option>");
            $("select#fac2").append("<option value='Med'> Yong Loo Lin School of Medicine </option>");
            $("select#fac2").append("<option value='YSTCM'> Yong Siew Toh Conservatory of Music </option>");
            $("select#fac2").append("<option value='FoS'> Faculty of Science </option>");
		} else {
			$("select#maj2 option").remove();
			$("select#maj2").append("<option value=> Select Major/Minor </option>");
			$("select#fac2 option").remove();
			$("select#fac2").append("<option value=> Select Faculty </option>");
		}
	})

	$("select#fac2").change(function() {
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
        } else if ($("select#fac2 option:selected").val() == "FASS") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Chinese Language'> Chinese Language </option>");
            $("select#maj2").append("<option value='Chinese Studies'> Chinese Studies </option>");
            $("select#maj2").append("<option value='Communications and New Media'> Communications and New Media </option>");
            $("select#maj2").append("<option value='Economics'> Economics </option>");
            $("select#maj2").append("<option value='English Language'> English Language </option>");
            $("select#maj2").append("<option value='English Literature'> English Literature </option>");
            $("select#maj2").append("<option value='European Studies'> European Studies </option>");
            $("select#maj2").append("<option value='Geography'> Geography </option>");
            $("select#maj2").append("<option value='History'> History </option>");
            $("select#maj2").append("<option value='Japanese Studies'> Japanese Studies </option>");
            $("select#maj2").append("<option value='Malay Studies'> Malay Studies </option>");
            $("select#maj2").append("<option value='Philosophy'> Philosophy </option>");
            $("select#maj2").append("<option value='Political Science'> Political Science </option>");
            $("select#maj2").append("<option value='Psychology'> Psychology </option>");
            $("select#maj2").append("<option value='Social Work'> Social Work </option>");
            $("select#maj2").append("<option value='Sociology'> Sociology </option>");
            $("select#maj2").append("<option value='South Asian Studies'> South Asian Studies </option>");
            $("select#maj2").append("<option value='Southeast Asian Studies'> Southeast Asian Studies </option>");
            $("select#maj2").append("<option value='Theatre Studies'> Theatre Studies </option>");
        } else if ($("select#fac2 option:selected").val() == "Biz") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Business Administration'> Business Administration </option>");
            $("select#maj2").append("<option value='Business Administration (Accountancy)'> Business Administration (Accountancy) </option>");
        } else if ($("select#fac2 option:selected").val() == "FoD") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value='Dentistry'> Dentistry </option>");
            $("select#maj2").val("Dentistry");
        } else if ($("select#fac2 option:selected").val() == "SDE") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Architecture'> Architecture </option>");
            $("select#maj2").append("<option value='Industrial Design'> Industrial Design </option>");
            $("select#maj2").append("<option value='Project and fac2ilities Management'> Project and fac2ilities Management </option>");
            $("select#maj2").append("<option value='Real Estate'> Real Estate </option>");
        } else if ($("select#fac2 option:selected").val() == "FoE") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Biomedical Engineering'> Biomedical Engineering </option>");
            $("select#maj2").append("<option value='Chemical & Biomolecular Engineering'> Chemical & Biomolecular Engineering </option>");
            $("select#maj2").append("<option value='Civil & Environmental Engineering'> Civil & Environmental Engineering </option>");
            $("select#maj2").append("<option value='Electrical & Computer Engineering'> Electrical & Computer Engineering </option>");
            $("select#maj2").append("<option value='Engineering & Technology Management'> Engineering & Technology Management </option>");
            $("select#maj2").append("<option value='Industrial & Systems Engineering'> Industrial & Systems Engineering </option>");
            $("select#maj2").append("<option value='Materials Science & Engineering'> Materials Science & Engineering </option>");
            $("select#maj2").append("<option value='Mechanical Engineering'> Mechanical Engineering </option>");
        } else if ($("select#fac2 option:selected").val() == "Law") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value='Law'> Law </option>");
            $("select#maj2").val("Law");
        } else if ($("select#fac2 option:selected").val() == "Med") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Medicine'> Medicine </option>");
            $("select#maj2").append("<option value='Nursing'> Nursing </option>");
        } else if ($("select#fac2 option:selected").val() == "YSTCM") {
            $("select#maj2 option").remove();
            $("select#maj2").append("<option value=> Select Major/Minor </option>");
            $("select#maj2").append("<option value='Performance'> Performance </option>");
            $("select#maj2").append("<option value='Composition'> Composition </option>");
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
