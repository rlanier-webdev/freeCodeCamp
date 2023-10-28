// set initial value
let count = 0;

// select value and buttons
const value = document.querySelector("#value")
const btns = document.querySelectorAll(".btn")

// Iterate over each button and add a click event listener
btns.forEach(function(btn) {
     btn.addEventListener('click', function(e) {
          // Get the classes of the clicked button
          const styles = e.currentTarget.classList;

          // Update the count based on the button's class
          count = styles.contains('decrease') ? count - 1 
               : styles.contains('increase') ? count + 1 
               : 0;
          // Change the text color based on the count value
          value.style.color = count > 0 ? "var(--clr-green-dark)"
               : count < 0 ? "var(--clr-red-dark)"
               : "var(--clr-white)";
          // Update the displayed count value
          value.textContent = count;
     });
});