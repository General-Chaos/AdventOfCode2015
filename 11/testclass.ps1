class testclass {
        [array]$value
        hidden [array]$b =1..25
    testclass([string]$value){
        $value | %{ $_} 
        $this.b | %{ $_}
    }
}
[testclass]::new((1..13))