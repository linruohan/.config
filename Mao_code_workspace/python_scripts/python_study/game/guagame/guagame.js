var GuaGame=function(fps,images,runCallback){
  //images是一个字典，里面是图片的引用名字和路径
  //程序会在载完所有图片后运行
  var g={
    actions:{},
    keydowns:{},
    images:{},
  }
  var canvas=document.querySelector('#id-canvas')
  var context=canvas.getContext('2d')
  g.canvas=canvas
  g.context=context
  g.drawImage=function(guaImage){
    g.context.drawImage(guaImage.image,guaImage.x,guaImage.y)
  }
  //events
  window.addEventListener('keydown',function(){
    g.keydowns[event.key]=true
  })
  window.addEventListener('keyup',function(){
    g.keydowns[event.key]=false
  })
  //
  g.registerAction=function(key,callback){
    g.actions[key]=callback
  }

  //定时器timer
  window.fps=30
  var runloop=function(){
    var actions=Object.keys(g.actions)
    for(var i=0;i<actions.length;i++){
      var key=actions[i]
      if(g.keydowns[key]){
        //如果按键被按下，调用被注册的action
        g.actions[key]()
        }
      }
    //update
    g.update()
    //clear
    context.clearRect(0,0,canvas.width,canvas.height)
    //draw
    g.draw()
    // next run loop
    setTimeout(function(){
      runloop()
    },1000/fps)
  }
  //预先载入所有图片
  var loads=[]
  var names=Object.keys(images)
  for (var i = 0; i < names.length; i++) {
    let name=names[i]
    var path=images[name]
    let img=new Image()
    img.src=path
    img.onload=function(){
      //存入g.images 中
      g.images[name]=img
      //所有图片都载入成功后，调用run
      loads.push(1)
      log('载入图片')
      if (loads.length==names.length) {
        g.run()
      }
    }
  }


  g.imageByName=function(name){
    log('image:',g.images)
    var img=g.images[name]
    var image={
      w:img.width,
      h:img.height,
      image:img
    }
    return image
  }

  g.run=function(){
    runCallback(g)
    // 开始运行程序
    setTimeout(function(){
      runloop()
    },1000/fps)
  }


  return g
}
