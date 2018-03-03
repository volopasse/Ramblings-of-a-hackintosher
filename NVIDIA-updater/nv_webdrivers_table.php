<!-- Styles are optional, but I like them -->
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>

<?php
$data = shell_exec(escapeshellcmd('python fetch_table.py'));
echo($data);
?>
