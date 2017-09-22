class lookandsay {
    [string]$value 
    #Constructor
     lookandsay([string]$value){
         $this.value = $value
     }
     [void] Transform(){
        $this.value = [regex]::Replace($this.value,"([0-9])\1*",{
            "$($args.value.length)$(($args.value -split '')[1] )"
        })
     }
}

$object =[lookandsay]::new("1321131112")

#transform object 40 times
0..39 | % {
    $object.Transform()
}

$firstresult = $object.value.Length

Write-Output "The value of the first Answer is: $firstresult"

#Transform the object 10 more times
0..9 | %{
    $object.Transform()
}

$secondresult = $object.value.Length

Write-Output "The value of the second answer is: $secondresult"