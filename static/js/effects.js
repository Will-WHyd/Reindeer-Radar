document.addEventListener("DOMContentLoaded", () => {

    



    // --- Start of Enhanced Sparkle Effect Functionality ---

    /**
     * Function to create a sparkle at the given coordinates within the button
     * @param {HTMLElement} button - The button element where the sparkle will appear
     * @param {number} x - The x-coordinate relative to the button
     * @param {number} y - The y-coordinate relative to the button
     */
    function createSparkle(button, x, y) {
        const sparkle = document.createElement('div');
        sparkle.classList.add('sparkle');

        // Calculate a random angle for even distribution
        const angle = Math.random() * 2 * Math.PI; // 0 to 2π radians

        // Randomize movement distance between 20px and 70px
        const distance = Math.random() * 50 + 20; // 20px to 70px

        // Calculate movement based on angle and distance
        const moveX = Math.cos(angle) * distance;
        const moveY = Math.sin(angle) * distance;

        // Set CSS variables for movement in the animation
        sparkle.style.setProperty('--moveX', `${moveX}px`);
        sparkle.style.setProperty('--moveY', `${moveY}px`);

        // Position the sparkle at the click coordinates with slight randomness to spread
        const spreadX = (Math.random() - 0.5) * 10; // -5px to +5px
        const spreadY = (Math.random() - 0.5) * 10; // -5px to +5px

        sparkle.style.left = `${x + spreadX}px`;
        sparkle.style.top = `${y + spreadY}px`;

        // Append sparkle to the button
        button.appendChild(sparkle);

        console.log(`Sparkle created at (${x + spreadX}, ${y + spreadY}) with moveX: ${moveX}px, moveY: ${moveY}px`);

        // Remove the sparkle after the animation completes to clean up the DOM
        sparkle.addEventListener('animationend', () => {
            sparkle.remove();
            console.log('Sparkle removed');
        });
    }

    /**
     * Function to play the click sound
     */
    function playClickSound() {
        const clickSound = document.getElementById('clickSound');
        if (clickSound) {
            clickSound.currentTime = 0; // Reset to start
            clickSound.play().catch(error => {
                console.error("Error playing click sound:", error);
            });
        } else {
            console.warn("Click sound element not found.");
        }
    }

    // Add event listener to all buttons for the sparkle effect and sound
    document.querySelectorAll("button, a.btn, input[type='button'], input[type='submit']").forEach((btn) => {
        btn.addEventListener('click', function(event) {
            // Get the bounding rectangle of the button
            const rect = btn.getBoundingClientRect();
            // Calculate the click position relative to the button
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;

            console.log(`Button clicked at: (${x}, ${y})`);

            // Number of sparkles per click
            const sparkleCount = 5; // Number of sparkles

            for (let i = 0; i < sparkleCount; i++) {
                createSparkle(btn, x, y);
            }

            // Play the click sound
            playClickSound();
        });
    });

    // --- End of Enhanced Sparkle Effect Functionality ---

    // Existing Alert Closing Functionality

    
    //Toggle status buttons
    // Get all visited checkboxes
    const checkboxes = document.querySelectorAll(".visited-checkbox");

    // Update the counters
    const niceCountElement = document.getElementById("nice_counter");
    const naughtyCountElement = document.getElementById("naughty_counter");

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function () {
            const householdId = this.id.split("-")[0];
            const visitedStatus = this.checked;
            const spinner = document.getElementById(`${householdId}-spinner`);
            const label = document.querySelector(`label[for="${this.id}"]`);

            // Disable the checkbox to prevent further clicks during loading
            this.disabled = true;

            // Show the spinner
            spinner.style.display = "inline-block";

            fetch("/update-visited/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": "{{ csrf_token }}"
                },
                body: JSON.stringify({ household_id: householdId, visited: visitedStatus })
            })
                .then(response => response.json())
                .then(data => {
                    label.textContent = `Visited: ${visitedStatus}`;

                    // Dynamically update the Nice and Naughty counters
                    if (data.nice_count !== undefined && data.naughty_count !== undefined) {
                        niceCountElement.textContent = `Number of presents needed: ${data.nice_count}`;
                        naughtyCountElement.textContent = `Number of coals needed: ${data.naughty_count}`;
                    }
                })
                .catch(error => console.error("Error:", error))
                .finally(() => {
                    // Hide the spinner
                    spinner.style.display = "none";
                    this.disabled = false;
                });
        });
    });


});

setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);



