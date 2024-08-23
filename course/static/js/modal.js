document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("lesson-modal");
    const btn = document.getElementById("create-lesson-btn");
    const span = document.querySelector(".close");

    const openModal = () => {
        modal.style.display = "block";
    };

    const closeModal = () => {
        modal.style.display = "none";
    };

    btn.addEventListener('click', openModal);

    span.addEventListener('click', closeModal);
    
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });
});
