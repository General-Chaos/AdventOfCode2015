#This is a brute force method, veeeeerrryy slow
$input = Get-Content $PSScriptRoot\input.txt
$dists=@()
$input | %{
    $_ -match "(\w+)\s+to\s+(\w+)\s+=\s+(\d+)" | out-null
    $dists+=[pscustomobject]@{
        Start = $Matches[1]
        JEnd = $Matches[2]
        Distance = $Matches[3]
    }
    $dists+=[pscustomobject]@{
        Start = $Matches[2]
        JEnd = $Matches[1]
        Distance = $Matches[3]
    }
}
$cities =$dists | group Start | % Name

function get-rand {
    param(
        $array
    )
    $out = @()
    while($out.Length -lt $array.Length){
        $array | Get-Random | ? {$_ -notin $out} | %{$out +=$_}
    }
    $out
}
$results=@()
0..100000 | %{
    $random = get-rand $cities
    $distance = 0
     0..($random.length -1) | %{$num = $_
        $dists | ?{$_.Start -eq $random[$num] -and $_.Jend -eq $random[$num+1]}| %{$Distance= $Distance + $_.Distance}}
    $results+=$distance
}
"First Answer"
$results | group | sort name select -first 1
"Second Answer"
$results | group | sort name select -last 1