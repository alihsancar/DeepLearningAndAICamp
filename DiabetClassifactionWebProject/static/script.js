document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const patientData = {
        Gender: parseFloat(document.getElementById('Gender').value),
        AGE: parseFloat(document.getElementById('AGE').value),
        Urea: parseFloat(document.getElementById('Urea').value),
        Cr: parseFloat(document.getElementById('Cr').value),
        HbA1c: parseFloat(document.getElementById('HbA1c').value),
        Chol: parseFloat(document.getElementById('Chol').value),
        TG: parseFloat(document.getElementById('TG').value),
        HDL: parseFloat(document.getElementById('HDL').value),
        LDL: parseFloat(document.getElementById('LDL').value),
        VLDL: parseFloat(document.getElementById('VLDL').value),
        BMI: parseFloat(document.getElementById('BMI').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData)
        });

        if (response.ok) {
            const result = await response.json();

            const resultBox = document.getElementById('resultBox');
            const resultText = document.getElementById('resultText');

            resultText.innerText = result.result_text;
            resultBox.classList.remove('hidden');

            // Modern Neon Renkler
            if(result.class_id === 0) {
                resultText.style.color = "#4ade80"; // Neon Yeşil
                resultBox.style.borderColor = "rgba(74, 222, 128, 0.3)";
            }
            if(result.class_id === 1) {
                resultText.style.color = "#f87171"; // Neon Kırmızı
                resultBox.style.borderColor = "rgba(248, 113, 113, 0.3)";
            }
            if(result.class_id === 2) {
                resultText.style.color = "#fbbf24"; // Neon Sarı/Turuncu
                resultBox.style.borderColor = "rgba(251, 191, 36, 0.3)";
            }

        } else {
            alert('Tahmin alınırken sunucu hatası oluştu!');
        }
    } catch (error) {
        console.error('Hata:', error);
        alert('Sunucuya bağlanılamadı. API açık mı?');
    }
});