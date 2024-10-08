// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./CompetencySystem.sol";


contract CompetencySystemFactory {

    CompetencySystem[] public deployedContracts;

    // Evento que notifica la creación de una nueva instancia de contrato
    event ContractCreated(address newContractAddress);

    // Función para crear una nueva instancia de CompetencySystem
    function createCompetencySystem(string memory _name, uint24 _competencyId, uint8 _KEamount) public {
        CompetencySystem newContract = new CompetencySystem(_name, msg.sender, _competencyId, _KEamount);
        deployedContracts.push(newContract);
        emit ContractCreated(address(newContract));
    }

    // Función para obtener todas las instancias desplegadas
    function getDeployedContracts() public view returns (CompetencySystem[] memory) {
        return deployedContracts;
    }
}
