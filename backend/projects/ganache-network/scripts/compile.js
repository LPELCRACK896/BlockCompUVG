const path = require('path');
const fs = require('fs-extra');
const solc = require('solc');

// Ruta del contrato
const contractPath = path.resolve(__dirname, '../contracts', 'CompetencySystemFactory.sol');
const source = fs.readFileSync(contractPath, 'utf8');

// Compilar el contrato
const input = {
  language: 'Solidity',
  sources: {
    'CompetencySystemFactory.sol': {
      content: source
    }
  },
  settings: {
    outputSelection: {
      '*': {
        '*': ['abi', 'evm.bytecode']  // ABI y Bytecode
      }
    }
  }
};

const output = JSON.parse(solc.compile(JSON.stringify(input)));

// Escribir ABI y Bytecode en archivos
const buildPath = path.resolve(__dirname, '../build');
fs.ensureDirSync(buildPath);

const contract = output.contracts['CompetencySystemFactory.sol'].CompetencySystemFactory;
fs.outputJsonSync(path.resolve(buildPath, 'CompetencySystemFactory.json'), contract);

console.log('Contrato compilado con éxito. ABI y bytecode guardados en la carpeta build.');
