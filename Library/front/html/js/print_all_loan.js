let loans = [];
const MYSERVER = "http://127.0.0.1:5000";
const load_loans = async () => {
    loans = await fetch(`${MYSERVER}/AddLoan/`)
    .then((response) => response.json())
    display.innerHTML = loans.map((loan, i) =>`
<div class="col">
<div class="card h-100">
<img src="https://picsum.photos/17${i}" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title"></h5>
<p class="card-text">Nane : ${loan.LoansID} </p>
City : ${loan.customers.Name}
</div>
<div class="card-footer">
<button class='btn btn-danger' onclick="delete_customer(${loan.LoansID})">Delete</button>
</div>
</div>
</div>`
    )
    .join("");
};
load_loans();

