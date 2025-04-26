document.addEventListener('DOMContentLoaded', function() {
    // Add new entry button click handler
    const addEntryBtn = document.querySelector('.add-entry');
    const entryModal = document.getElementById('entryModal');
    const closeModal = document.querySelector('.close');
    const entryForm = document.getElementById('entryForm');
    const entriesContainer = document.getElementById('entries-container');

    // Load entries when page loads
    loadEntries();

    addEntryBtn.onclick = function() {
        entryModal.style.display = "block";
    }

    closeModal.onclick = function() {
        entryModal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == entryModal) {
            entryModal.style.display = "none";
        }
    }

    entryForm.onsubmit = function(e) {
        e.preventDefault();
        
        const formData = new FormData(entryForm);
        
        fetch('/add_journal_entry/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Clear the form
                entryForm.reset();
                // Close the modal
                entryModal.style.display = "none";
                // Reload entries to show the new one
                loadEntries();
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while saving the entry.');
        });
    }

    // Function to load entries
    function loadEntries() {
        fetch('/get_journal_entries/')
            .then(response => response.json())
            .then(data => {
                entriesContainer.innerHTML = ''; // Clear existing entries
                if (data.entries && data.entries.length > 0) {
                    data.entries.forEach(entry => {
                        const entryDiv = document.createElement('div');
                        entryDiv.className = 'entry';
                        entryDiv.innerHTML = `
                            <span class="star">&#9733; ${entry.date}</span>
                            <div class="title-text">${entry.content}</div>
                            <button class="delete-btn" data-id="${entry.id}">&times;</button>
                        `;
                        entriesContainer.appendChild(entryDiv);
                    });

                    // Add delete event listeners
                    document.querySelectorAll('.delete-btn').forEach(button => {
                        button.addEventListener('click', function() {
                            const entryId = this.getAttribute('data-id');
                            if (confirm('Are you sure you want to delete this entry?')) {
                                deleteEntry(entryId);
                            }
                        });
                    });
                } else {
                    entriesContainer.innerHTML = '<p class="no-entries">No entries yet. Start by adding your first entry!</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while loading entries.');
            });
    }

    // Function to delete an entry
    function deleteEntry(entryId) {
        fetch(`/delete_journal_entry/${entryId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                loadEntries(); // Reload entries after deletion
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while deleting the entry.');
        });
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}); 