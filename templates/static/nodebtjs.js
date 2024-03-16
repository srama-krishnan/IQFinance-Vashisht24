function validateForm() {
    let fields = ["SeriousDlqin2yr", "RevolvingUtilizationOfUnsecuredLines", "age", "NumberOfTime3059DaysPastDueNotWorse", "DebtRatio", "MonthlyIncome", "NumberOfOpenCreditLinesAndLoans", "NumberOfTimes90DaysLate", "NumberRealEstateLoansOrLines", "NumberOfTime6089DaysPastDueNotWorse", "NumberOfDependents"];
    for (let i = 0; i < fields.length; i++) {
        let x = document.forms["myForm"][fields[i]].value;
        if (x == "") {
            alert("All fields must be filled out");
            return false;
        }
    }
    return true;
}