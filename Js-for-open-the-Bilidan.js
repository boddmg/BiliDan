// ==UserScript==
// @name         Js for open the Bilidan.
// @namespace    http://your.homepage/
// @version      0.1
// @description  enter something useful
// @author       You
// @match        http://www.bilibili.com/*
// @grant        none
// ==/UserScript==

function addJQuery(callback) {
    var script = document.createElement("script");
    script.setAttribute("src", "//libs.baidu.com/jquery/2.0.0/jquery.min.js");
    script.addEventListener('load', function() {
        var script = document.createElement("script");
        script.textContent = "window.jQ=jQuery.noConflict(true);(" + callback.toString() + ")();";
        document.body.appendChild(script);
    }, false);
    document.body.appendChild(script);
}

function main(){
    $.get("http://127.0.0.1:8080/"+encodeURIComponent(location.href));
}

addJQuery(main);