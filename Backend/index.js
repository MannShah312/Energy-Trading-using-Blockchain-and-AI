// Initialize Node.js Project
const express = require("express");
const mongoose = require("mongoose");
const passport = require("passport");
const JwtStrategy = require("passport-jwt").Strategy;
const ExtractJwt = require("passport-jwt").ExtractJwt;
require("dotenv").config();
const cors = require("cors");

// Import Routes
const AuthRoutes = require("./routes/auth");
const aiRoutes = require("./routes/ai");
const tradeRoutes = require("./routes/trade");

//kfB1fv4XZuhUvGM5
// Create Express App
const app = express();
const port = 4000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose
    .connect(
        "mongodb+srv://pdeuworkms:"
        + process.env.MONGO_PASSWORD + 
        "@cluster0.eezx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        }
    )
    .then(() => {
        console.log("✅ MongoDB connection established!");
    })
    .catch((err) => {
        console.error("❌ MongoDB connection error:", err.message);
    });

// Passport Configuration for JWT Authentication
let opts = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: process.env.JWT_SECRET,
};

passport.use(
    new JwtStrategy(opts, async (jwt_payload, done) => {
        try {
            const User = require("../Backend/models/User");
            const user = await User.findById(jwt_payload.id);
            if (user) return done(null, user);
            return done(null, false);
        } catch (err) {
            return done(err, false);
        }
    })
);

// Test Route
app.get("/", (req, res) => {
    res.send("Hello World! This is the backend for our website.");
});

// Routes
app.use("/auth", AuthRoutes);
app.use("/ai", aiRoutes);
app.use("/trade", tradeRoutes);

// Start Server
app.listen(port, () => {
    console.log(`🚀 Server running on http://localhost:${port}`);
});