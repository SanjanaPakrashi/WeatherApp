// script.js

document.addEventListener('DOMContentLoaded', function () {
    const input = document.querySelector('input[name="city"]');
    const button = document.querySelector('button');
    const container = document.querySelector('.container');

    button.addEventListener('mouseenter', () => {
        button.style.transform = 'scale(1.1)';
        button.style.transition = 'transform 0.3s ease';
    });
    button.addEventListener('mouseleave', () => {
        button.style.transform = 'scale(1)';
    });

    input.addEventListener('focus', () => {
        container.style.boxShadow = '0 15px 30px rgba(137, 247, 254, 0.7)';
    });
    input.addEventListener('blur', () => {
        container.style.boxShadow = '0 10px 25px rgba(0,0,0,0.1)';
    });
});
