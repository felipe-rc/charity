const FROM_TO = {
    item: 'Item',
    quantidade: 'Quantidade',
    status: 'Status',
}

const requests = [
    {
    item: 'Leite',
    quantidade: '2',
    status: 'Aceita',
    },
    {
    item: 'Ovos',
    quantidade: '1',
    status: 'Concluída',
    },
    {
    item: 'Óleo',
    quantidade: '2',
    status: 'Aberta',
    },
    {
    item: 'Sabonete',
    quantidade: '4',
    status: 'Aberta',
    },
]

const tableBody = document.getElementById("tableBody");

requests.forEach(function(items) {
  const row = document.createElement("tr");
    Object.keys(items).forEach((key) => {
      const newCell = document.createElement("td");
      newCell.textContent = items[key];
      row.appendChild(newCell);
    })  
  tableBody.appendChild(row);
});