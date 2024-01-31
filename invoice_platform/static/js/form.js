document.addEventListener('DOMContentLoaded', function () {
    function updateCardAccountTypes() {
        const cardTypeChoices = JSON.parse(document.getElementById('cardTypeChoices').textContent);
        const accountTypeChoices = JSON.parse(document.getElementById('accountTypeChoices').textContent);

        cardTypeField.innerHTML = "";
        accountTypeField.innerHTML = "";

        if (paymentType === "card") {
            for (const [value, label] of cardTypeChoices) {
                const option = document.createElement('option');
                option.value = value;
                option.text = label;
                cardTypeField.add(option);
            }
        } else if (paymentType === "account") {
            for (const [value, label] of accountTypeChoices) {
                const option = document.createElement('option');
                option.value = value;
                option.text = label;
                accountTypeField.add(option);
            }
        }
    }

    window.updateCardAccountTypes = updateCardAccountTypes;

    updateCardAccountTypes();

    // Обработка изменения значения в поле payment_type
    const paymentTypeField = document.getElementById('id_payment_type');
    paymentTypeField.addEventListener('change', updateCardAccountTypes);
});
