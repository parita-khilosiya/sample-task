function reloadData(){
    url = "/getdata"
    $.ajax({
        url: url,
        type: 'GET',
        
        success: function(data) {
          console.log(data)
          displayCards(data)
        }.bind(this),
        error: function(xhr, status, err) {
          console.log( err.toString()          );
        }
    });
}
reloadData()
setInterval(reloadData, 300000)

imgs = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.png", "image6.jpg", "image7.jpg", "image8.jpg", "image9.jpg", "image10.jpg"]

function displayCards(data){
    dataArr = data.data
    timeDiv = document.getElementById("syncTime")
    timeDiv.innerHTML = data.lasupdatedtime.toString()

    contendDiv = document.getElementById("content")
    contendDiv.innerHTML = ""
    for (var i = 0; i < dataArr.length; i++){
        tempDiv = document.createElement("div")
        tempDiv.className = "cardBox"

        tempDiv.innerHTML = "<div class='title'>"+dataArr[i].symbol+"</div>"+
                            "<div class='card-left'>"+
                            "<div class='items'> Open : "+dataArr[i].openPrice+"</div>"+
                            "<div class='items'> High : "+dataArr[i].highPrice+"</div>"+
                            "<div class='items'> Low : "+dataArr[i].lowPrice+"</div>"+
                            "</div>"+
                            "<div class='card-img'> <img height='100px' width='60px' src='static/images/"+(i >= imgs.length? img[0]:imgs[i]) +"'> </div>"+
                            "<div class='detail-btn' onclick='showDetails(dataArr["+i+"])'>Show Details</div>"
        contendDiv.appendChild(tempDiv);
    }
}
function showDetails(obj){
  
    popupDiv = document.createElement("div")
    popupDiv.className = "popup-container"
    popupDiv.id = "popup-div"
    popupDiv.innerHTML = '<div class="light-views-background" style="position:absolute;top:0;left:0;height:100%;width:100%;opacity:.5;background-color:#000;"></div>'+
                        "<div class='popup-content'>"+
                        "<div class='close-btn' onclick='closeDetail()'><img height=30px; width=30px; src='/static/images/close_button.png'></div>"+
                        "<table class='popup-table'>"+
                        "<tr> <td> Symbol </td><td>"+obj.symbol+"</td></tr>"+
                        "<tr> <td> LTP </td><td>"+obj.ltp+"</td></tr>"+
                        "<tr> <td> % Change </td><td>"+obj.netPrice+"</td></tr>"+
                        "<tr> <td> Traded Quantity </td><td>"+obj.tradedQuantity+"</td></tr>"+
                        "<tr> <td> Value (in Lakhs) </td><td>"+obj.turnoverInLakhs+"</td></tr>"+
                        "<tr> <td> open Price </td><td>"+obj.openPrice+"</td></tr>"+
                        "<tr> <td> High Price </td><td>"+obj.highPrice+"</td></tr>"+
                        "<tr> <td> Low Price </td><td>"+obj.lowPrice+"</td></tr>"+
                        "<tr> <td> Previous Price </td><td>"+obj.previousPrice+"</td></tr>"+
                        "<tr> <td> Latest Ex Date  </td><td>"+obj.lastCorpAnnouncementDate+"</td></tr>"+                        
                        "</table>"+
                        "</div>"
    document.body.appendChild(popupDiv)
    console.log(obj.symbol)
}
function closeDetail(){
    divObj = document.getElementById("popup-div")
    document.body.removeChild(divObj)
}