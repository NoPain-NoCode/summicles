// /* SWIPER */


const slide = new Swiper('.swiper-container', {
    // 다양한 옵션 설정, 
    // 아래에서 설명하는 옵션들은 해당 위치에 들어갑니다!!
    direction: 'horizontal',
    slidesPerView :7,
    spaceBetween: -200,  

    breakpoints : {
      300: {
        
        slidesPerView : 4,
        spaceBetween : 10,
      },
      784: {
        slidesPerView :7,
        spaceBetween: -200,  
      }
    }
    
  })
