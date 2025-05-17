const mongoose = require("mongoose");

const EnergyDataSchema = new mongoose.Schema({
    userId: { 
        type: mongoose.Schema.Types.ObjectId, 
        ref: "User", 
        required: true 
    },
    date: { 
        type: Date, 
        required: true 
    },
    hourlyGeneration: { 
        type: [Number], 
        required: true 
    }, // Array of 24 values for hourly generation
    hourlyConsumption: { 
        type: [Number], 
        required: true 
    }, // Array of 24 values for hourly consumption
}, 
{ 
    timestamps: true 
});

module.exports = mongoose.model("EnergyData", EnergyDataSchema);