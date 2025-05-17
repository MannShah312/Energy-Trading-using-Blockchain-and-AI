const mongoose = require("mongoose");

const tradeSchema = new mongoose.Schema({
    tradeId: { type: String, required: true },
    type: { type: String, enum: ["bid", "ask"], required: true },
    pricePerUnit: { type: Number, required: true },
    energyAmount: { type: Number, required: true },
    sellerId: { type: String, required: true },
    status: {
        type: String,
        enum: ["active", "completed", "cancelled"],
        default: "active",
        required: true
    },
    matchedTradeId: { type: String },
});

const Trade = mongoose.model("Trade", tradeSchema);

module.exports = Trade;