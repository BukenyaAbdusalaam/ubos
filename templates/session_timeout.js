// session_timeout.js

function resetSessionTimeout() {
    // Send an AJAX request to the server to reset the session timeout
    // You can use any method to trigger a server request, such as Fetch API or jQuery.ajax
    // Example using jQuery:
    $.ajax({
        type: 'POST',
        url: '/reset_session_timeout/',  // Replace with your server endpoint
        data: {},
        success: function (data) {
            console.log('Session timeout reset successfully.');
        },
        error: function (error) {
            console.error('Error resetting session timeout:', error);
        }
    });
}

// Monitor user activity (e.g., mousemove and keydown events)
document.addEventListener('mousemove', resetSessionTimeout);
document.addEventListener('keydown', resetSessionTimeout);
