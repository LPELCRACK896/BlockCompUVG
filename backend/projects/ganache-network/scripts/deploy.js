const { Web3 } = require("web3");
const fs = require("fs");
const path = require("path");

const web3 = new Web3("http://127.0.0.1:8545");

const deploy = async () => {
  const accounts = await web3.eth.getAccounts();

  const contractPath = path.resolve(__dirname, "../build", "CompetencySystemFactory.json");
  const { abi, bytecode } = JSON.parse(fs.readFileSync(contractPath, "utf8"));

  const factoryContract = new web3.eth.Contract(abi);

  console.log("Desplegando el contrato desde la cuenta:", accounts[0]);

  const deployedContract = await factoryContract
    .deploy({ data: bytecode })
    .send({ from: accounts[0], gas: 1500000 });

  console.log("Contrato desplegado en:", deployedContract.options.address);
};

deploy().catch(error => {
  console.error("Error al desplegar el contrato:", error);
});
