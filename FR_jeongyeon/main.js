    //팝업창 제거, 생성 JS
    
    const popupLayer = document.querySelector('.popup');
    const openPopup = document.querySelector('.show-article');
    const hide = "hide";

    const openPopuptitle = document.querySelector('.title');
    const btnClose1 = document.querySelector(".btn-close");
    const btnClose2 = document.querySelector(".btn-close");

    openPopuptitle.addEventListener('click', ()=>{
        onElements();
    });
    openPopup.addEventListener('click', ()=>{
        onElements();
    });
    btnClose1.addEventListener('click',()=>{
        closePopup();
    });
    btnClose2.addEventListener('click',()=>{
        closePopup();
    });

    function onElements(){
        popupLayer.classList.remove(hide);
    }

    function closePopup(){
        popupLayer.classList.add('hide');
    }
    

    

    


    // hide클래스 추가
    // function onElements(){
    //     [].forEach.call($popupLayer, function(e){
    //         popup.classList.remove('hide');
    //     });
    // };

    // //hide클래스 제거
    // function offElements(){
    //     [].forEach.call($popupLayer, function(e){
    //         popup.classList.add('hide');
    //     });
    // }

    // hide클래스 제거


