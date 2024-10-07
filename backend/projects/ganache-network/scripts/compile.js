const solc = require("solc");
const fs = require("fs");
const path = require("path");

// Ruta hacia el contrato
const contractPath = path.resolve(__dirname, "../contracts", "CompetencySystem.sol");
const source = fs.readFileSync(contractPath, "utf8");

const input = {
  language: "Solidity",
  sources: {
    "CompetencySystem.sol": { content: source },
  },
  settings: {
    outputSelection: {
      "*": {
        "*": ["abi", "evm.bytecode"],
      },
    },
  },
};

const output = JSON.parse(solc.compile(JSON.stringify(input)));
const abi = output.contracts["CompetencySystem.sol"].CompetencySystem.abi;
const bytecode = output.contracts["CompetencySystem.sol"].CompetencySystem.evm.bytecode.object;

// Guardar ABI y bytecode
const buildPath = path.resolve(__dirname, "../build");
if (!fs.existsSync(buildPath)) {
  fs.mkdirSync(buildPath);
}

fs.writeFileSync(path.resolve(buildPath, "CompetencySystem.json"), JSON.stringify({ abi, bytecode }));
console.log("Compilación completada y guardada en /build");
