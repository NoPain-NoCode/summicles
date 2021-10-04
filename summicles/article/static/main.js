const goMain = document.querySelector("#main");
const goPolitics = document.querySelector("#politics");
const goEconomic = document.querySelector("#economic");
const goSociety = document.querySelector("#society");
const goCulture = document.querySelector("#culture");
const goForeign = document.querySelector("#foreign")
const goDigital = document.querySelector("#digital");
//카테고리 클릭 시 해당 카테고리 기사들로 이동. 
//초기값은 main으로 설정. 
let moveUrl = 'http://dylee.pythonanywhere.com/api/';
const urlMain = 'http://dylee.pythonanywhere.com/api/';
const urlPolitics = 'http://dylee.pythonanywhere.com/api/politics/';
const urlEconomic = 'http://dylee.pythonanywhere.com/api/economic/';
const urlSociety = 'http://dylee.pythonanywhere.com/api/society/';
const urlCulture = 'http://dylee.pythonanywhere.com/api/culture/';
const urlForeign = 'http://dylee.pythonanywhere.com/api/foreign/';
const urlDigital = 'http://dylee.pythonanywhere.com/api/digital/';
const urlSearch = 'http://dylee.pythonanywhere.com/api/?search=';

const inputSearch = document.querySelector('#search');
const searchNum = document.querySelector('.search-number');
const searchKeyword = document.querySelector('.search-keyword');
const articleDateHere = document.querySelector('.article-date-here');

const ex_article = document.querySelector('.ex--article');
const popupList = document.querySelector(".popup-list");
const popup = document.querySelectorAll('.popup');

inputSearch.addEventListener('keydown',(e)=>{
    if(e.keyCode === 13){
        let searchValue = inputSearch.value;
        moveUrl = urlSearch + searchValue;
        searchKeyword.classList.remove('hide');
        searchKeyword.innerHTML = `<p><strong>\" ${searchValue} \"</strong> 의 검색 결과 입니다.</p>`;
        getArticle(moveUrl);
        
    }
})

    goMain.addEventListener('click',()=>{
        moveUrl = urlMain;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goPolitics.addEventListener('click',()=>{
        moveUrl = urlPolitics;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goEconomic.addEventListener('click',()=>{
        moveUrl = urlEconomic;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goSociety.addEventListener('click',()=>{
        moveUrl = urlSociety;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goCulture.addEventListener('click',()=>{
        moveUrl = urlCulture;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goForeign.addEventListener('click',()=>{
        moveUrl = urlForeign;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    goDigital.addEventListener('click',()=>{
        moveUrl = urlDigital;
        searchKeyword.classList.add('hide');
        getArticle(moveUrl);
    })
    


function getArticle(fetchUrl){
        while(ex_article.firstChild){
            ex_article.removeChild(ex_article.firstChild);
        }
        while(popupList.firstChild){
            popupList.removeChild(popupList.firstChild);
        }
    
    fetch(fetchUrl,{
        method: 'GET',
        
    }).then(response => response.json())
    .then(response =>{
        let ul
        for(let i=0; i<response.length; i++){
            const {title, img, article_date, newspaper,contents,link,category,headline} = response[i];
            
            if(i%5 === 0){
                ul = document.createElement('ul');
                ul.setAttribute('class', 'clearfix');
            }
            if(img===null){
                ul.innerHTML += `
                    <li>
                        <img class="show-article img_here img-article" src=null_article_img>
                        <div class="article-group article_here">
                            <a class="title title_here">${title}</a>
                            <p class="headline-here">${headline}</p>
                            <div class="date-and-newspaper">
                                <p class="tag-here">#${category}</p>
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
                                <p>${article_date}</p>
                                <p>#${category}</p>
                            </div>
                        </div>
                    <div class="modal-body">
                        <img class="modal-img-here"  src=null_article_img alt="pic">
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
                        <img class="show-article img_here img-article" src="${img}" onerror="this.src=null_article_img">
                        <div class="article-group article_here">
                            <a class="title title_here">${title}</a>
                            <p class="headline-here">${headline}</p>
                            
                            <div class="date-and-newspaper">
                                <p class="tag-here">#${category}</p>
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
                            <div class="info-wrap">
                                <div class="original-wrap">
                                    <button type="button" onclick="location.href = '${link}'">기사원문</button>
                                    <p>${article_date}</p>
                                </div>
                                <p>#${category}</p>
                            </div>
                        </div>
                    <div class="modal-body">
                        <img class="modal-img-here"  src="${img}" alt="pic" onerror="this.src=null_article_img">
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
            searchNum.innerHTML = '총 ' + response.length + '개의 기사';
            
            articleDateHere.innerHTML = response[0].article_date+' ~ '+response[response.length-1].article_date + ' 기준';
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

getArticle(urlMain);

