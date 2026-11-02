// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CustomerBank {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Deposit ETH into the contract
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be greater than zero");
    }

    // Withdraw ETH from the contract
    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "Only account owner can withdraw");
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");

        payable(owner).transfer(amount);
    }

    // Show the contract's balance in wei
    function showBalance() public view returns (uint256) {
        return address(this).balance;
    }
}