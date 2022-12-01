const MYSERVER = "http://127.0.0.1:5000";

const add_book = async () =>{
    new_book = await fetch(`${MYSERVER}/addBook/`,{
        method: 'POST',
        body: JSON.stringify({
            NameBook: NameBook.value,
            Author: Author.value,
            YearPublished: YearPublished.value,
            Type: Type.value,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    .then((response) => response.json())
    .then((json) => console.log(new_customer));;
    load_books();
}

