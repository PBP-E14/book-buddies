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

    // Function to show a message in a Bootstrap modal
    function showMessageModal(message, autoCloseDelay) {
        var messageModal = new bootstrap.Modal(document.getElementById('messageModal'));
        var messageContent = document.getElementById('messageContent');
        messageContent.textContent = message;
        messageModal.show();

        // Close the modal automatically after the specified delay (in milliseconds)
        if (autoCloseDelay) {
            setTimeout(function() {
                messageModal.hide(); // Close the modal
            }, autoCloseDelay);
        }
    }

    // Function to update books on the page
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
                if (label.toLowerCase() === 'year') {
                    var listItem = document.createElement('li');
                    listItem.className = 'list-group-item';
                    listItem.textContent = label + ': ' + book.year;
                    listGroup.appendChild(listItem);
                } else {
                    var listItem = document.createElement('li');
                    listItem.className = 'list-group-item';
                    listItem.textContent = label + ': ' + book[label.toLowerCase()];
                    listGroup.appendChild(listItem);
                }
            });

            // Add the card to the book container
            bookContainer.appendChild(card);
        });
    }

    // Attach an event listener to the filter form
    const filterForm = document.getElementById('filter-form');
    filterForm.addEventListener('submit', function(event) {
        event.preventDefault();
        filterBooks();
    });

    // Function to filter books
    function filterBooks() {
        const selectedYearRange = document.getElementById('selected_year_range').value;
        fetchBooks(selectedYearRange);
    }

    // Function to fetch books via AJAX
    function fetchBooks(yearRange) {
        fetch(filterUrl + '?selected_year_range=' + yearRange)
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    // Show the message in a modal
                    showMessageModal(data.message, 2500);
                }
                // Update books as usual, even if there's a message
                updateBooks(data.books);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }


    // Function to update books on the page
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
                if (label.toLowerCase() === 'year') {
                    var listItem = document.createElement('li');
                    listItem.className = 'list-group-item';
                    listItem.textContent = label + ': ' + book.year; 
                    listGroup.appendChild(listItem);
                } else {
                    var listItem = document.createElement('li');
                    listItem.className = 'list-group-item';
                    listItem.textContent = label + ': ' + book[label.toLowerCase()];
                    listGroup.appendChild(listItem);
                }
            });
    
            // Add the card to the book container
            bookContainer.appendChild(card);
        });
    }   

});


