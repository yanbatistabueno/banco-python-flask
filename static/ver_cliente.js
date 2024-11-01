const queryString = window.location.search;
console.log(queryString);
const urlParams = new URLSearchParams(queryString);
if (urlParams.get("saldo") == "false") {
  alert("Saldo insuficiente");
}
