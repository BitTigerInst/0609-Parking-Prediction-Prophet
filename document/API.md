###GET domain/
return raw html file
<br /><br />

###GET domain/:month
return predicted data of that month in json<br />
month format: YYYYMM<br />
for invalid parameter, redirect to the current month

###POST domain/date
submit the start date/ end date in form

###GET domain/predict
test for pass local json to front end
