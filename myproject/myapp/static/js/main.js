// Dynamic UI interactions and animations
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Event registration countdown
    const countdowns = document.querySelectorAll('.event-countdown');
    countdowns.forEach(countdown => {
        const eventDate = new Date(countdown.dataset.date);
        
        const timer = setInterval(() => {
            const now = new Date();
            const distance = eventDate - now;
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            
            countdown.innerHTML = `${days}d ${hours}h ${minutes}m`;
            
            if (distance < 0) {
                clearInterval(timer);
                countdown.innerHTML = "Event Started";
            }
        }, 1000);
    });

    // Dynamic form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    
                    const errorMessage = document.createElement('div');
                    errorMessage.className = 'error-message';
                    errorMessage.textContent = 'This field is required';
                    
                    if (!field.nextElementSibling?.classList.contains('error-message')) {
                        field.parentNode.insertBefore(errorMessage, field.nextSibling);
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // Real-time event capacity updates
    const eventCapacity = document.querySelectorAll('.event-capacity');
    eventCapacity.forEach(capacity => {
        const eventId = capacity.dataset.eventId;
        
        setInterval(() => {
            fetch(`/api/event-capacity/${eventId}`)
                .then(response => response.json())
                .then(data => {
                    capacity.textContent = `${data.current}/${data.max} spots filled`;
                    
                    if (data.current >= data.max) {
                        const registerBtn = document.querySelector(`#register-${eventId}`);
                        if (registerBtn) {
                            registerBtn.disabled = true;
                            registerBtn.textContent = 'Event Full';
                        }
                    }
                });
        }, 30000); // Update every 30 seconds
    });

    // Interactive leaderboard
    const leaderboard = document.querySelector('.leaderboard');
    if (leaderboard) {
        const items = leaderboard.querySelectorAll('.leaderboard-item');
        
        items.forEach((item, index) => {
            item.style.animationDelay = `${index * 0.1}s`;
            item.classList.add('animate-fade-in');
        });
    }
});