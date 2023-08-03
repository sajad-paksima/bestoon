/submit/expense/
    POST, return a json
    input: date (optional), token, amount, text
    output: status:ok
    
/submit/income/
    POST, return a json
    input: date (optional), token, amount, text
    output: status:ok

/accounts/register/
    step1:
        POST
        input: username, email, password
        output: status:ok
    step2:
        GET
        input: email, code
        output: status:ok (shows the token)

/q/generalstat/
    POST, return a json
    input: fromdate(optional), todate(optional), token
    output: json from some stats related to this user
    