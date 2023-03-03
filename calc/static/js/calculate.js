let field1 = document.getElementById("id_water_current");
let field2 = document.getElementById("id_water_past");
let field3 = document.getElementById("id_water_tariff");
let field4 = document.getElementById("id_electricity_current");
let field5 = document.getElementById("id_electricity_past");
let field6 = document.getElementById("id_electricity_tariff");
let result = document.getElementById("result");
let calculate = () => {
  let ecurrent = Number(document.getElementById("id_electricity_current").value);
  let epast = Number(document.getElementById("id_electricity_past").value);
  let etariff = Number(document.getElementById("id_electricity_tariff").value);
  let e_sum_to_pay = (ecurrent-epast)*etariff;
  let wcurrent = Number(document.getElementById("id_water_current").value);
  let wpast = Number(document.getElementById("id_water_past").value);
  let wtariff = Number(document.getElementById("id_water_tariff").value);
  let w_sum_to_pay = (wcurrent-wpast)*wtariff;

  if (ecurrent >= epast | wcurrent >= wpast){
    result.innerHTML = `<div>Amount payable for electricity: <span>${e_sum_to_pay.toFixed(2)} UAH </span></div>
  <div>Amount payable for water: <span>${w_sum_to_pay.toFixed(2)} UAH </span></div>`;
  }
  else {
  result.innerHTML = `<div>Please enter the correct values of the meter readings</div>`;
  }
};

field1.addEventListener("input", calculate);
field2.addEventListener("input", calculate);
field3.addEventListener("input", calculate);
field4.addEventListener("input", calculate);
field5.addEventListener("input", calculate);
field6.addEventListener("input", calculate);
window.addEventListener("load", calculate);
