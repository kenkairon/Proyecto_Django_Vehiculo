setTimeout(() => {
    const messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        messageContainer.style.transition = "opacity 0.3s"; // Transición rápida (300ms)
        messageContainer.style.opacity = 0; // Efecto de desvanecimiento
        setTimeout(() => messageContainer.remove(), 300); // Remover el contenedor después del desvanecimiento
    }
}, 2000); // Mostrar mensaje solo durante 2 segundos antes de desvanecerlo
