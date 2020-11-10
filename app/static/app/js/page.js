const nombre=document.getElementById("name")
const apellido=document.getElementById("apellido")
const email=document.getElementById("email")
const pass=document.getElementById("pass")
const repass=document.getElementById("repass")
const form=document.getElementById("form")
const parrafo= document.getElementById("warnings")

form.addEvenListener("submit", e=>{
    e.preventDefault()
    let warnings= ""
    let regexEmail= /^\w+([\.-]?)\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    parrafo.innerHTML= ""
    if(nombre.value.length <6){
        warnings += `El nombre no es valido <br>`
        entrar=true
    }
    console.log(regexEmail.test(email.value))
    if(regexEmail.test(email.value)){
        warnings += `El email no es valido <br>`
        entrar=true
    }

    if(pass.value.length <8){
        warnings += `El contraseña no es valido <br>`
        entrar=true
    }

    if(entrar){
        parrafo.innerHTML= warnings
    }else{
        parrafo.innerHTML= "enviado"
    }
}
)