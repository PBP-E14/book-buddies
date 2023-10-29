async function getWishlists() {
    return fetch(`get_wishlist/`).then((res) =>
        res.json()
    );
}

async function refreshWishlists() {
    document.getElementById("wishlist").innerHTML = "";
    const { wishlists, books } = await getWishlists();
    const readBooks = await getReadBook();
    let dateAdded = []; // Initialize the variable to store the date_added
    let wishlistPk = [];
    let i = 0;
    for (const item of JSON.parse(wishlists)) {
        dateAdded[i] = item.fields.date_added;
        wishlistPk[i] = item.pk;
        i++;
    }

    let htmlString = `
`;

    JSON.parse(books).forEach((book, idx) => {
        htmlString += `
        <div class="col-md-4 mb-4">
            <div class="card-container"> <!-- Wrap the cards in a container -->
                ${
                    readBooks.includes(book.pk)
                        ? `<div class="card light-green">`
                        : `<div class="card light-red">`
                }
            
            <img
                src="${book.fields.image_cover}"
                class="card-img-top"
                style="height: 18rem; object-fit: cover"
                alt="${book.fields.title} image"
            />
                <div class="card-body">
                    <h5 class="card-title">${book.fields.title}</h5>
                    ${
                        readBooks.includes(book.pk)
                            ? `<h6 class="m-0">Status: Read</p>`
                            : `<h6 class="m-0">Status: Not Read Yet</p>`
                    }
                    <p class="m-0">by: ${book.fields.author}</p>
                    <p class="m-0">publisher: ${book.fields.publisher}</p>
                    <p class="m-0">year: ${book.fields.year_publication}</p>
                    <br>
                    <a>
                        <button type="submit" class="btn btn-outline-danger btn-sm edit-item-btn" onclick="removeWishlist(${wishlistPk[idx]})">Remove</button>
                    </a>
                </div>
                <div class="card-footer text-muted">
                    Created: ${dateAdded[idx]}
                </div>
            </div>
        </div>
    </div>
`;
    });

    document.getElementById("wishlist").innerHTML = htmlString;
}

refreshWishlists();

async function removeWishlist(id) {
    await fetch(`/wishlist/remove_wishlist/${id}/`, {
        method: "DELETE",
    }).then(refreshWishlists);
}

async function getReadBook() {
    const result = await fetch(`/book/get-read-book/`).then(
        (res) => res.json()
    );

    const readBooksPk = [];
    for (const item of result) {
        readBooksPk.push(item.pk);
    }

    return readBooksPk;
}