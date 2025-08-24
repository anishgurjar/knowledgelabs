// simple example of a type system

type PaymentMethod = "cash" | "card" | "upi"

interface order{
    id: number | string,
    amount: number,
    paymentMethod: PaymentMethod,
    status: "pending" | "completed" | "cancelled"
}

const order: order = {
    id: 1,
    amount: 100,
    paymentMethod: "cash",
    status: "pending"
}

console.log(order)