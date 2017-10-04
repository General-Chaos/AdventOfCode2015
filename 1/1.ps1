get-content $PSScriptRoot\Input.txt -Raw | %{$i=0;$j=1;$_ -split ""}| ?{$_ -match "(\(|\))"}| %{if($_ -eq "("){$i++}elseif($_ -match "\)"){$i--};if($i -lt 0){$j;break};$j++}
$i