

const MYSERVER = "http://127.0.0.1:5000";
const login = async () => {
  let lst_user = [];
  let lst_password = [];
  let user = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  login_user = await fetch(`${MYSERVER}/print_user/`).then((response) =>
    response.json()
  );
  login_user.map((item) =>lst_user.push(item.username));
  login_user.map((item) =>lst_password.push(item.password));
  for (let index = 0; index < lst_user.length; index++)
  for (let index = 0; index < lst_password.length; index++){
    if (lst_user[index] === user && lst_password[index] === password){
      return alert(`Welcome ${user}`)
    }
  }}
