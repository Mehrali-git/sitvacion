$(document).on('click', '#submit', function () {
    $forms = $('form');
    var allvalid = true;
    $($forms).each(function (index, $form) {
        $inputs = $($form).find('input');

        $($inputs).each(function (index, $input) {
            if ($($input).val() == "") {
                document.getElementById($input.id).value = 0;
                $($input).val = 0;
                allvalid = false;
            }
        });
    });
});

function convertNumbers2English(input) {
    try {
        var persianDigits = "۰۱۲۳۴۵۶۷۸۹";
        return input.replace(/[\u06F0-\u06F90]/g, function (m) {
            return persianDigits.indexOf(m);
        });
    } catch (ex) {
        return input;
    }

}

function validateNumber(event) {
    var key = window.event ? event.keyCode : event.which;
    if (event.keyCode === 8) {
        return true;
    } else if (key < 48 || key > 57) {
        return false;
    } else {
        return true;
    }
};
$(document).ready(function () {
    $('[id*=es]').keypress(validateNumber);
    $('[id*=n_]').keypress(validateNumber);
    $('[id*=ir_]').keypress(validateNumber);
    $('[id*=t_]').keypress(validateNumber);
    $('[id*=sek_]').keypress(validateNumber);
    $('[id*=pardakht]').keypress(validateNumber);
    $('[id*=daryaft]').keypress(validateNumber);
});

function final_cash() {
    try {

        var man = ex_normalNum(document.getElementById("id_total_yesterday").value);
        var dar = ex_normalNum(document.getElementById("id_daryaft").value);
        var par = ex_normalNum(document.getElementById("id_pardakht").value);
        var sum_esk_nik_ir = ex_normalNum(document.getElementById("id_sum_esk_nik_ir").value);
        var result = (parseInt(man) + parseInt(dar)) - parseInt(par);
        differnt = parseInt(sum_esk_nik_ir) - result;

        document.getElementById("cash").innerHTML = result;
        document.getElementById("diff_cash").innerHTML = differnt;
        document.getElementById("diffrent_display").innerHTML = document.getElementById("diff_cash").innerHTML;
        if (differnt == 0) {
            document.getElementById("diff_cash").style.backgroundColor = "#0ab00a";
            document.getElementById("submit").disabled = false;
            document.getElementById("submit").value = "ارسال";
        }
        if (differnt > 0) {
            document.getElementById("diff_cash").style.backgroundColor = "#fcc201";
            document.getElementById("submit").disabled = true;
            document.getElementById("submit").value = "عدم امکان ارسال به علت وجود اختلاف";
        }
        if (differnt < 0) {
            document.getElementById("diff_cash").style.backgroundColor = "#dc3545";
            document.getElementById("submit").disabled = true;
            document.getElementById("submit").value = "عدم امکان ارسال به علت وجود اختلاف";
        }
    } catch (ex) {
        alert("final_Cash");
    }
}

function Un_separateNum() {
    try {
        document.getElementById("id_es_1").value = ex_normalNum(document.getElementById("id_es_1").value);
        document.getElementById("id_es_2").value = ex_normalNum(document.getElementById("id_es_2").value);
        document.getElementById("id_es_5").value = ex_normalNum(document.getElementById("id_es_5").value);
        document.getElementById("id_es_10").value = ex_normalNum(document.getElementById("id_es_10").value);
        document.getElementById("id_es_20").value = ex_normalNum(document.getElementById("id_es_20").value);
        document.getElementById("id_es_50").value = ex_normalNum(document.getElementById("id_es_50").value);
        document.getElementById("id_es_100").value = ex_normalNum(document.getElementById("id_es_100").value);
        document.getElementById("id_es_far").value = ex_normalNum(document.getElementById("id_es_far").value);

        document.getElementById("id_n_1").value = ex_normalNum(document.getElementById("id_n_1").value);
        document.getElementById("id_n_2").value = ex_normalNum(document.getElementById("id_n_2").value);
        document.getElementById("id_n_5").value = ex_normalNum(document.getElementById("id_n_5").value);
        document.getElementById("id_n_10").value = ex_normalNum(document.getElementById("id_n_10").value);

        document.getElementById("id_ir_50").value = ex_normalNum(document.getElementById("id_ir_50").value);
        document.getElementById("id_ir_100").value = ex_normalNum(document.getElementById("id_ir_100").value);
        document.getElementById("id_ir_far").value = ex_normalNum(document.getElementById("id_ir_far").value);

        document.getElementById("id_t_m").value = ex_normalNum(document.getElementById("id_t_m").value);
        document.getElementById("id_t_va").value = ex_normalNum(document.getElementById("id_t_va").value);
        document.getElementById("id_t_ch_25").value = ex_normalNum(document.getElementById("id_t_ch_25").value);
        document.getElementById("id_t_ch_50").value = ex_normalNum(document.getElementById("id_t_ch_50").value);
        document.getElementById("id_t_ch_100").value = ex_normalNum(document.getElementById("id_t_ch_100").value);
        document.getElementById("id_t_ch_hav").value = ex_normalNum(document.getElementById("id_t_ch_hav").value);
        document.getElementById("id_t_ch_taz").value = ex_normalNum(document.getElementById("id_t_ch_taz").value);
        document.getElementById("id_t_pard").value = ex_normalNum(document.getElementById("id_t_pard").value);
        document.getElementById("id_t_saf").value = ex_normalNum(document.getElementById("id_t_saf").value);

        document.getElementById("id_daryaft").value = ex_normalNum(document.getElementById("id_daryaft").value);
        document.getElementById("id_pardakht").value = ex_normalNum(document.getElementById("id_pardakht").value);
        document.getElementById("id_total_yesterday").value = ex_normalNum(document.getElementById("id_total_yesterday").value);

    } catch (ex) {
        alert(ex + "برداشت ویرگول");
    }

}

function sandgo() {
    var esk = ex_normalNum(document.getElementById("eskenas").innerHTML);
    var nikl = ex_normalNum(document.getElementById("n_sum").innerHTML);
    var ir_ch = ex_normalNum(document.getElementById("ir_sum").innerHTML);
    var c = parseInt(esk) + parseInt(nikl) + parseInt(ir_ch);
    document.getElementById("sum_esk_nik_ir").innerHTML = separateNum(c);
    document.getElementById("id_sum_esk_nik_ir").value = separateNum(c);
}

function sum_row(x, y, z, row) {
    var a = document.getElementById(x).value;
    var b = document.getElementById(y).value;
    var c = ((a * 100) * row) + (b * row)
    document.getElementById(z).value = separateNum(c);
}

function sum_split_row(x, y, z, row) {
    var s3 = document.getElementById(z).value;
    num = ex_normalNum(s3);
    temp = num / (100 * row);
    var box = parseInt(temp)
    document.getElementById(x).value = box;
    document.getElementById(y).value = separateNum((num - (box * 100) * row) / row);
}

function sum_row_tamr(input, result, row) {
    var var1 = parseInt(document.getElementById(input).value);
    if (!isNaN(var1)) {
        var var2 = var1 * row;
        document.getElementById(result).value = separateNum(var2);
    } else
        document.getElementById(result).value = "0";
}

function sum_row_tamr_chek(input, result, count, row) {
    var var1 = parseInt(document.getElementById(input).value);
    if (!isNaN(var1)) {
        var var2 = (var1 * row) * count;
        document.getElementById(result).value = separateNum(var2);
    } else
        document.getElementById(result).value = "ورودی نامشخص";
}

//         /* seprate number input 3 number */#}
function separateNum(value, input) {
    var nStr = value + '';
    nStr = nStr.replace(/\,/g, "");
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    if (input !== undefined) {

        input.value = x1 + x2;
    } else {
        return x1 + x2;
    }
}

function ex_normalNum(num) {
    num = num.replace(/,\s?/g, "");
    return (num);
}

// var debugScript = true;#}
function computeTableColumnTotal(tableId, colNumber) {
    // find the table with id attribute tableId
    // return the total of the numerical elements in column colNumber
    // skip the top row (headers) and bottom row (where the total will go)
    var result = 0;

    try {
        var tableElem = window.document.getElementById(tableId);
        var tableBody = tableElem.getElementsByTagName("tbody").item(0);

        var howManyRows = tableBody.rows.length;

        for (var i = 1; i < (howManyRows - 1); i++) // skip first and last row (hence i=1, and howManyRows-1)
        {
            var thisTrElem = tableBody.rows[i];
            var thisTdElem = thisTrElem.cells[colNumber];
            try {
                var thisTextNode = ex_normalNum(thisTdElem.querySelector('input').value);
            } catch (ex) {
                var thisTextNode = 0;
            }
            //   var thisTextNode = thisTdElem.childNodes.item(0);#}
            //      if (debugScript)#}
            //      {#}
            //         window.alert("text is " + thisTextNode.data);#}
            //      } // end if#}
            // try to convert text to numeric
            var thisNumber = parseInt(thisTextNode);
            // if you didn't get back the value NaN (i.e. not a number), add into result
            if (!isNaN(thisNumber))
                result += thisNumber;

        } // end for

    } // end try
    catch (ex) {
        window.alert("Exception in function computeTableColumnTotal()\n" + ex);
        result = 0;
    } finally {
        return result;
    }

}


$(document).ready(function () {
    $("input").keyup(function () {
        document.getElementById("eskenas").innerHTML = separateNum(computeTableColumnTotal("esk", 4));
        document.getElementById("es_b").innerHTML = separateNum(computeTableColumnTotal("esk", 2));
        document.getElementById("es_g").innerHTML = separateNum(computeTableColumnTotal("esk", 3));
        document.getElementById("n_sum").innerHTML = separateNum(computeTableColumnTotal("nikl", 3));
        document.getElementById("n_g").innerHTML = separateNum(computeTableColumnTotal("nikl", 2));
        document.getElementById("ir_b").innerHTML = separateNum(computeTableColumnTotal("ir_chek", 2));
        document.getElementById("ir_g").innerHTML = separateNum(computeTableColumnTotal("ir_chek", 3));
        document.getElementById("ir_sum").innerHTML = separateNum(computeTableColumnTotal("ir_chek", 4));
        document.getElementById("tambr_g").innerHTML = separateNum(computeTableColumnTotal("tambr", 2));
        document.getElementById("tambr_sum").innerHTML = separateNum(computeTableColumnTotal("tambr", 3));
        document.getElementById("seke_sum").innerHTML = separateNum(computeTableColumnTotal("seke", 2));

        document.getElementById("id_es_far").value = separateNum(document.getElementById("id_es_far").value);
        document.getElementById("id_ir_far").value = separateNum(document.getElementById("id_ir_far").value);
        sandgo();
        final_cash();

        document.getElementById("id_total_yesterday").value = separateNum(document.getElementById("id_total_yesterday").value);
        document.getElementById("cash").innerHTML = separateNum(document.getElementById("cash").innerHTML);
        document.getElementById("id_daryaft").value = separateNum(document.getElementById("id_daryaft").value);
        document.getElementById("id_pardakht").value = separateNum(document.getElementById("id_pardakht").value);
        document.getElementById("diff_cash").innerHTML = separateNum(document.getElementById("diff_cash").innerHTML);
        document.getElementById("diffrent_display").innerHTML = document.getElementById("diff_cash").innerHTML;
    });
});

window.onload = function () {
    try {

        document.getElementById("submit").disabled = true;

        document.getElementById("id_es_1").value = separateNum(document.getElementById("id_es_1").value);
        sum_split_row('es_1_b', 'es_1_g', 'id_es_1', '1000');
        document.getElementById("id_es_2").value = separateNum(document.getElementById("id_es_2").value);
        sum_split_row('es_2_b', 'es_2_g', 'id_es_2', '2000');
        document.getElementById("id_es_5").value = separateNum(document.getElementById("id_es_5").value);
        sum_split_row('es_5_b', 'es_5_g', 'id_es_5', '5000');
        document.getElementById("id_es_10").value = separateNum(document.getElementById("id_es_10").value);
        sum_split_row('es_10_b', 'es_10_g', 'id_es_10', '10000');
        document.getElementById("id_es_20").value = separateNum(document.getElementById("id_es_20").value);
        sum_split_row('es_20_b', 'es_20_g', 'id_es_20', '20000');
        document.getElementById("id_es_50").value = separateNum(document.getElementById("id_es_50").value);
        sum_split_row('es_50_b', 'es_50_g', 'id_es_50', '50000');
        document.getElementById("id_es_100").value = separateNum(document.getElementById("id_es_100").value);
        sum_split_row('es_100_b', 'es_100_g', 'id_es_100', '100000');
        document.getElementById("id_es_far").value = separateNum(document.getElementById("id_es_far").value);

        document.getElementById("id_n_1").value = separateNum(document.getElementById("id_n_1").value);
        document.getElementById("id_n_2").value = separateNum(document.getElementById("id_n_2").value);
        document.getElementById("id_n_5").value = separateNum(document.getElementById("id_n_5").value);
        document.getElementById("id_n_10").value = separateNum(document.getElementById("id_n_10").value);

        document.getElementById("id_ir_50").value = separateNum(document.getElementById("id_ir_50").value);
        sum_split_row('ir_50_b', 'ir_50_g', 'id_ir_50', '500000');
        document.getElementById("id_ir_100").value = separateNum(document.getElementById("id_ir_100").value);
        sum_split_row('ir_100_b', 'ir_100_g', 'id_ir_100', '1000000');
        document.getElementById("id_ir_far").value = separateNum(document.getElementById("id_ir_far").value);

        document.getElementById("id_daryaft").value = separateNum(document.getElementById("id_daryaft").value);
        document.getElementById("id_pardakht").value = separateNum(document.getElementById("id_pardakht").value);

        document.getElementById("eskenas").innerHTML = separateNum(computeTableColumnTotal("esk", 4));
        document.getElementById("n_sum").innerHTML = separateNum(computeTableColumnTotal("nikl", 3));
        document.getElementById("ir_sum").innerHTML = separateNum(computeTableColumnTotal("ir_chek", 4));

        sandgo();
        final_cash();

        document.getElementById("id_total_yesterday").value = separateNum(document.getElementById("id_total_yesterday").value);
        document.getElementById("cash").innerHTML = separateNum(document.getElementById("cash").innerHTML);
        document.getElementById("id_daryaft").value = separateNum(document.getElementById("id_daryaft").value);
        document.getElementById("diff_cash").innerHTML = separateNum(document.getElementById("diff_cash").innerHTML);
        document.getElementById("diffrent_display").innerHTML = document.getElementById("diff_cash").innerHTML;
    } catch (ex) {
        alert(ex);
    }
}
$(document).ready(function () {
    $("#tambr,#nikl,#esk,#ir_chek").hover(function () {
        if (document.getElementById("diff_cash").innerHTML != 0) {
            $("#diffrentSandogh").show(1300);
            document.getElementById("diffrent_display").innerHTML = document.getElementById("diff_cash").innerHTML;
        }
    });

    $("#sandogh,#submit").hover(function () {
        $("#diffrentSandogh").hide(1300);
    });

});
$("input[type=text]").focus(function () {
    $(this).select();
});
$("input").focus(function (){
   $(this).css({'background':'#fcff64'});
});
$("input").focusout(function (){
   $(this).css({'background':'#fff'});
});

