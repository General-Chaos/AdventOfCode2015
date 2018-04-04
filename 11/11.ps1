class password {
    [string]$value
    #Constructor
    password([string]$value){
        $this.value = $value
    }
    [void] Iterate(){
        $temp = $this.value.ToCharArray()
        $iterated = $false
        $i = 0
        while(!$iterated){
            if($i -lt ($temp.Length -1)){
                $currentchar = $temp[$temp.length - 1 - $i]
                if([byte]$currentchar -lt 122){
                    $newchar = [char]([byte]$currentchar +1)
                    $temp[$temp.length -1 -$i ] = $newchar
                    $iterated = $true
                }
                else{
                    $temp[$temp.length - 1 - $i] = [char]"a"
                    $i++
                }
            }
            else{
                $temp = ("a"+($temp -join "")).ToCharArray()
                $iterated = $true
            }
        }
        $this.value = $temp -join ""
    }
    [bool] Validate(){
        if($this.value -match "(\w)\1.*(\w)\2" -and $this.value -notmatch "(i|o|l)"){
            if($this.value.length -gt 3){
                foreach($index in 0..($this.value.Length -3)){
                    if(([byte]$this.value.tochararray()[$index] -eq ([byte]$this.value.tochararray()[$index+1] -1)) -and ([byte]$this.value.tochararray()[$index] -eq ([byte]$this.value.tochararray()[$index+2] -2)) ){
                        return $true
                    }
                    elseif($index -eq ($this.value.Length -3)){
                        return $false
                    }
                }
            }
        }
        else{
            return $false
        }
        return $false
    }
}

$pass = [password]::new("cqjxjnds")
while(!($pass.Validate())){
    $pass.Iterate()
}
$pass
$pass.Iterate()
while(!($pass.Validate())){
    $pass.Iterate()
}
$pass