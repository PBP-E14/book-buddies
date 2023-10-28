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
});