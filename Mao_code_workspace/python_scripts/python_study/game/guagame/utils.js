var e=sel=>document.querySelector(sel)
var log=function(s){
  e('#id-text-log').value+='\n'+s
}


var imageFromPath=function (path) {
  var img=new Image()
  img.src=path
  return img
}

var ainb=function(a,b){
  var o=a
  if (b.y>o.y &&b.y<o.image.height+o.y) {
    if(b.x>o.x && b.x<o.x+o.image.width){
      // log('相撞')
      return true
    }
    return false
  }
}
