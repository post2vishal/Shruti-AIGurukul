// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ShrutiGKT {
    string public name = "Shruti AI GKT";
    string public symbol = "SGKT";
    uint256 public totalSupply = 1_000_000_000 * 10**18;
    address public xAIAdmin;
    mapping(address => uint256) public balanceOf;

    event Mint(address indexed to, uint256 value, string reason);

    constructor() {
        xAIAdmin = msg.sender;
        balanceOf[xAIAdmin] = totalSupply;
    }

    function mintForRecitation(address user, uint256 amount, string memory fact) public {
        require(msg.sender == xAIAdmin, "Only xAI");
        balanceOf[user] += amount;
        emit Mint(user, amount, fact);
    }
}
