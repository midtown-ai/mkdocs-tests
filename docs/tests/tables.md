# Tables

## Styled Table

| First Header | Second Header | Third Header
| :----------- |:-------------:| -----------:
| Left         | Center        | Right :material-check:
| Left         | Center        | Right :material-check-all:
| Left         | Center        | Right :material-close:

```
| First Header | Second Header | Third Header
| :----------- |:-------------:| -----------:
| Left         | Center        | Right :material-check:
| Left         | Center        | Right :material-check-all:
| Left         | Center        | Right :material-close:

# To HTML

<table>
<thead>
<tr>
<th style="text-align: left;">First Header</th>
<th style="text-align: center;">Second Header</th>
<th style="text-align: right;">Third Header</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Left</td>
<td style="text-align: center;">Center</td>
<td style="text-align: right;">Right <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M21 7 9 19l-5.5-5.5 1.41-1.41L9 16.17 19.59 5.59z"></path></svg></span></td>
</tr>
<tr>
<td style="text-align: left;">Left</td>
<td style="text-align: center;">Center</td>
<td style="text-align: right;">Right <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M.41 13.41 6 19l1.41-1.42L1.83 12m20.41-6.42L11.66 16.17 7.5 12l-1.43 1.41L11.66 19l12-12M18 7l-1.41-1.42-6.35 6.35 1.42 1.41z"></path></svg></span></td>
</tr>
<tr>
<td style="text-align: left;">Left</td>
<td style="text-align: center;">Center</td>
<td style="text-align: right;">Right <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg></span></td>
</tr>
</tbody>
</table>

# To CSS

/* General table styling */
table {
    width: 100%; /* Make the table take full width of the container */
    border-collapse: collapse; /* Remove gaps between table cells */
    margin: 20px 0; /* Add spacing above and below the table */
    font-family: Arial, sans-serif; /* Use a clean font */
    font-size: 16px; /* Set font size */
    text-align: left; /* Default text alignment */
}

/* Header styling */
table thead th {
    background-color: #f4f4f4; /* Light gray background for headers */
    color: #333; /* Dark text color for contrast */
    font-weight: bold; /* Make header text bold */
    padding: 10px; /* Add padding inside header cells */
    border: 1px solid #ddd; /* Add light borders */
}

/* Row styling */
table tbody tr:nth-child(even) {
    background-color: #f9f9f9; /* Alternate row background */
}

table tbody tr:nth-child(odd) {
    background-color: #fff; /* Default row background */
}

/* Cell styling */
table td {
    padding: 10px; /* Add padding inside cells */
    border: 1px solid #ddd; /* Add borders to table cells */
}

/* Align specific cells */
table td:nth-child(1) {
    text-align: left; /* Align the first column to the left */
}

table td:nth-child(2) {
    text-align: center; /* Center-align the second column */
}

table td:nth-child(3) {
    text-align: right; /* Right-align the third column */
}

/* SVG inside table */
table .twemoji svg {
    width: 16px; /* Set a uniform size for icons */
    height: 16px;
    fill: #888; /* Default icon color */
    vertical-align: middle; /* Align icon with text */
}

/* Add hover effect for rows */
table tbody tr:hover {
    background-color: #f1f1f1; /* Light gray on hover */
    cursor: pointer; /* Pointer cursor for interactive tables */
}
```

