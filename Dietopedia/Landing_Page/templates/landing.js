function BMR() {
    var h=document.getElementById('heig').value;
    var w=document.getElementById('weiko').value;
    var a=document.getElementById('ageee').value;
    var g=document.getElementById('gen').value;
    if (g=="1"){
      bmr =66+(6.23*w)+(12.7*h)-(6.8*a);
    }
    else if (g=="2"){
      bmr =655+(4.35*w)+(4.7*h)-(4.7*a);
    }


    document.getElementById("result").innerHTML="Your BMR is " + bmr;
    alert(bmr);
  }
  