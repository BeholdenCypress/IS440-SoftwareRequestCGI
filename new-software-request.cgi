#!C:\xampp\perl\bin\perl.exe
#
#
#Released under the GNU General Public License
#
#Software Request form for user input and output to CSV file.
#Copyright (C) 2018 Kacey Howell
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#
use CGI qw(:standard);
$TITLE_DESC="New Software Request";
$FIRST_DESC="Please enter your first name";
$LAST_DESC="Please enter your last name";
$PHONE_DESC="Please enter your office phone number";
$DEPT_DESC="Please enter your department";
$SOFT_DESC="Please enter the name of the software you need";

if (! param()) {
showForm();
} else {
processQuery();
}

sub showForm {
    print header();
    print <<EOT;
    <html>
    <head>
    <title>New Software Request</title>
    </head>
    <body>
    <h1>$TITLE_DESC</h1>
    <br>
    <h2>Please enter the required information</h2>
    <form method="post" action="New-Software-Process.cgi">
    <table>
    <tr><td>*$FIRST_DESC<td><input type="text" name="FirstName" required>
    <tr><td>*$LAST_DESC<td><input type="text" name="LastName" required>
    <tr><td>*$PHONE_DESC<td><input class="no-spinners" type="number" name="OffPhone" required>
    <tr><td>*$DEPT_DESC<td><input type="text" name="Department" required>
    <tr><td>*$SOFT_DESC<td><input type="text" name="Software" required>
    <tr align=LEFT><td colspan=2 LEFT><input type="Submit" value="Submit Software Request">
    </table>
    </form>
    <p>*indicates a required field</p>
    </body>
    
EOT
}