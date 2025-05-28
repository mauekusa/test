// Basic form submission handler to show confirmation without reloading
const form = document.getElementById('contact-form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const response = await fetch('/submit', {
        method: 'POST',
        body: new URLSearchParams(formData)
    });
    if (response.ok) {
        alert('送信しました。ありがとうございます！');
        form.reset();
    } else {
        alert('送信に失敗しました');
    }
});
