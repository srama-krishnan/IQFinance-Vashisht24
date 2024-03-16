function validateForm() {
    var savings = document.forms["financialForm"]["savings"].value;
    var investment = document.forms["financialForm"]["investment"].value;
    if (savings <= 0 || investment <= 0) {
      alert("Both amounts must be positive numbers.");
      return false;
    }
    return true;
  }