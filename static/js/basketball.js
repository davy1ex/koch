function search() {
    url = "https://geocode-maps.yandex.ru/1.x/?apikey=6e5bb8b0-59fd-4ea5-898d-f909933a59da&format=json&results=5&kind=Address&geocode=Тверская+6"
    // var request = new Request(url);
    // // console.log(request.json)
    // request.body.json().then(function(data){
    //     console.log(data)
    // })
    
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(JSON.parse(xmlHttp.responseText)["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]);
    
}
