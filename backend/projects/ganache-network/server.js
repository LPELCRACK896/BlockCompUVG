const ganache = require("ganache");
const fs = require("fs");
const path = require("path");

const dbPath = path.resolve(__dirname, './ganache-db');

if (!fs.existsSync(dbPath)) {
  fs.mkdirSync(dbPath, { recursive: true });
  console.log(`Carpeta de base de datos creada en: ${dbPath}`);
} else {
  console.log(`Carpeta de base de datos ya existe en: ${dbPath}`);
}

const options = {
  wallet: {
    totalAccounts: 1,
    defaultBalance: 1000  // Asigna 1000 ETH a la cuenta por defecto
  },
  database: {
    dbPath: dbPath,
  },
  chain: {
    chainId: 1337,       // Fija el chainId
    networkId: 1337,     // Fija el networkId
  }
};

const server = ganache.server(options);

server.listen(8545, (err) => {
  if (err) throw err;

  console.log("Ganache corriendo en http://127.0.0.1:8545");

  server.provider.on('message', (message) => {
    console.log("Interacción en Ganache:", message);
  });
});
