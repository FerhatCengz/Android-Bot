const indexArray = $(".followButton .app-center-vertical");
let sayac = 5;
let scrollDownYediyuz = 700;

setInterval(() => {
  if (indexArray[sayac].textContent != "Takibi Bırak") {
    for (let i = sayac; i < sayac + 8; i++) {
      indexArray[sayac].click();
    //   window.scroll(1000, scrollDownYediyuz);
    //   scrollDownYediyuz += 100;
    }
    sayac += 8;
  }
}, 500);
