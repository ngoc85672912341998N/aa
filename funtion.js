var url = document.getElementsByTagName("script")
for (var i = 0; i<url.length; i++) {
    var url2 = url[i].getAttribute("src");
    url[i].setAttribute("src",String(url[i].src))
    console.log(url[i].src)
}
var url = document.getElementsByTagName("link")
for (var i = 0; i<url.length; i++) {
    var url2 = url[i].getAttribute("href");
    url[i].setAttribute("href",String(url[i].href))
    console.log(url[i].href)
}
var url = document.getElementsByTagName("a")
for (var i = 0; i<url.length; i++) {
    var url2 = url[i].getAttribute("href");
    url[i].setAttribute("href",String(url[i].href))
    console.log(url[i].href)
}
var url = document.getElementsByTagName("img")
for (var i = 0; i<url.length; i++) {
    var url2 = url[i].getAttribute("src");
    url[i].setAttribute("src",String(url[i].src))
    console.log(url[i].src)
}