const aux = [
   {
    name: 'Jagunço',
    desciption: 'Iniciou no dia...',
    },
    {
    name: 'Leonil',
    desciption: 'Começou a trabalhar...',
    },
    {
    name: 'Ricardo',
    desciption: 'Família de 6 pessoas',
    },
]

const tableBody = document.getElementById("tableBody");

aux.forEach(function(items) {
  const row = document.createElement("tr");
    Object.keys(items).forEach((key) => {
      const newCell = document.createElement("td");
      newCell.textContent = items[key];
      row.appendChild(newCell);
    })  
  tableBody.appendChild(row);
});