let customers = [];
const MYSERVER = "http://127.0.0.1:5000";
const load_customer = async () => {
  customers = await fetch(`${MYSERVER}/PrintAll/`)
    .then((response) => response.json())
    display.innerHTML = customers.map((cust, i) =>`
<div class="col">
<div class="card h-100">
<img src="https://picsum.photos/17${i}" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title"></h5>
<p class="card-text">Nane : ${cust.Name} </p>
City : ${cust.City}
</div>
<div class="card-footer">
<button class='btn btn-danger' onclick="delete_customer(${cust.CusomerID})">Delete</button>
</div>
</div>
</div>`
    )
    .join("");
};
load_customer();

const delete_customer = async (id) => {
  await fetch(`${MYSERVER}/deleteCustomer/${id}`, {methods: 'DELETE'})

}
load_customer()