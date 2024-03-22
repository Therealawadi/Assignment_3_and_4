document.addEventListener("DOMContentLoaded", function () {
    // Select cursor elements
    const cursorDot = document.querySelector(".cursor-dot");
    const cursorOutline = document.querySelector(".cursor-outline");

    // Track mouse movement
    document.addEventListener("mousemove", (e) => {
        // Position cursor elements based on mouse coordinates
        cursorDot.style.top = e.pageY + "px";
        cursorDot.style.left = e.pageX + "px";
        cursorOutline.style.top = e.pageY + "px";
        cursorOutline.style.left = e.pageX + "px";
    });

    // Track hoverable elements (buttons and anchor tags)
    const hoverables = document.querySelectorAll("button, .info-btn, a");
    hoverables.forEach((element) => {
        // Change cursor style on hover or touch
        element.addEventListener("mouseenter", () => {
            expandCursorOutline();
        });
        element.addEventListener("mouseleave", () => {
            resetCursorOutline();
        });
        element.addEventListener("touchstart", () => {
            expandCursorOutline();
        });
        element.addEventListener("touchend", () => {
            resetCursorOutline();
        });
    });

    // Function to expand cursor outline
    function expandCursorOutline() {
        cursorOutline.style.width = "70px"; // Expanding cursor outline width
        cursorOutline.style.height = "70px"; // Expanding cursor outline height
    }

    // Function to reset cursor outline
    function resetCursorOutline() {
        cursorOutline.style.width = "50px"; // Reseting cursor outline width
        cursorOutline.style.height = "50px"; // Reseting cursor outline height
    }
});
