function check(){
    user_number = document.querySelector("#letter").value
    fetch(`/404?user_number=${user_number}`)
    .then(
        function (response){
            return(response.json())
        })
    .then(
        //словарь
        function(deta){
            let hint = deta["hint"]
            let attempts = deta["attempts"]
            document.querySelector("#attemps").innerHTML = `Осталось:  ${attempts} попыток`
            document.querySelector("#p1").innerHTML =  `Подсказка: ${hint}`
        }) 


}

    function reset(){
       document.querySelector("#attemps").innerHTML = "Осталось 10 попыток"
       document.querySelector("#p1").innerHTML = "Количесто от 1 до 100"
       document.querySelector("#letter").value = ""
       fetch(`/404040`)
    

    }

document.querySelector("#reload").addEventListener("click",reset)
document.querySelector("#check").addEventListener("click",check)

           