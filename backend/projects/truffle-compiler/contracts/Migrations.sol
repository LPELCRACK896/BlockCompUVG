// SPDX-License-Identifier: MIT
/*
Original
- @author Paul De Jesús Belches Flores-Gómez (paulbelches)
- @author David Uriel Soto Alvarez
Original project: https://github.com/LPELCRACK896/CompetencySystemApi.git
*/

pragma solidity >=0.4.22 <0.9.0;

contract Migrations {
  address public owner = msg.sender;
  uint public last_completed_migration;

  modifier restricted() {
    require(
      msg.sender == owner,
      "This function is restricted to the contract's owner"
    );
    _;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }
}
