const mongoose = require("mongoose");

const ForecastSchema = new mongoose.Schema({
    userId: { 
        type: mongoose.Schema.Types.ObjectId, 
        ref: "User", 
        required: true 
    },
    date: { 
        type: Date, 
        required: true 
        
    },
    hourlyForecast: { 
        type: [Number], 
        required: true 
    }, // Array of 24 values for hourly predictions
}, 
{ 
    timestamps: true 
});


module.exports = mongoose.model("Forecast", ForecastSchema);    