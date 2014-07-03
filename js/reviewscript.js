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
            $("select#maj").append("<option value=0> Select Major </option>");
            $("select#maj").append("<option value=1> Applied Mathematics </option>");
            $("select#maj").append("<option value=2> Chemistry </option>");
            $("select#maj").append("<option value=3> Computational Biology </option>");
            $("select#maj").append("<option value=4> Food Science and Technology</option>");
            $("select#maj").append("<option value=5> Life Sciences </option>");
            $("select#maj").append("<option value=6> Mathematics </option>");
            $("select#maj").append("<option value=7> Pharmacy </option>");
            $("select#maj").append("<option value=8> Physics </option>");
            $("select#maj").append("<option value=9> Quantitative Finance</option>");
            $("select#maj").append("<option value=10> Statistics </option>");
        } else if ($("select#fac option:selected").val() == "SoC") {
            $("select#maj option").remove();
            $("select#maj").append("<option value=0> Select Major </option>");
            $("select#maj").append("<option value=1> Business Analytics </option>");
            $("select#maj").append("<option value=2> Computational Biology</option>");
            $("select#maj").append("<option value=3> Computer Engineering</option>");
            $("select#maj").append("<option value=4> Computer Science </option>");
            $("select#maj").append("<option value=5> Electronic Commerce</option>");
            $("select#maj").append("<option value=6> Information Systems </option>");
        } else {
            $("select#maj option").remove();
            $("select#maj").append("<option value=0> Select Major </option>");
        }
            
    })
});