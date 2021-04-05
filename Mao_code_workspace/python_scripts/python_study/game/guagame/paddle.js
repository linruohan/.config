var Paddle=function(game){
  var o=game.imageByName('paddle')
  // var o={
  //   image:image,
  //   x:100,
  //   y:200,
  //   speed:15,
  //
  // }
  o.x=100
  o.y=250
  o.speed=15

  var paddle=o
  o.move=function(x){
    if (x<0) {
      x=0
    }
    if (x>400-o.image.width) {
      x=400-o.image.width
    }
    o.x=x
  }
  o.move1=function(y){
    if (y<0) {
      y=0
    }
    if (y>300-o.image.height) {
      y=300-o.image.height
    }
    o.y=y
  }
  o.moveLeft=function(){
    o.move(paddle.x-paddle.speed)
  }
  o.moveRight=function(){
    o.move(paddle.x+paddle.speed)
  }
  o.moveForward=function(){
    o.move1(paddle.y-paddle.speed)
  }
  o.moveBack=function(){
    o.move1(paddle.y+paddle.speed)
  }
  o.collide=function(ball){
    if (ball.y+ball.image.height>o.y) {
      if(ball.x>0 && ball.x<(o.x+o.image.width)){
        return true
      }
    return false
    }
  }
  return o
}
