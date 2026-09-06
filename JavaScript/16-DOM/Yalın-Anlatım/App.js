//! ============================================================
//!  DOM NEDİR?
//! ============================================================
//* Tarayıcı HTML dosyasını okur ve her etiketi bir "düğüm" yapar.
//* Bu düğümler üst-alt ilişkisiyle bir ağaç oluşturur. İşte DOM bu ağaçtır.
//* JavaScript bu ağaca dokunarak sayfayı okur ve değiştirir.

//
//   HTML kodu                         Tarayıcının gördüğü DOM
//
//   <html>                            document
//     <body>                              │
//       <h2>Başlık</h2>                  html
//       <ul>                              │
//         <li>html</li>                  body
//         <li>css</li>                 /      \
//       </ul>                       h2          ul
//     </body>                    "Başlık"     /    \
//   </html>                                 li      li
//                                          "html"  "css"
//
//* Kural: önce öğeyi seç, sonra oku / değiştir / dinle.
//*
//*   1) Öğe seçmek      →  "hangi kutuyu istiyorum?"
//*   2) Metin içeriği   →  "kutunun içindeki yazı ne / ne olsun?"
//*   3) Olay dinlemek   →  "kullanıcı bir şey yapınca ne olsun?"
//*


//! ============================================================
//!  1) ÖĞE SEÇMEK   (17-1 klasörünün yalın hali)
//! ============================================================
//* Sayfada bir öğeye ulaşmak = o öğeyi değiştirebilmek.
//* Hepsi document üzerinden başlar.

//
//                      document
//                          │
//          ┌───────────────┼───────────────┬──────────────┐
//          ▼               ▼               ▼              ▼
//   getElementById   getElementsBy    querySelector   querySelectorAll
//        ("id")       ClassName/Tag     (CSS seçici)    (CSS seçici)
//          │               │               │              │
//          ▼               ▼               ▼              ▼
//      tek öğe        HTMLCollection    ilk eşleşen     NodeList
//                    (canlı liste)      tek öğe        (statik liste)
//


//? --- id ile seçmek: getElementById ---
//* Sayfada id benzersizdir. Bu yüzden tek bir öğe döner.

//
//   <h2 id="baslik">...</h2>
//            │
//            └──►  document.getElementById("baslik")
//                           │
//                           ▼
//                    o h2 öğesinin kendisi
//

let baslik = document.getElementById("baslik")
console.log("id ile:", baslik)


//? --- class ile seçmek: getElementsByClassName ---
//* Aynı class birden fazla öğede olabilir.
//* Bu yüzden tek öğe değil, HTMLCollection (liste) döner.

//
//   <button class="myButton">  ┐
//   <button class="myButton">  ├── hepsi aynı class
//   <button class="myButton">  ┘
//                │
//                ▼
//        HTMLCollection [btn, btn, btn]
//                │
//                ├── [0] birinci buton
//                ├── [1] ikinci buton
//                └── [2] üçüncü buton
//

let butonlar = document.getElementsByClassName("myButton")
console.log("class ile (liste):", butonlar)

for (const buton of butonlar) {
    console.log("tek tek buton:", buton)
}


//? --- etiket adıyla seçmek: getElementsByTagName ---
//* Tüm <h5> etiketlerini ister. Yine HTMLCollection döner.

let h5ler = document.getElementsByTagName("h5")
console.log("tag ile:", h5ler)


//? --- querySelector: CSS seçici, SADECE İLK eşleşeni verir ---
//* class için başına "."  →  .kutu
//* id için başına "#"     →  #kutuId
//* etiket için doğrudan   →  span

//
//   sayfada 3 tane span var:
//
//   [span] [span] [span]
//      ▲
//      └── querySelector("span")  sadece BİRİNCİYİ alır
//
//* Toplu işlem için querySelector yetmez.

let classIle = document.querySelector(".kutu")
let idIle = document.querySelector("#kutuId")
let tagIle = document.querySelector("span")
console.log("querySelector class:", classIle)
console.log("querySelector id:", idIle)
console.log("querySelector tag (sadece ilk):", tagIle)


//? --- querySelectorAll: CSS seçici, HEPSİNİ verir ---
//* Dönen şey NodeList'tir. Döngü ile gezilebilir.

//
//   [span] [span] [span]
//      ▲      ▲      ▲
//      └──────┴──────┘
//      querySelectorAll("span")  →  NodeList(3)
//

let tumSpanler = document.querySelectorAll("span")
console.log("querySelectorAll:", tumSpanler)


//! ------------------------------------------------------------
//!  HTMLCollection (canlı)  vs  NodeList (statik)
//! ------------------------------------------------------------
//* İkisi de "liste gibi" durur. Fark: yeni öğe eklenince güncellenir mi?

//
//   BAŞLANGIÇ
//   ul.myList →  [ html ] [ css ] [ js ]
//
//
//   sonra yeni <li>react</li> eklenir
//                      │
//                      ▼
//
//   HTMLCollection (getElementsByTagName)
//   canlıdır, anında uzar
//   [ html ] [ css ] [ js ] [ react ]     length: 4
//
//   NodeList (querySelectorAll)
//   çekildiği andaki fotoğraftır, değişmez
//   [ html ] [ css ] [ js ]               length: 3
//

let canliListe = document.getElementsByTagName("li")
let statikListe = document.querySelectorAll("li")

console.log("eklemeden önce canlı:", canliListe.length)
console.log("eklemeden önce statik:", statikListe.length)

let yeniLi = document.createElement("li")
yeniLi.innerHTML = "react"
document.querySelector(".myList").appendChild(yeniLi)

console.log("ekledikten sonra canlı:", canliListe.length)   // 4 olur
console.log("ekledikten sonra statik:", statikListe.length) // 3 kalır


//! ============================================================
//!  2) METİN İÇERİĞİ   (17-2 klasörünün yalın hali)
//! ============================================================
//* Öğeyi seçtik. Şimdi içindeki yazıyı okuyacağız veya değiştireceğiz.
//* İki yol: innerHTML ve innerText. Okumak aynı, yazmak farklıdır.

//? --- okumak ---

let paragraf = document.querySelector(".paragraf")
console.log("öğenin kendisi:", paragraf)
console.log("innerHTML:", paragraf.innerHTML)
console.log("innerText:", paragraf.innerText)


//? --- innerHTML: HTML'i anlar ---
//* İçine etiket yazarsan tarayıcı onu gerçek HTML gibi uygular.

//
//   paragraf.innerHTML = "<b>kalın yazı</b>"
//                              │
//                              ▼
//                     ekranda:  kalın yazı
//                               ^^^^^
//                               kalın görünür
//                     çünkü <b> etiketi işlenir
//

let htmlParagraf = document.querySelector(".paragrafHtml")
htmlParagraf.innerHTML = "<b>Paragrafımı kalın yaptım!</b>"


//? --- innerText: her şeyi düz yazı sanar ---
//* Etiket yazsan bile ekranda etiket karakterleri görünür.

//
//   paragraf.innerText = "<b>kalın yazı</b>"
//                              │
//                              ▼
//                     ekranda:  <b>kalın yazı</b>
//                     etiket çalışmaz, harf harf yazılır
//

let textParagraf = document.querySelector(".paragrafText")
textParagraf.innerText = "<b>deneme yazısı</b>"


//
//   KISA KARŞILAŞTIRMA
//
//   ┌─────────────┬──────────────────────────────┐
//   │  innerHTML  │  HTML etiketini uygular      │
//   │  innerText  │  her şeyi düz metin yazar    │
//   └─────────────┴──────────────────────────────┘
//


//! ============================================================
//!  3) OLAY DİNLEMEK   (17-3 klasörünün yalın hali)
//! ============================================================
//* Seçmek ve yazı değiştirmek senin kodun çalışınca olur.
//* Olay dinlemek ise kullanıcı bir şey YAPINCA kodun çalışmasıdır.

//
//   [ kullanıcı tıklar / yazar / üzerine gelir ]
//                      │
//                      ▼
//           tarayıcı bir OLAY üretir  (click, input...)
//                      │
//                      ▼
//        addEventListener bu olayı bekliyordur
//                      │
//                      ▼
//              senin fonksiyonun çalışır
//

//? --- tıklama ---
//* addEventListener(olayAdı, çalışacakFonksiyon)

let olayButon = document.getElementById("olayButon")
let olaySonuc = document.getElementById("olaySonuc")

olayButon.addEventListener("click", function () {
    olaySonuc.innerText = "Butona tıklandı!"
    console.log("click oldu")
})


//? --- yazı yazınca ---
//* input olayı, her harfte çalışır.

let olayInput = document.getElementById("olayInput")

olayInput.addEventListener("input", function (event) {
    olaySonuc.innerText = "Yazılan: " + event.target.value
    console.log("input oldu:", event.target.value)
})


//? --- olay nesnesi (event) ---
//* Fonksiyona gelen event, "ne oldu, nerede oldu?" sorusunun cevabıdır.

//
//   addEventListener("click", function (event) { ... })
//                                      │
//                                      ▼
//                         event.type    →  "click"
//                         event.target  →  tıklanan öğe
//

olayButon.addEventListener("mouseover", function (event) {
    console.log("olay türü:", event.type)
    console.log("hedef öğe:", event.target)
})


//
//   SIK KULLANILAN OLAYLAR
//
//   click      →  tıklama
//   mouseover  →  üzerine gelme
//   input      →  yazı yazıldıkça
//   change     →  değer değişip odak gidince
//   submit     →  form gönderilince  (event.preventDefault ile sayfa yenilenmesini kes)
//   keydown    →  tuşa basılınca
//


//! ============================================================
//!  TEK CÜMLELİK ÖZET
//! ============================================================
//* 1) Seç     : getElementById / querySelector / querySelectorAll
//* 2) Oku-yaz : innerText (düz yazı)  |  innerHTML (HTML'li yazı)
//* 3) Dinle   : addEventListener("click", fonksiyon)
