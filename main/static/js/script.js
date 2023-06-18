const carousel = document.querySelector(".my_carousel");    
const body = document.querySelector("body");
const firstCardWidth = carousel.querySelector(".my_card").offsetWidth;
const carousel_children = [...carousel.children];


let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);  // Ekrandaki maksimum kart sayısı

carousel_children.slice(-cardPerView).reverse().forEach(card => {   // Karoselin başına sondan ekleme
    carousel.insertAdjacentHTML("afterBegin",card.outerHTML)
});

carousel_children.slice(0, cardPerView).forEach(card => {           // Sona baştan ekleme
    carousel.insertAdjacentHTML("beforeEnd",card.outerHTML)
});

const infiniteScroll = () => {
    if(carousel.scrollLeft === 0){
        carousel.classList.add("no-transition")
        carousel.scrollLeft = carousel.scrollWidth - ( 2 * carousel.offsetWidth)
        carousel.classList.remove("no-transition")
    }
    else if(Math.ceil(carousel.scrollLeft) === carousel.scrollWidth - carousel.offsetWidth) {
        carousel.classList.add("no-transition")
        carousel.scrollLeft = carousel.offsetWidth
        carousel.classList.remove("no-transition")
    }
}

carousel.addEventListener("scroll", infiniteScroll)

setInterval(
    function slide() {
        console.log(carousel.scrollLeft);
        carousel.scrollLeft += firstCardWidth;
      },
    2000
  );
