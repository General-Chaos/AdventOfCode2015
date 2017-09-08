Get-Content $PSScriptRoot\input.txt | % -Begin{$array=@();$dumb=@(); 0..999|%{$dumb+=$false};0..999 | %{$array+= $false ;$array[$_] = $dumb.Clone() }} {if($_ -match "turn on"){$action ="on"}elseif($_ -match "turn off"){$action ="off"}else{$action ="toggle"};$found = $_ -match ".*\s(\d+),(\d+).*\s(\d+),(\d+)";[pscustomobject]@{Action=$action;Start=$matches[1],$matches[2];End=$matches[3],$matches[4]}} | %{$obj=$_;if($_.Action -eq "on"){$_.Start[0]..$_.End[0]|%{$x=$_;$obj.Start[1]..$obj.End[1]|%{$array[$x][$_]=$true}}}elseif($_.Action -eq "off"){$_.Start[0]..$_.End[0]|%{$x=$_;$obj.Start[1]..$obj.End[1]|%{$array[$x][$_]=$false}}}elseif($_.Action -eq "toggle"){$_.Start[0]..$_.End[0]|%{$x=$_;$obj.Start[1]..$obj.End[1]|%{if($array[$x][$_]){$array[$x][$_]=$false}else{$array[$x][$_]=$true}}}}} -End{$array | %{$_} | ? {$_ -eq $true}|Measure-object}
