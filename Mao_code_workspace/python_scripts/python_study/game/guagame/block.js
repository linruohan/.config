var Block=function(game,position){
  //position是[0,0]格式
  var p=position

  var img=imageByName('block')
  var o={
    x:p[0],
    y:p[1],
    alive:true,
    lifes:p[2]||1,
  }
  o.image=img.image
  o.w=img.w
  o.h=img.h
  o.kill=function(){
    o.lifes--
    if (o.lifes<1) {
      o.alive=false
    }
  }
  o.collide=function(b){
    return o.alive&&(ainb(o,b) || ainb(b,o))
  }
  return o
}
