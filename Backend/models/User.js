const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    firstName: { 
        type: String, 
        required: true 
    },
    lastName: { 
        type: String, 
        required: false 
    },
    email: { 
        type: String, 
        required: true, 
        unique: true 
    },
    username: { 
        type: String, 
        required: true, 
        unique: true 
    },
    password: { 
        type: String, 
        required: true 
    },
    panelCount: {
        type: Number,
        default: 1,
    },
    pricePerUnit: {
        type: Number,
        default: 5
    },
    energyTokens: { 
        type: Number, 
        default: 0 
    }, // Balance of energy tokens
    discomRate: { 
        type: Number, 
        default: 0.1 
    }, // Rate for DISCOM fallback
}, 
{ 
    timestamps: true 
});


module.exports = mongoose.model("User", UserSchema);