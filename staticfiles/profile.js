document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('userProfileForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch(updateProfileUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                var successModal = new bootstrap.Modal(document.getElementById('successModal'));
                successModal.show();
            } else {
                var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
                errorModal.show();
            }
        });
    });

    // Filter form event listener
    document.getElementById('filter-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        var selectedYearRange = document.getElementById('selected_year_range').value;

        // Use AJAX to send a request to the server with the selected year range
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/filter_books/?year=' + selectedYearRange, true); // Replace with the actual URL
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Handle the AJAX response here
                var response = JSON.parse(xhr.responseText);
                updateBooks(response.books); // Implement a function to update the book elements
            }
        };
        xhr.send();
    });
});

function updateBooks(books) {
    // Clear the current book container
    var bookContainer = document.getElementById('book-container');
    while (bookContainer.firstChild) {
        bookContainer.removeChild(bookContainer.firstChild);
    }

    // Create and append book elements based on the filtered books data
    books.forEach(function(book) {
        // Create a new book card element
        var card = document.createElement('div');
        card.className = 'card';
        card.id = 'book-' + book.id;

        // Create the image element
        var img = document.createElement('img');
        img.className = 'card-img-top';
        img.alt = book.title;
        img.src = book.image_cover;
        card.appendChild(img);

        // Create the card body
        var cardBody = document.createElement('div');
        cardBody.className = 'card-body';
        card.appendChild(cardBody);

        // Create the card title
        var title = document.createElement('h5');
        title.className = 'card-title';
        title.textContent = book.title;
        cardBody.appendChild(title);

        // Create the list group
        var listGroup = document.createElement('ul');
        listGroup.className = 'list-group list-group-flush';
        card.appendChild(listGroup);

        // Create list items for author, publisher, and year
        ['Author', 'Publisher', 'Year'].forEach(function (label) {
            var listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = label + ': ' + book[label.toLowerCase()];
            listGroup.appendChild(listItem);
        });

        // Create the card body for the delete button
        var deleteCardBody = document.createElement('div');
        deleteCardBody.className = 'card-body';
        card.appendChild(deleteCardBody);

        // Create the delete button
        var deleteButton = document.createElement('a');
        deleteButton.className = 'btn btn-danger btn-sm';
        deleteButton.href = book.delete_url;  // You need to include a 'delete_url' in your JSON data
        deleteButton.innerHTML = '<i class="bi bi-journal-minus"></i>';
        deleteCardBody.appendChild(deleteButton);

        // Add the card to the book container
        var bookContainer = document.getElementById('book-container');
        bookContainer.appendChild(card);
    });
}