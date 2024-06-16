const don = [
    {
    name: 'Felipe',
    description: 'Usuário administrador ...',
    },
    {
    name: 'Gustavo',
    description: 'Usuário administrador ...',
    },
    {
    name: 'Silvia',
    description: 'Usuário Doador ...',
    },
]

const tableBody = document.getElementById("tableBody");

don.forEach(function(items) {
  const row = document.createElement("tr");
    Object.keys(items).forEach((key) => {
      const newCell = document.createElement("td");
      newCell.textContent = items[key];
      row.appendChild(newCell);
    })  
  tableBody.appendChild(row);
});