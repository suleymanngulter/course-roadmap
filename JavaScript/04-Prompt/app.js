//! prompt / alert — tarayıcıda index.html açarak dene

// prompt: kullanıcıdan yazı alır (her zaman string döner)
let ad = prompt("Adınızı girin")
console.log("Merhaba, " + ad)

// sayı için başına + koy
let sayi = +prompt("Bir sayı girin")
console.log("3 katı:", sayi * 3)

// alert: ekranda mesaj gösterir
alert("Girilen ad: " + ad)
