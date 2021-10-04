// 네비게이터 이동 색 변환 JS

const mainMenu = document.querySelector('#topic-menu>li:nth-child(1)');
const politics = document.querySelector('#topic-menu>li:nth-child(2)');
const economi= document.querySelector('#topic-menu>li:nth-child(3)');
const society = document.querySelector('#topic-menu>li:nth-child(4)');
const culture = document.querySelector('#topic-menu>li:nth-child(5)');
const international = document.querySelector('#topic-menu>li:nth-child(6)');
const science = document.querySelector('#topic-menu>li:nth-child(7)');
//메뉴 요소를 리스트에 담음. 

const menuSelectList = [mainMenu, politics, economi, society, culture, international, science];
//각 메뉴 클릭 시 addOntoMenu 함수 호출
menuSelectList.forEach(menu=>{
    menu.addEventListener('click', ()=>{
        addOntoMenu(menu);
    })
})
//클릭된 menu 요소 제외 나머지 모두 on class제거. 클릭한 클래스에만 on 추가.
function addOntoMenu(menu){
    menu.classList.add('on');
    for(let i=0; i<menuSelectList.length; i++){
        if(menuSelectList[i]===menu) continue;
        menuSelectList[i].classList.remove('on');
    }
}








