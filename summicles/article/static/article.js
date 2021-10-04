// 기사를 가져오는 JS
const clickMain = document.querySelector('#main');
const clickPolitics= document.querySelector('#politics');
const clickEconomic= document.querySelector('#economic');
const clickSociety= document.querySelector('#society');
const clickCulture= document.querySelector('#culture');
const clickForeign= document.querySelector('#foreign');
const clickDigital= document.querySelector('#digital');

const urlMain = 'http://dylee.pythonanywhere.com/summicles/';
const urlPolitics = 'http://dylee.pythonanywhere.com/summicles/politics/';
const urlEconomic = 'http://dylee.pythonanywhere.com/summicles/economic/';
const urlSociety = 'http://dylee.pythonanywhere.com/summicles/society/';
const urlCulture = 'http://dylee.pythonanywhere.com/summicles/culture/';
const urlForeign = 'http://dylee.pythonanywhere.com/summicles/foreign/';
const urlDigital = 'http://dylee.pythonanywhere.com/summicles/digital/';
const urlSearch = 'http://dylee.pythonanywhere.com/summicles/?search=';

const ex_article = document.querySelector('.ex--article');
const popupList = document.querySelector(".popup-list");



function getArticle () {
    if (ex_article.hasChildNodes() && popupList.hasChildNodes()){
        ex_article.removeChild();
        popupList.removeChild();
    }
    fetch(urlMain,{
        method: 'GET',
        
    }).then(response => response.json())
    .then(response =>{
        let ul
        for(let i=0; i<response.length; i++){
            const {title, img, article_date, newspaper,contents,link,category,headline} = response[i];
            
            if(i%5 === 0){
                ul = document.createElement('ul');
                // ul.setAttribute('class', 'article-bundle');
            }
            if(img===null){
                ul.innerHTML += `
                    <li>
                        <img class="show-article img_here img-article" src="./img/null_article_img.png">
                        <div class="article-group article_here">
                            <a class="title title_here">${title}</a>
                            <p class="headline-here">${headline}</p>
                            <p class="tag-here">${category}</p>
                            <div class="date-and-newspaper">
                                <p class="date_here">${article_date}</p>
                                <p>${newspaper}</p>
                            </div>
                            
                        </div>
                    </li>
                `;

                popupList.innerHTML += `
                <div class="popup hide">
                    <div class="modal-content">
                        <div class="modal-header">
                            <div class="magazine-wrap">
                                <div class="magazine modal-magazine-here">${newspaper}</div>
                                <button class="btn-close1 close-img"><i class="fas fa-times"></i></button>
                            </div>
                            <h3 class="title madal-title-here">${title}</h3>
                            <div class="original-wrap">
                                <button type="button" onclick="location.href = '${link}'">기사원문</button>
                                <p>#태그#태그#태그#태그</p>
                            </div>
                        </div>
                    <div class="modal-body">
                        <img class="modal-img-here"  src="./img/null_article_img.png" alt="pic">
                        <p class="modal-article-here">${contents}</p>
                    </div>
                    <div class="modal-footer clearfix">
                        <button class="btn-close2 float--right">닫기</button>
                    </div>
                </div>

                <div class="popup_dimmed"></div>
                </div>
                `;
            }
            else{
                ul.innerHTML += `
                    <li>
                        <img class="show-article img_here img-article" src="${img}">
                        <div class="article-group article_here">
                            <a class="title title_here">${title}</a>
                            <p class="headline-here">${headline}</p>
                            <p class="tag-here">${category}</p>
                            <p class="date_here">${article_date}</p>
                            <p>${newspaper}</p>
                        </div>
                    </li>
                `; 

                popupList.innerHTML += `
                <div class="popup hide">
                    <div class="modal-content">
                        <div class="modal-header">
                            <div class="magazine-wrap">
                                <div class="magazine modal-magazine-here">${newspaper}</div>
                                <button class="btn-close1 close-img"><i class="fas fa-times"></i></button>
                            </div>
                            <h3 class="title madal-title-here">${title}</h3>
                            <div class="original-wrap">
                                <button type="button" onclick="location.href = '${link}'">기사원문</button>
                                <p>#태그#태그#태그#태그</p>
                            </div>
                        </div>
                    <div class="modal-body">
                        <img class="modal-img-here"  src="${img}" alt="pic">
                        <p class="modal-article-here">${contents}</p>
                    </div>
                    <div class="modal-footer clearfix">
                        <button class="btn-close2 float--right">닫기</button>
                    </div>
                </div>

                <div class="popup_dimmed"></div>
                </div>
                `;
            }
            
            ex_article.appendChild(ul);
            
        }

    const popupLayer = document.querySelectorAll('.popup');
    const openPopup = document.querySelectorAll('.img-article');

    const openPopuptitle = document.querySelectorAll('.title');
    const btnClose1 = document.querySelectorAll(".btn-close1");
    const btnClose2 = document.querySelectorAll(".btn-close2");
        
    getPopup(popupLayer,openPopup,openPopuptitle,btnClose1,btnClose2);
    
    })
}


function getPopup(popupLayer,openPopup,openPopuptitle,btnClose1,btnClose2){
    for(let i=0; i<=popupLayer.length; i++){
        openPopuptitle[i].addEventListener('click', ()=>{
            onElements(popupLayer[i]);
        });
        openPopup[i].addEventListener('click', ()=>{
            onElements(popupLayer[i]);
        });
        btnClose1[i].addEventListener('click',()=>{
            closePopup(popupLayer[i]);
        });
        btnClose2[i].addEventListener('click',()=>{
            closePopup(popupLayer[i]);
        });
    }
}

function onElements(element){
    element.classList.remove('hide');
}

function closePopup(element){
    element.classList.add('hide');
}

getArticle();



function changeTopic(){
    clickPolitics.addEventListener('click',()=>{
        ex_article.removeChild();
        popupList.removeChild();
    });
    clickEconomic.addEventListener('click',()=>{
        getEconomicArticle()
    });
    clickSociety.addEventListener('click',()=>{
        getSocietyArticle()
    });
    clickCulture.addEventListener('click',()=>{
        getCultureArticle()
    });
    clickForeign.addEventListener('click',()=>{
        getForeignArticle()
    });
    clickDigital.addEventListener('click',()=>{
        getDigitalArticle()
    });
}
changeTopic();


