################################################################################
#
#  Script reads list of customers from customer.txt file and 
#  looks up number of employees on Google.
#  Writes output to employees.txt
#
#  Dave Thornton
#  10/02/2018
#
################################################################################

Clear-Host

# Input file
$company_file = "c:\temp\customer.txt"

# Output file
$employee_file = "c:\temp\employee.txt"



$pt1 = "https://www.google.co.uk/search?source=hp&ei=XYd-WsmvBKqLgAbEsqGoAg&q="
$pt2 = "+number+of+employees&oq="
$pt3 = "+number+of+employees&gs_l=psy-ab.1.0.35i39k1j0i30k1l2j0i5i10i30k1j0i8i30k1l5.8654.28671.0.36488.9.8.0.0.0.0.126.552.7j1.8.0....0...1c.1.64.psy-ab..1.4.281.0..0i7i10i30k1j0i7i30k1.0.dpPHyqtNgoE"

$DB = import-csv $company_file

foreach ($Data in $DB)
    {
    $cus = $Data.cus
    $cus2 = $cus -replace " ", "+"
    $url = $pt1 + $cus2 + $pt2 + $cus2 + $pt3

    $WebResponse = Invoke-WebRequest($url) 

    $emp = $webResponse.ParsedHtml.getElementsByTagName('div') | ? {$_.className -match '_o0d'} | Select-Object 'textContent' | select-string "Number of employees"
    
    if ($emp -like '*employees:*')  
        {
        # Employee data found
        $junk, $employees = $emp -split ":"
        $employees = $employees -replace '[}]',''
        }
    Else
        {
        # Didn't find employee data
        $employees = " "
        }
    $output = $cus + ";" + $employees
    Write-Host $output
    Out-File -filepath $employee_file -InputObject $output -Append
    }