const Web3 = require("web3");
const fs = require("fs");
const path = require("path");

const web3 = new Web3("http://127.0.0.1:8545");

const interact = async () => {
  const accounts = await web3.eth.getAccounts();

  // Cargar el ABI del contrato desplegado
  const contractPath = path.resolve(__dirname, "../build", "CompetencySystem.json");
  const { abi } = JSON.parse(fs.readFileSync(contractPath, "utf8"));

  const contractAddress = "DIRECCION_DEL_CONTRATO_DESPLEGADO"; // Dirección del contrato
  const contract = new web3.eth.Contract(abi, contractAddress);

  // Llamar a una función del contrato
  const result = await contract.methods.someFunction().call({ from: accounts[0] });
  console.log("Resultado de la función:", result);
};

interact();
