function generateTable(s1,s2,alignCorrds) {
    // Code based on: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Traversing_an_HTML_table_with_JavaScript_and_DOM_Interfaces
    n1 = s1.length + 1
    n2 = s2.length + 1
    const tblBody = document.createElement("div");
    tblBody.className = "m-3 p-2"
    tblBody.style="overflow: auto; max-height: 100vh; display: inline-block; max-width: 95%; border-style: double;"
    const blankRow = document.createElement("div");
    tblBody.appendChild(blankRow);
    for (let i = 0; i <= n1; i++) {
        const row = document.createElement("div");
        row.className = "board-row"
        row.style.width = (n2 + 1) * 34 + "px";
        for (let j = 0; j <= n2; j++) {

            const cell = document.createElement("button");
            cell.className = "square"
            cellText = ""
            if (i == 0 && j > 1) {
                cellText = document.createTextNode(s2[j - 2]);
            }
            else if (j == 0 && i > 1) {
                cellText = document.createTextNode(s1[i - 2]);
            }
            else {
                cellText = document.createTextNode("");
                console.log(alignCorrds);
                
                    
            }
            cell.appendChild(cellText);
            if (alignCorrds.includes(`(${i - 1}, ${j - 1})`)) {
                console.log(`(${i}, ${j})`);
                cell.style.background = "#89C35C"
            }
            if (i == 0 || j == 0) {
                cell.style.border = "1px solid #fff"
            }
            row.appendChild(cell);

            
        }

        // add the row to the end of the table body
        tblBody.appendChild(row);
    }

    // put the <tbody> in the <table>
    // tbl.appendChild(tblBody);
    // appends <table> into <body>
    document.body.appendChild(tblBody);
    // sets the border attribute of tbl to '2'
    tblBody.setAttribute("border", "2");
}

// function generateTable(s1,s2,alignCorrds) {
//     // Code based on: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Traversing_an_HTML_table_with_JavaScript_and_DOM_Interfaces
//     n1 = s1.length
//     n2 = s2.length
//     // creates a <table> element and a <tbody> element
//     const tbl = document.createElement("table");
//     tbl.className = "table m-3"
//     const tblBody = document.createElement("tbody");

//     // creating all cells
//     for (let i = 0; i <= n1; i++) {
//     // creates a table row
//     const row = document.createElement("tr");

//     for (let j = 0; j <= n2; j++) {
//         // Create a <td> element and a text node, make the text
//         // node the contents of the <td>, and put the <td> at
//         // the end of the table row
//         const cell = document.createElement("td");
//         cell.style = "width: 10px"
//         const cellText = document.createTextNode(`cell in row ${i}, column ${j}`);
//         cell.appendChild(cellText);
//         row.appendChild(cell);
//     }

//     // add the row to the end of the table body
//     tblBody.appendChild(row);
//     }

//     // put the <tbody> in the <table>
//     tbl.appendChild(tblBody);
//     // appends <table> into <body>
//     document.body.appendChild(tbl);
//     // sets the border attribute of tbl to '2'
//     tbl.setAttribute("border", "2");
// }