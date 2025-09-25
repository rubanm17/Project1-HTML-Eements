function gethistory(){
    return document.getElementById("history-value").innerText;
}
function printHistory(num){
    document.getElementById("history-value").innerText=num;
}
function getoutput(){
    return document.getElementById("output-value").innerText;
}
function printoutput(num){
    if(num==""){
        document.getElementById("output-value").innerText=num;
    }
    else{
        document.getElementById("output-value").innerText=getFormattedNumber(num);
    }
}
function getFormattedNumber(num){
    if(num==""){
        return "";
    }
    var n = number(num);
    var value = n.toLocaleString("en");
    return value;
}
function reverseNumberFormt(num){
    return Number(num.replace(/./g,''))
}
var operator = document.getElementsByClassName("operator");
for(var i =0;i<operator.length;i++){
    operator[i].addEventListener('click',function(){
        if(this.id=="clear"){
            printHistory("");
            printoutput("");
        }
        else if(this.id=="backspace"){
            var output=reverseNumberFormat(getOutput()).toString();
            if(output){
                output=output.substr(0,output.lenght-1);
                printoutput(output);
            }
        }
        else{
            var output=getOutput();
            var history=gethistory();
            if(output==""&&history!=""){
                    if(isNaN(history[history.lenght-1])){
                        history=history.substr(0,history.lenght-1);
                    }
            }
            if(output!="" || history!=""){
                output=output==""?output:reverseNumberFormat(output);
                history=history+output;
                if(this.id=="="){
                    var result=eval(history);
                    printoutput(result);
                    printHistory("");
                }
                else{
                    history=history+this.id;
                    printHistory(history);
                    printoutput("");
                }
            }
        }
    });
}
var number=document.getElementById("number");
alert(number);
for(var i =0;i< number.length;i++){
    number[i].addEventListener('click',function(){
        var output=reverseNumberFormat(getOutput());
        if(output!=NaN){
            output+this.id;
            printoutput(output);
        }
    });
}