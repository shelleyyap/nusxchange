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
});