const mongoose = require("mongoose");

const BillSchema = new mongoose.Schema({
    userId: { 
        type: mongoose.Schema.Types.ObjectId, 
        ref: "User", 
        required: true 
    },
    startDate: { 
        type: Date, 
        required: true 
    },
    endDate: { 
        type: Date, 
        required: true 
    },
    totalConsumption: { 
        type: Number, 
        required: true 
    }, // Total energy consumed
    totalGeneration: { 
        type: Number, 
        required: true 
    }, // Total energy generated
    tokensEarned: { 
        type: Number, 
        required: true 
    }, // Energy tokens earned
    tokensSpent: { 
        type: Number, 
        required: true 
    }, // Energy tokens spent
    amountDue: { 
        type: Number, 
        required: true 
    }, // Amount owed to DISCOM or other users
}, 
{ 
    timestamps: true 

});
module.exports = mongoose.model("Bill", BillSchema);