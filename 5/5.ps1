Get-Content $PSScriptRoot\input.txt | ? {$_ -match "[aeiou]{1}.*[aeiou]{1}.*[aeiou]{1}.*" -and $_ -match "(.)\1" -and $_ -notmatch "(ab|cd|pq|xy)"} |Measure-Object

Get-Content $PSScriptRoot\input.txt | ? {$_ -match "(..).*\1" -and $_ -match "(.).\1" } | Measure-Object