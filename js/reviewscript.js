$(document).ready(function(){
        /*$("#btn1").click(function(){
          $("select").append("<option value=0> Physics </option>");*/
         /* $("#maj").replaceWith("<select name="major" required>
                         <option value=0> Select Major </option><option value="Physics"> Physics </option>
                      </select>"); */
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
    
    $("#reviewform").validate({
        rules: {
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
        }
    });
});