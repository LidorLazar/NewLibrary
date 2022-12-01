
const MYSERVER = "http://127.0.0.1:5000";
const add_customer = async() =>{
    new_customer = await fetch(`${MYSERVER}/addCustomer/` ,{
        method: 'POST',
        body: JSON.stringify({
            custID: custID.value,
            Name: Name.value,
            City: City.value,
            Age: Age.value,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    .then((response) => response.json())
    .then((json) => console.log(new_customer));;

load_customer()
}





