$input = Get-Content $PSScriptRoot\input.txt 
 $input = $input  -replace "\s+$" -replace "^\s+"

#replace with / to avoid clashes with [regex] operation "\\x.." would be caught, could of just replaced \x.. with a random char as it wasnt needed in part 2
$output = $input  -replace "(^`"|`"$)" -replace "\\`"" ,"`"" -replace "\\\\" , "/" | %{
    [regex]::Replace($_,"\\x([a-f0-9]{2})",{[char]([convert]::ToInt16(($args.groups[1]),16))})
}
$firstresult = ($input | Measure-Object -Character | % Characters) - ($output | Measure-Object -Character | % Characters)

Write-Output "The Value of the first answer is $firstresult"

#Part2 is easy
$output2 = $input2 -replace "\\","\\" -replace "\`"", "\`"" -replace "^","`"" -replace "$","`""
$secondresult = ($output2 | Measure-Object -Character | % Characters) - ($input | Measure-Object -Character | % Characters)
Write-Output "The Value of the second answer is $secondresult"