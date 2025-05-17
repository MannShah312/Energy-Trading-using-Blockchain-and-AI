// const express = require("express");
// const passport = require("passport");
// const router = express.Router();
// const User = require("../models/User");
// const bcrypt = require("bcrypt");
// const {getToken} = require("../utils/helpers");
// const Trade = require("../models/Trade");

// router.post(
//     "/bid",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         const currentUser = req.user; // Authenticated user
//         const { pricePerUnit, energyAmount } = req.body;

//         // Validate request body
//         if (!pricePerUnit || !energyAmount) {
//             return res.status(400).json({ error: "Price per unit and energy amount are required." });
//         }

//         try {
//             // Prepare bid data
//             const bidData = {
//                 tradeId: `bid-${Date.now()}`,
//                 type: "bid",
//                 userId: currentUser._id,
//                 pricePerUnit,
//                 energyAmount,
//                 status: "active",
//             };

//             // Create bid entry in the database
//             const bid = await Trade.create(bidData);

//             return res.status(201).json({
//                 message: "Bid placed successfully.",
//                 bid,
//             });
//         } catch (error) {
//             console.error("Error placing bid:", error);
//             return res.status(500).json({ error: "Internal server error." });
//         }
//     }
// );

// router.post(
//     "/ask",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         const currentUser = req.user; // Authenticated user
//         const { pricePerUnit, energyAmount } = req.body;

//         if (!pricePerUnit || !energyAmount) {
//             return res.status(400).json({ err: "Insufficient data" });
//         }

//         try {
//             const askData = {
//                 tradeId: `ask-${Date.now()}`,
//                 type: "ask",
//                 userId: currentUser._id,
//                 pricePerUnit,
//                 energyAmount,
//                 status: "active",
//             };

//             const ask = await Trade.create(askData);
//             return res.status(201).json(ask);
//         } catch (error) {
//             console.error(error);
//             return res.status(500).json({ err: "Error placing ask" });
//         }
//     }
// );

// router.get(
//     "/active",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         try {
//             const activeTrades = await Trade.find({ status: "active" });
//             return res.status(200).json(activeTrades);
//         } catch (error) {
//             console.error(error);
//             return res.status(500).json({ err: "Error fetching active trades" });
//         }
//     }
// );

// router.get(
//     "/my",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         const currentUser = req.user; // Authenticated user

//         try {
//             const userTrades = await Trade.find({ userId: currentUser._id });
//             return res.status(200).json(userTrades);
//         } catch (error) {
//             console.error(error);
//             return res.status(500).json({ err: "Error fetching user trades" });
//         }
//     }
// );



// router.patch(
//     "/cancel/:id",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         const currentUser = req.user; // Authenticated user
//         const tradeId = req.params.id;

//         try {
//             const trade = await Trade.findOne({ tradeId });

//             if (!trade) {
//                 return res.status(404).json({ err: "Trade not found" });
//             }

//             if (trade.userId.toString() !== currentUser._id.toString()) {
//                 return res.status(403).json({ err: "Unauthorized action" });
//             }

//             trade.status = "cancelled";
//             await trade.save();

//             return res.status(200).json({ message: "Trade cancelled successfully", trade });
//         } catch (error) {
//             console.error(error);
//             return res.status(500).json({ err: "Error cancelling trade" });
//         }
//     }
// );


// router.post(
//     "/match",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         try {
//             const activeBids = await Trade.find({ type: "bid", status: "active" });
//             const activeAsks = await Trade.find({ type: "ask", status: "active" });

//             for (const bid of activeBids) {
//                 for (const ask of activeAsks) {
//                     if (bid.pricePerUnit >= ask.pricePerUnit && bid.status === "active" && ask.status === "active") {
//                         const tradedAmount = Math.min(bid.energyAmount, ask.energyAmount);

//                         bid.energyAmount -= tradedAmount;
//                         ask.energyAmount -= tradedAmount;

//                         if (bid.energyAmount === 0) bid.status = "completed";
//                         if (ask.energyAmount === 0) ask.status = "completed";

//                         bid.matchedTradeId = ask.tradeId;
//                         ask.matchedTradeId = bid.tradeId;

//                         await bid.save();
//                         await ask.save();

//                         console.log(`Matched ${tradedAmount} kWh between ${bid.userId} and ${ask.userId}`);
//                     }
//                 }
//             }

//             return res.status(200).json({ message: "Order matching completed" });
//         } catch (error) {
//             console.error(error);
//             return res.status(500).json({ err: "Error during order matching" });
//         }
//     }
// );

// module.exports = router;


// const express = require("express");
// const passport = require("passport");
// const router = express.Router();
// const { ethers } = require("ethers");
// require('dotenv').config({path: "./blockchain/.env"});
// const { energyTokenABI, energyTradingABI, lockContractABI } = require("../blockchain/ABI/abi");

// // Fetch the private key and network RPC URL from environment variables
// const privateKey = process.env.PRIVATE_KEY;
// const networkUrl = process.env.NETWORK_RPC_URL;

// console.log("Private Key:", privateKey);
// if (!privateKey) {
//     console.error("Private key is missing!");
// }

// // Connect to Ethereum network
// const provider = new ethers.providers.JsonRpcProvider(networkUrl);
// const wallet = new ethers.Wallet(privateKey, provider);

// // Example: Connect to the EnergyToken contract
// const energyTokenAddress = process.env.ENERGY_TOKEN_CONTRACT_ADDRESS;
// const energyTokenContract = new ethers.Contract(energyTokenAddress, energyTokenABI, wallet);

// // Example: Connect to the EnergyTrading contract
// const energyTradingAddress = process.env.ENERGY_TRADING_CONTRACT_ADDRESS;
// const energyTradingContract = new ethers.Contract(energyTradingAddress, energyTradingABI, wallet);

// // Example: Connect to the Lock contract
// const lockContractAddress = process.env.LOCK_CONTRACT_ADDRESS;
// const lockContract = new ethers.Contract(lockContractAddress, lockContractABI, wallet);

// // Bid API
// router.post(
//     "/bid",
//     passport.authenticate("jwt", { session: false }),
//     async (req, res) => {
//         const currentUser = req.user;
//         const { pricePerUnit, energyAmount } = req.body;

//         // Validate request body
//         if (!pricePerUnit || !energyAmount) {
//             return res.status(400).json({ error: "Price per unit and energy amount are required." });
//         }

//         try {
//             // Prepare bid data
//             const bidData = {
//                 tradeId: `bid-${Date.now()}`,
//                 type: "bid",
//                 userId: currentUser._id,
//                 pricePerUnit,
//                 energyAmount,
//                 status: "active",
//             };

//             // Create bid entry in the database
//             const bid = await Trade.create(bidData);

//             // Call contract function to place a bid (for example, buying energy)
//             const transaction = await energyTradingContract.placeBid(pricePerUnit, energyAmount, {
//                 from: wallet.address,
//             });

//             return res.status(201).json({
//                 message: "Bid placed successfully.",
//                 bid,
//                 transactionHash: transaction.hash,
//             });
//         } catch (error) {
//             console.error("Error placing bid:", error);
//             return res.status(500).json({ error: "Internal server error." });
//         }
//     }
// );

// // Ask, Active, My Trades, etc., would follow the same pattern of contract interaction when necessary

// module.exports = router;

const express = require("express");
const passport = require("passport");
const { ethers } = require("ethers");
const router = express.Router();
const Trade = require("../models/Trade");
const User = require("../models/User");
require("dotenv").config({ path: "./blockchain/.env" });

// Load contract ABIs
const { energyTokenABI, energyTradingABI }  = require("../blockchain/ABI/abi");

// Fetch private key, network URL, and contract addresses from .env
const privateKey = process.env.PRIVATE_KEY;
const networkUrl = process.env.NETWORK_RPC_URL;
const energyTokenAddress = process.env.ENERGY_TOKEN_CONTRACT_ADDRESS;
const energyTradingAddress = process.env.ENERGY_TRADING_CONTRACT_ADDRESS;

// Ethereum provider and wallet setup
const provider = new ethers.providers.JsonRpcProvider(networkUrl);
const wallet = new ethers.Wallet(privateKey, provider);
const energyTokenContract = new ethers.Contract(energyTokenAddress, energyTokenABI, wallet);
const energyTradingContract = new ethers.Contract(energyTradingAddress, energyTradingABI, wallet);

// Middleware for JWT authentication
const authenticateJWT = passport.authenticate("jwt", { session: false });

// Place Bid
router.post("/bid", authenticateJWT, async (req, res) => {
    const { pricePerUnit, energyAmount, sellerId } = req.body;

    if (!pricePerUnit || !energyAmount || !sellerId) {
        return res.status(400).json({ error: "Price per unit, energy amount, and sellerId are required." });
    }

    try {
        const bidData = {
            tradeId: `bid-${Date.now()}`,
            type: "bid",
            pricePerUnit,
            energyAmount,
            sellerId,
            status: "active",  // Set the status to 'active'
        };

        const bid = await Trade.create(bidData);
        return res.status(201).json({
            message: "Bid placed successfully.",
            bid,
        });
    } catch (error) {
        console.error("Error placing bid:", error);
        return res.status(500).json({ error: "Internal server error." });
    }
});

// Place Ask
router.post("/ask", authenticateJWT, async (req, res) => {
    const { pricePerUnit, energyAmount, sellerId } = req.body;

    if (!pricePerUnit || !energyAmount || !sellerId) {
        return res.status(400).json({ err: "Price per unit, energy amount, and sellerId are required." });
    }

    try {
        const askData = {
            tradeId: `ask-${Date.now()}`,
            type: "ask",
            pricePerUnit,
            energyAmount,
            sellerId,
            status: "active",  // Set the status to 'active'
        };

        const ask = await Trade.create(askData);
        return res.status(201).json({
            message: "Ask placed successfully.",
            ask,
        });
    } catch (error) {
        console.error("Error placing ask:", error);
        return res.status(500).json({ err: "Internal server error." });
    }
});

// Get All Trades
router.get("/trades", authenticateJWT, async (req, res) => {
    try {
        const trades = await Trade.find({ status: { $in: ["active", "completed"] } });
        res.status(200).json({ trades });
    } catch (error) {
        console.error("Error fetching trades:", error);
        res.status(500).json({ error: "Failed to fetch trades" });
    }
});

// Update Trade Status
router.put("/trade/:id", authenticateJWT, async (req, res) => {
    const tradeId = req.params.id;
    const { status } = req.body;  // e.g., 'completed' or 'cancelled'

    if (!status || !["completed", "cancelled"].includes(status)) {
        return res.status(400).json({ error: "Invalid status value. Must be 'completed' or 'cancelled'." });
    }

    try {
        const trade = await Trade.findById(tradeId);

        if (!trade) {
            return res.status(404).json({ error: "Trade not found." });
        }

        // Check if the user is the seller of the trade
        if (trade.sellerId !== req.user.id) {
            return res.status(403).json({ error: "You are not authorized to update this trade." });
        }

        // Update trade status
        trade.status = status;
        await trade.save();

        res.status(200).json({ message: `Trade status updated to ${status}.`, trade });
    } catch (error) {
        console.error("Error updating trade:", error);
        res.status(500).json({ error: "Failed to update trade status." });
    }
});

// Cancel Trade
router.delete("/trade/:id", async (req, res) => {
    const tradeId = req.params.id;

    try {
        const trade = await Trade.findById(tradeId);

        if (!trade) {
            return res.status(404).json({ error: "Trade not found." });
        }

        // Check if the user is the seller of the trade
        if (trade.sellerId !== req.user.id) {
            return res.status(403).json({ error: "You are not authorized to cancel this trade." });
        }

        // Cancel the trade
        trade.status = "cancelled";
        await trade.save();

        res.status(200).json({ message: "Trade has been cancelled.", trade });
    } catch (error) {
        console.error("Error cancelling trade:", error);
        res.status(500).json({ error: "Failed to cancel trade." });
    }
});
module.exports = router;