let fetchUrl = 'http://ysa8497.pythonanywhere.com/api/';
const urlMain = 'http://ysa8497.pythonanywhere.com/api/';
const urlPolitics = 'http://ysa8497.pythonanywhere.com/api/politics/';
const urlEconomic = 'http://ysa8497.pythonanywhere.com/api/economic/';
const urlSociety = 'http://ysa8497.pythonanywhere.com/api/society/';
const urlCulture = 'http://ysa8497.pythonanywhere.com/api/culture/';
const urlForeign = 'http://ysa8497.pythonanywhere.com/api/foreign/';
const urlDigital = 'http://ysa8497.pythonanywhere.com/api/digital/';
const urlSearch = 'http://ysa8497.pythonanywhere.com/api/main/?search=';

function getArticle(fetchUrl){
    fetch(fetchUrl).then(function(response) {
        if (response.status === 200 || res.status === 201) {
            response.text().then(function(text) {
                var newsText = JSON.parse(text);
                var columns = document.getElementById('columns');
                for (var i in newsText) {
                    var newFigure = document.createElement("figure");
                    var figcaption = document.createElement("figcaption");
                    var newsPopup = document.createElement("div"); 
                    newsPopup.id = "newsPopup";
                    
                    figcaption.innerHTML += 
                    "<img alt='' src="+newsText[i].img+">"+
                    "<button type='button' id=\"modal_btn\">"+
                    newsText[i].title+"</button>"

                    newsPopup.innerHTML = 
                    "<div id='black' class='black_bg'>"+
                    "<div id='popup' class='modal_wrap'>"+
                    
                    "<a id='close_btn' href='#0'>닫기</a>"+
                    newsText[i].contents+
                    
                    "</div></div>"

                    columns.appendChild(newFigure);
                    newFigure.appendChild(figcaption);
                    figcaption.appendChild(newsPopup);   
                }

                var cols = document.querySelectorAll('#modal_btn'); 
                var close = document.querySelectorAll('#close_btn');
                for(var k=0; k<cols.length; k++){
                    (function(m) {
                        console.log(m);
                        cols[m].addEventListener('click', event => onClick(m));
                        close[m].addEventListener('click', event => offClick(m));
                    })(k);
                }
            })
        } else { 
            console.error(rxes.statusText);
        }
    }).catch(err => console.error(err));
}

function onClick(index) {
    console.log(index);
    document.querySelectorAll('#popup')[index].style.display ='block';
    document.querySelectorAll('#black')[index].style.display ='block';
}  

function offClick(index) {
    console.log(index);
    document.querySelectorAll('#popup')[index].style.display ='none';
    document.querySelectorAll('#black')[index].style.display ='none';
}  

(function (window, document) {
    'use strict';
    const  $toggles = document.querySelectorAll('.toggle');
    const $toggleBtn = document.getElementById('toggle-btn');

    $toggleBtn.addEventListener('click', function() {
        toggleElements();
    });
   

    function toggleElements() {
        [].forEach.call($toggles, function (toggle) {
            toggle.classList.toggle('on');
        });
    }

}) (window, document)

var politics = document.getElementById('politics');
var economic = document.getElementById('economic');
var society = document.getElementById('society');
var culture = document.getElementById('culture');
var foreign = document.getElementById('foreign');
var digital = document.getElementById('digital');

politics.addEventListener('click', function(){
    fetchUrl = urlPolitics;
    getArticle(fetchUrl);
});
economic.addEventListener('click', function(){
    fetchUrl = urlEconomic;
    getArticle(fetchUrl);
});
society.addEventListener('click', function(){
    fetchUrl = urlSociety;
    getArticle(fetchUrl);
});
culture.addEventListener('click', function(){
    fetchUrl = urlCulture;
    getArticle(fetchUrl);
});
foreign.addEventListener('click', function(){
    fetchUrl = urlForeign;
    getArticle(fetchUrl);
});
digital.addEventListener('click', function(){
    fetchUrl = urlDigital;
    getArticle(fetchUrl);
});

getArticle(urlMain);
console.log('aaa');