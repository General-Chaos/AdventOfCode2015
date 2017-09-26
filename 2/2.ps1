#1
Import-Csv S:\Prod\AdventOfCode\NicMc\2\Input.txt -Delimiter x -Header l,w,h | select l,w,h, @{n="2lw";e={2*$_.l*$_.w}}, @{n="2wh";e={2*$_.w*$_.h}}, @{n="2hl";e={2*$_.h*$_.l}} | select 2lw,2wh,2hl, @{n="min";e={($_."2hl",$_."2lw",$_."2wh"| sort | select -first 1)/2}} | %{$_."2hl",$_."2lw",$_."2wh",$_.min}|measure-object -Sum
#2
Get-Content S:\Prod\AdventOfCode\NicMc\2\Input.txt | select @{n="Sides";e={[int[]]($_ -split "x")|sort}} | %{(($_.Sides)[0]+($_.Sides)[1])*2 + ($_.Sides)[0]*($_.Sides)[1]*($_.Sides)[2]} | Measure-Object -Sum | % sum