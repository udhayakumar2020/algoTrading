//INSTALLATION : use node version 14.17.0 and above

//npm install fyers-api-v2 --save (this will install particular 
//npm package into your system environment)

//Import the module in your Js by using the following command 
console.log("df")
const fyers   = require("fyers-api-v2")

access_token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc…CvMToekG_o2dGhZrClIo8BaTctqGT3C_gd3awPA7g'
refresh_token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJp…REo8smDszH3W2JUK1I53OSMa77z-agV6XlcAlTUl8'
fyers.setAppId('176EKUCLSL-100')
fyers.setRedirectUrl('https://trade.fyers.in/api-login/redirect-uri/index.html')
    
fyers.generateAuthCode()

// Response Structure:
// This will print a url on which by clicking you will get the authorization code.

// https://api.fyers.in/api/v2/generate-authcode?client_id=TXXXXXXXX4-101&redirect_uri=https://trade.fyers.in/api-login/redirect-uri/index.html&response_type=code&state=sample_state


/*auth_code : “This will be the response of the generateAuthCode method once you click on the redirect_url you will be provided with the auth_code”*/

const reqBody = {
    auth_code:'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzE3NjIxODQsImV4cCI6MTY3MTc5MjE4NCwibmJmIjoxNjcxNzYxNTg0LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYVTAwMDU3Iiwib21zIjpudWxsLCJub25jZSI6IiIsImFwcF9pZCI6IjE3NkVLVUNMU0wiLCJ1dWlkIjoiYThiYTk3MGZkNjgyNDE5ZjhkODYxYmFiOGUzYWY4ODQiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.pgWzDDOjwE3PdwBTJIYdY3_PDRtLd4wA1pv3u5ef60w',
        
    secret_key:'I9T6F7X8WQ'
    
}

fyers.generate_access_token(reqBody).then((response)=>{
    console.log(response)
})

// Copy
/*Copy the access token and paste it here. NOTE : Make sure for running 
any api 
fyers.setAccessToken and setAppId is set or it will throw error. */

fyers.setAccessToken('eyJ0eXAXXOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2MjM0MDM1NjgsImV4cCI6MTYyMzQ1NzgwOCwibmJmIjoxNjIzNDAzNTY4LCJhdWQiOlsieDoyIiwieDoxIiwieDowIiwiZDoxIiwiZDoyIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCZ3d5d3dwaEdHZlgzNVJ6MEpHTEhIVVlHY2w5SzJTdkd3RWtYS3p5NVIzZkxXLUtCSnkwVVdmTmFSVndDWlZrN2V5MlJYVDJPd0VITlZYYjAyN1huLWttSlUyTV9uN3NDY2NZTWhOS3pWUTNNWU9Tbz0iLCJkaXNwbGF5X25hbWUiOiJTQUlLQVQgREFTIiwiZnlfaWQiOiJYUzA1ODA1IiwiYXBwVHlwZSI6MTAxLCJwb2FfZmxhZyI6Ik4ifQ.Y57EeJqWcr1H6qODsKKrAWcqDfb8pTfjbOFRV3aLLPI')

fyers.get_profile().then((response) => {

    console.log(response)

})


/*Copy the access token and paste it here. NOTE : Make sure for running 
any api 
fyers.setAccessToken and setAppId is set or it will throw error. */

// fyers.setAccessToken('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc…ZVy9xxPX2yW6TegHKO4jSHTv3cIpuEPIl-0t1o92M')

// fyers.get_profile().then((response) => {

//     console.log(response)

// })
















// fyers.get_funds().then((response) => {
//     console.log(response)
// })
// fyers.setAccessToken('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzE3NTgyMTksImV4cCI6MTY3MTc4ODIxOSwibmJmIjoxNjcxNzU3NjE5LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYVTAwMDU3Iiwib21zIjpudWxsLCJub25jZSI6IiIsImFwcF9pZCI6IjE3NkVLVUNMU0wiLCJ1dWlkIjoiODM5OTc3MDcxZDhkNGViMjliMjNkMjU2MjAzOTc3MzEiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.xTYPuvniU0t2K31SywLCI0Zx2sjELxUNGD0ci358dgY')

// fyers.get_profile().then((response) => {

//     console.log(response)

// })
