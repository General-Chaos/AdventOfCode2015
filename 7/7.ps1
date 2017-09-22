$a =Get-Content $PSScriptRoot\input.txt| %{
    $found = $_ -match "([a-z0-9]+)\s+([A-Z0-9]+)\s+([a-z0-9]+).*->\s+([a-z]+)";
    if($found){[PSCustomObject]@{Action = $Matches[2];input1=$matches[1];input2=$matches[3];output=$matches[4]}
    }else{
        $found2 = $_ -match "(NOT)\s+([a-z]+)\s+->\s+([a-z]+)";
        if($found2){
            [PSCustomObject]@{
                Action = $Matches[1];
                input1=$matches[2];input2=$null;output=$matches[3]
            }
        }else{
            $found3 = $_ -match "([a-z0-9]+)\s+->\s+([a-z]+)";
            [PSCustomObject]@{
                Action = "ADDITION";input1=$matches[1];
                input2=$null;output=$matches[2]
            }
        };
    };
}

function get-result {
    param(
        $obj,
        $results
    )
    if($obj.input1 -match "^\d+$"){
        $input1 = $obj.input1
    }elseif($obj.input1 -ne $null){
        $input1 = $results[$obj.input1]
    }
    if($obj.input2 -match "^\d+$"){
        $input2 = $obj.input2
    }elseif($obj.input2 -ne $null){
        $input2 = $results[$obj.input2]
    }
    Switch($obj.Action){
        NOT{-bnot $input1}
        OR{$input1 -bor $input2}
        AND{$input1 -band $input2}
        LSHIFT{$input1 -shl $input2}
        RSHIFT{$input1 -shr $input2}
        ADDITION{$input1}
    }
}

$results = @{}
while($results.Count -lt $a.Count){
    $a | ? {($_.input1 -in $results.keys -or $_.input1 -match "^\d+$" -or $_.input1 -eq $null) -and ($_.input2 -in $results.keys -or $_.input2 -match "^\d+$" -or $_.input2 -eq $null) -and $_.output -notin $results.keys} |
        %{
            $results.add("$($_.output)" , (get-result $_ $results))
        }
}

$firstresult=$results["a"]
Write-output "First result is : $firstresult"
#Override b input
$a | ? output -eq "b" | % {$_.input1 = $firstresult}
#reset results and rerun
$results = @{}
while($results.Count -lt $a.Count){
    $a | ? {($_.input1 -in $results.keys -or $_.input1 -match "^\d+$" -or $_.input1 -eq $null) -and ($_.input2 -in $results.keys -or $_.input2 -match "^\d+$" -or $_.input2 -eq $null) -and $_.output -notin $results.keys} |
        %{
            $results.add("$($_.output)" , (get-result $_ $results))
        }
}
$secondresult=$results["a"]
Write-output "First result is : $secondresult"