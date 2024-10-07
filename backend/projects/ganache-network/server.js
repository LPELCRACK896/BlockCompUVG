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
  wallet: { totalAccounts: 0 },
  logging: {
    quiet: false,
  },
  database: {
    dbPath: dbPath,
  },
};

const server = ganache.server(options);

server.listen(8545, (err) => {
  if (err) throw err;

  console.log("Ganache corriendo en http://127.0.0.1:8545");

  server.provider.on('message', (message) => {
    console.log("Interacción en Ganache:", message);
  });
});
