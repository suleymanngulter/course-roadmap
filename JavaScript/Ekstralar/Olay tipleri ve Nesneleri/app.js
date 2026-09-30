//! addEventListener — öğeyi seç, olayı dinle, fonksiyonu çalıştır

let btn = document.querySelector("#btn")
let yazi = document.querySelector("#yazi")
let form = document.querySelector("#form")
let sonuc = document.querySelector("#sonuc")

btn.addEventListener("click", function () {
    sonuc.innerText = "Butona tıklandı"
    console.log("click")
})

yazi.addEventListener("input", function (event) {
    sonuc.innerText = "Yazılan: " + event.target.value
})

form.addEventListener("submit", function (event) {
    event.preventDefault()
    sonuc.innerText = "Form gönderildi"
})
