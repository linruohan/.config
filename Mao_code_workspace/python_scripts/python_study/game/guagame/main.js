
var loadLevel=function(game,n){
  n=n-1
  var level=levels[n]
  var blocks=[]
  for (var i=0;i<level.length; i++) {
    var p=level[i]
    var b=Block(game,p)
    blocks.push(b)
  }
  return blocks
}

var enableDebugMode=function(game,enable){
  if (!enable) {
    return
  }
  window.addEventListener('keydown',function(event){
    var k=event.key
    if (k=='p') {
      //暂停功能
      paused=!paused
    }else if('1234567'.includes(k)){
      // 载入关卡功能
      blocks=loadLevel(game,k)
    }
  })
}

//主函数————————****入口****
var __main=function(){

  var images={
    ball:'ball.png',
    block:'block.png',
    paddle:'paddle.png',
  }
  var game=GuaGame(30,images)
  enableDebugMode(game,true)
  var paddle=Paddle(game)
  var ball=Ball(game)

  var score=0

  blocks=loadLevel(game,1)

  var paused=false
  game.registerAction('a',function(){
    paddle.moveLeft()
  })
  game.registerAction('d',function(){
    paddle.moveRight()
  })
  game.registerAction('w',function(){
    paddle.moveForward()
  })
  game.registerAction('s',function(){
    paddle.moveBack()
  })
  game.registerAction('f',function(){
    ball.fire()
  })



  game.update=function(){
    if(paused){
      return
    }
    // log(update)
    ball.move()
    //判断ball和paddle相撞
    if(paddle.collide(ball)) {
      // 这里应该用一个ball.反弹（）实现
      ball.fantan()
    }
    // 判断ball和blocks相撞
    for (var i = 0; i < blocks.length; i++) {
      var block=blocks[i]
      if(block.collide(ball)) {
        log('block相撞')
        block.kill()
        ball.fantan()
        score+=100//得分
      }
    }
  }
  game.draw=function(){
    game.drawImage(paddle)
    game.drawImage(ball)
    for (var i = 0; i < blocks.length; i++) {
      var block=blocks[i]
      if (block.alive) {
        game.drawImage(block)
      }
    }
    //draw lables
    game.context.fillText('分数：'+score,20,290)
  }





__main()
