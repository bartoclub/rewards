var msnShoppingGamePane = document.querySelector("shopping-page-base")
    ?.shadowRoot.querySelector("shopping-homepage")
    ?.shadowRoot.querySelector("msft-feed-layout")
    ?.shadowRoot.querySelector("msn-shopping-game-pane");
 
if(msnShoppingGamePane != null){
    msnShoppingGamePane.scrollIntoView();
    msnShoppingGamePane.cardsPerGame = 1;
	console.log(msnShoppingGamePane)
	try {
		msnShoppingGamePane.resetGame();
	} catch {
		console.log("cant reset game");
	}
}
else alert("Unable to locate the shopping game!");

function removeBlur(){
	try {
		document.querySelector("shopping-modal[blurprice]").removeAttribute("blurprice")
	} catch {
	}
}

setInterval(removeBlur, 500);
