let books = [];
const MYSERVER = "http://127.0.0.1:5000";


const load_books = async () => {
    books = await fetch(`${MYSERVER}/Book/`).then((response) => response.json())
    display.innerHTML = books.map((book, i) =>`
<div class="col">
<div class="card h-100">
<img src="https://picsum.photos/17${i}" class="card-img-top" alt="...">
<div class="card-body">
<h5 class="card-title"></h5>
<p class="card-text">Name book  : ${book.NameBook} </p>
Author : ${book.Author}
</div>
<div class="card-footer">
<button class='btn btn-danger' onclick="delete_book(${book.BookId})">Delete</button>
</div>
</div>
</div>`
    )
    .join("")
    
};



const delete_book = async (id) => {
    await fetch(`${MYSERVER}/deleteBook/${id}`,{method: 'DELETE'})
}

function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", cssFile);

    document.getElementsByTagName("head").item(cssLinkIndex).replaceChild(newlink, oldlink);
}

load_books()

