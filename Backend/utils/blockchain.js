const { ethers } = require("ethers");
const energyTokenABI = require("../../blockchain/artifacts/contracts/EnergyToken.sol/EnergyToken.json").abi;

const provider = new ethers.JsonRpcProvider(process.env.LOCALHOST_RPC_URL);
const signer = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

const energyTokenContract = new ethers.Contract("contract_address", energyTokenABI, signer);

async function getBalance(address) {
    return await energyTokenContract.balanceOf(address);
}

async function transferTokens(to, amount) {
    return await energyTokenContract.transfer(to, ethers.utils.parseEther(amount.toString()));
}
module.exports = { getBalance, transferTokens };