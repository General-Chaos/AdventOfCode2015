class password {
    [string]$value
    hidden [hashtable]$forward = @{}
    hidden [hashtable]$back =@{}
    hidden [array]$nums = 0..25
    hidden [array]$chars = 97..122
    hidden [int]$i =0
    #Constructor
    password([string]$value){
        $this.value = $value
        foreach($char in $this.chars) {
            $this.forward.Add("$($this.nums[$this.i])",([char]$char).ToString())
            $this.back.Add(([char]$char).ToString(),$this.nums[$this.i])
            $this.i++
        }
    }
    [void] Iterate(){
        $temp = $this.value.ToCharArray()
        ($temp.length -1)..0 | %{ 
            if($_ -ne 0){
                if($this.back["$($temp[$_])"] -lt 25){
                    $newindex = $this.back["$($temp[$_])"] + 1
                    $temp[$_] = $this.forward["$newindex"]
                    $this.value = $temp -join ""
                    break
                }
                else{
                    $temp[$_] = "a"
                }
            }
            else{
                if($this.back["$($temp[$_])"] -lt 25){
                    $newindex = $this.back["$($temp[$_])"] + 1
                    $temp[$_] = $this.forward["$newindex"]
                    $this.value = $temp -join ""
                    break
                }
                else{
                    $temp[$_] = "a"
                    $this.value = "a" + [string]($temp -join "")
                }

            }
        }
    }
}

$pass = [password]::new("z")
$pass
$pass.Iterate()
$pass