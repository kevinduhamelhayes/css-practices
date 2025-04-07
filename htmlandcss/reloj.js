function updateClock() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    // Calcular los ángulos de rotación
    const secondDegrees = (seconds / 60) * 360;
    const minuteDegrees = ((minutes + seconds / 60) / 60) * 360;
    const hourDegrees = ((hours % 12 + minutes / 60) / 12) * 360;

    // Actualizar las manecillas
    document.querySelector('.second').style.transform = `rotate(${secondDegrees}deg)`;
    document.querySelector('.minute').style.transform = `rotate(${minuteDegrees}deg)`;
    document.querySelector('.hour').style.transform = `rotate(${hourDegrees}deg)`;
}

// Actualizar cada segundo
setInterval(updateClock, 1000);

// Actualizar inmediatamente al cargar
updateClock(); 