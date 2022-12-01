
const MYSERVER = "http://127.0.0.1:5000";
const add_user = async() =>{
    new_user = await fetch(`${MYSERVER}/registeruser/`,{
        method: 'POST',
        body: JSON.stringify({
            username: username.value,
            password: password.value,
            email: email.value
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    .then((response) => response.json())
    .then((json) => console.log(new_user));;

}