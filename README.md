# fineFoodsReviews
A simple search engine to search reviews for keywords

Prerequisites:
  - Libraries: nltk, flask

Steps to run code locally:
 - clone the repo
 - run query_server.py: `python query_server.py`
 
Sample URL for testing on local: 
 - `http://127.0.0.1:5000/good-taffy`
 
    Output(partial):
 
    `[
  {
    "product/productId": " B0007OVWLU", 
    "review/helpfulness": " 3/3", 
    "review/profileName": " Jim Hudson \"Captain Hudson\"", 
    "review/score": " 5.0", 
    "review/summary": " Just as I remembered", 
    "review/text": " This product is exactly as I remember it as an adolescent in the 70's. Once you get past the first couple of pieces, you will find different flavors for each color, red and white for Cherry, purple and white for grape, and yellow and white for banana.  Other color combinations have different flavors, some hard to identify but all good.  If the weather is a bit warm, the wax paper can be a little hard to separate from the taffy.  Quick Fix - stick them in the refrigerator for a two minutes and the paper will come off easily.  Makes a great treat for kids.  Adults, watch out for the expensive dental work. This taffy is the real stuff.  Enjoy!", 
    "review/time": " 1247097600", 
    "review/userId": " A3BLQEPBH0XB1A"
  }, 
  {
    "product/productId": " B000FNB7UY", 
    "review/helpfulness": " 0/0", 
    "review/profileName": " ilmq5210", 
    "review/score": " 4.0", 
    "review/summary": " same taste same quality", 
    "review/text": " This yummy banana chewy candy is a great sweet tooth satisfier. I remember this candy back in the days of my childhood years, It tastes just as good now as it did growing up. I recommend this candy for anyone that loves a sweet banana flavored chewy candy.<br />I must say it's better than Laffy Taffy!!!!", 
    "review/time": " 1328832000", 
    "review/userId": " A1XMESDTSSRZHJ"
  }
  ]`
