#1
Get-Content S:\Prod\AdventOfCode\NicMc\3\input.txt | %{$loc =0,0; $Track =@() ; $_ -split $null} | %{$Track+="$($loc[0]) $($loc[1])"; if($_ -eq "^"){$loc[0]++}elseif($_ -eq "v"){$loc[0]--}elseif($_ -eq ">"){$loc[1]++}elseif($_ -eq "<"){$loc[1]--}}
$Track | group | ? count -ge 1 | Measure-Object

#2
Get-Content S:\Prod\AdventOfCode\NicMc\3\input.txt | %{$loc1 =0,0;$loc2 =0,0 ; $Track =@();$i=0 ; $_ -split $null} |? {$_ -ne ""}| %{if(($i % 2) -eq 0){$r = 1}else{$r=2};$Track+="$((Get-Variable "loc$r" -ValueOnly)[0]) $((Get-Variable "loc$r" -ValueOnly)[1])"; if($_ -eq "^"){(Get-Variable "loc$r" -ValueOnly)[0]++}elseif($_ -eq "v"){(Get-Variable "loc$r" -ValueOnly)[0]--}elseif($_ -eq ">"){(Get-Variable "loc$r" -ValueOnly)[1]++}elseif($_ -eq "<"){(Get-Variable "loc$r" -ValueOnly)[1]--};$i++}
$Track | group | ? count -ge 1 | Measure-Object