document.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:5001/api/v1/orders")
        .then(res => res.json())
        .then(meds => {
            const container = document.getElementById("medication-list");
            meds.forEach(med => {
                const medBox = document.createElement("div");
                medBox.className = "order-item";
                medBox.innerHTML = `
                    <h3>${med.name}</h3>
                    <p><strong>Dosage:</strong> ${med.dosage}</p>
                    <p><strong>Price:</strong> $${med.price}</p>
                    <p><strong>Stock:</strong> ${med.stock}</p>
                    <input type="number" id="qty-${med.id}" min="1" max="${med.stock}" value="1">
                    <button onclick="placeOrder('${med.id}', ${med.price})">Order</button>
                    <hr/>
                `;
                container.appendChild(medBox);
            });
        });
});

function placeOrder(medId, price) {
    const qty = parseInt(document.getElementById(`qty-${medId}`).value);
    const userId = "822daf6a-3915-4068-9e41-9e34d68a6366"; // replace with real logic later
    fetch("http://127.0.0.1:5001/api/v1/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user_id: userId,
            medication_id: medId,
            quantity: qty
        })
    })
    .then(res => res.json())
    .then(order => {
        alert(`Order placed!\nTotal: $${order.total_price}\nStatus: ${order.status}`);
    })
    .catch(err => {
        console.error("Order failed", err);
        alert("An error occurred. Please try again.");
    });
}
