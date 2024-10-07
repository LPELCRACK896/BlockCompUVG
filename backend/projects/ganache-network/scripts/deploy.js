const { Web3 } = require("web3");
const fs = require("fs");
const path = require("path");

const web3 = new Web3("http://127.0.0.1:8545");

const deploy = async () => {
  const accounts = await web3.eth.getAccounts();

  // Leer el ABI y bytecode del contrato compilado
  const contractPath = path.resolve(__dirname, "../build", "CompetencySystem.json");
  const { abi, bytecode } = JSON.parse(fs.readFileSync(contractPath, "utf8"));

  // Desplegar el contrato
  const contract = new web3.eth.Contract(abi);
  const contractInstance = await contract.deploy({ data: bytecode })
    .send({ from: accounts[0], gas: 1500000 });

  console.log("Contrato desplegado en:", contractInstance.options.address);
};

deploy();
