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
use CGI qw(:cgi-lib :standard);

$TITLE_DESC="Please enter the required information";
$FIRST_DESC="Please enter your first name";
$LAST_DESC="Please enter your last name";
$PHONE_DESC="Please enter your office phone number";
$DEPT_DESC="Please enter your department";
$SOFT_DESC="Please enter the name of the software you need";

my @params = param();
my $firstname = param('FirstName');
my $lastname = param('LastName');
my $officephone = param('OffPhone');
my $department = param('Department');
my $software = param('Software');

showForm();

sub showForm {
    print header();
    print <<EOT;
    <html>
    <head>
    <title>Submission Results</title>
    </head>
    <body>
    <h1>You have submitted your information</h1>
    <h2>Here is the information you submitted</h2>
    <p>$FIRST_DESC: <b>$firstname</b></p>
    <p>$LAST_DESC: <b>$lastname</b></p>
    <p>$PHONE_DESC: <b>$officephone</b></p>
    <p>$DEPT_DESC: <b>$department</b></p>
    <p>$SOFT_DESC: <b>$software</b></p>
    <form method="post" action="new-software-request.cgi">
    <input type="Submit" value="Click here to add another request">
    </form>
    </body>
    </html>

EOT
}

open(LOG, ">>softwareRequest.csv") || die "Could not open softwareRequest.csv, $!";
 print LOG "$firstname, $lastname, $officephone, $department, $software\n";
close(LOG);




