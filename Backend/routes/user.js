const express = require("express");
const router = express.Router();
const User = require("../models/User");
const bcrypt = require("bcrypt");
const {getToken} = require("../utils/helpers");

router.get(
    "/profile",
    passport.authenticate("jwt", { session: false }),
    async (req, res) => {
        try {
            const user = await User.findById(req.user._id).select("-password"); // Exclude password
            if (!user) {
                return res.status(404).json({ err: "User not found" });
            }
            return res.status(200).json(user);
        } catch (error) {
            console.error(error);
            return res.status(500).json({ err: "Error fetching user profile" });
        }
    }
);