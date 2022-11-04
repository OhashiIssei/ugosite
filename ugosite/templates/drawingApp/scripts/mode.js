const modeRadio = document.querySelectorAll('#mode-change label');

const modeKeys =  ["w","s","e","a","g","b",]
for(let i=0;i<modeRadio.length;i++){
  modeRadio[i].textContent += " ("+modeKeys[i].charAt(0).toUpperCase()+")"
}

window.addEventListener("keydown",function(e){
  if(pressed){
    console.log("描画中はコマンド無効")
  }else{
    console.log(e.modeKey)
    for(let i=0;i<modeRadio.length;i++){
      if(e.key===modeKeys[i]){
        decribeToPage()
        changeToMode(modeRadio[i].getAttribute("id"))
        break
      }
    }
  }
})




let mode = "write"

changeToMode(mode)

//modeの切り替え関数
function changeToMode(m){
  mode = m
  for(let i=0;i<modeRadio.length;i++){
    modeRadio[i].setAttribute("status","off")
    }
  switch(m){
    case "write":
      modeRadio[0].setAttribute("status","on")
      break
    case "shape":
    case "line":
    case "ellipse":
    case "curve":
      modeRadio[1].setAttribute("status","on")
      break
    case "erase":
      modeRadio[2].setAttribute("status","on")
      break
    case "select":
    case "selected":
    case "transform":
      modeRadio[3].setAttribute("status","on")
      break
    case "graph":
      modeRadio[4].setAttribute("status","on")
      break
    case "ball":
      modeRadio[5].setAttribute("status","on")
      break
  }
  // layers.setAttribute("class",m)
  console.log(m+"にしました")
}

//ボタンをクリックしてモード切り替え
for(let i=0;i<modeRadio.length;i++){
    modeRadio[i].addEventListener("click",setMode)
  }

//ボタン以外でも切り替えられるように関数を定義
function setMode(e){
  uiClear()
  decribeToPage()
  changeToMode(e.target.getAttribute("id"))
}


// ||マウス座標データの蓄積

// function addStrokeP(e){
//   curX = (window.Event) ? e.pageX : e.clientX + (document.documentElement.scrollLeft ? document.documentElement.scrollLeft : document.body.scrollLeft);
//   curY = (window.Event) ? e.pageY : e.clientY + (document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop);
// }

//グローバルな可変変数

let path
let eraser
let pressed = false

let inP = new DOMPoint()
let outP = new DOMPoint()

let dx = 0
let dy = 0

let deleteCount

let timer1

let center = new DOMPoint()
let id = 1


// || 'pointerdown'の振る舞い
layers.addEventListener('pointerdown', writeStart)

function writeStart(e){
  e.preventDefault();
  pressed = true
  inP = e
  switch(mode){
  case "shape":
    timer1 = setTimeout(()=>{
      changeToMode("select")
      selectStart(e)
      },500)

  case "write":
    path = document.createElementNS(SVG_URL,"path")
    selected.appendChild(path)
    path.setAttributeNS(null,"id","write"+id);id++
    path.setAttributeNS(null,"style",`stroke:${penColor};stroke-width:${penSize};fill-opacity:0`)
    path.setAttributeNS(null,"d","M "+e.x+" "+e.y)
    pastP = e
    break

  case "ball":
    path = document.createElementNS(SVG_URL,"path")
    ui.appendChild(path)
    path.setAttributeNS(null,"style",`stroke:${penColor};stroke-width:${penSize/4};`)
    path.setAttributeNS(null,"d","M "+e.x+" "+e.y)
    break

  case "erase":
    eraser = document.createElementNS(SVG_URL,"circle")
    eraser.setAttributeNS(null,"id","eraser")
    ui.appendChild(eraser)
    erase(e)
    eraser.setAttributeNS(null,"cx",e.x)
    eraser.setAttributeNS(null,"cy",e.y)
    eraser.setAttributeNS(null,"r",eraserSize/2)
    eraser.setAttributeNS(null,"fill","white")
    break

  case "select":
    selectStart(e)
    break

  case "selected":
    if(path.isPointInFill(e)){
    }else{
      changeToMode("select")
      selectStart(e)
    }
    break
  }
  console.log(
    back.childElementCount+", "
   +currentPage.childElementCount+", "
   +selected.childElementCount+", "
   +ui.childElementCount+", "
   +mode+", "+operate+"で描き始め")
};


function selectStart(e){
  decribeToPage()
  uiClear()
  path = document.createElementNS(SVG_URL,"path")
  ui.appendChild(path)
  path.setAttributeNS(null,"style",`fill:blue; fill-opacity:0.1`)
  path.setAttributeNS(null,"d","M "+e.x+" "+e.y)
  selected.transformCash = ""
  console.log("selected.transformCashをリセット")
}

// Shape検出のルール

function changeToShape(e) {
  const d = distance(inP,e)
  const box = path.getBoundingClientRect()
  w = box.width
  h = box.height
  s = Math.sqrt(w**2+h**2)
  center = path.clientCenter()
  // console.log(d+","+w+","+h+","+s)
  switch(true){
    case d/s>0.9://直線
      id--
      path.setAttributeNS(null,"id","line"+id);id++
      path.setAttributeNS(null,"style",`stroke:${penColor};stroke-width:${penSize};fill-opacity:0`)
      path.setAttributeNS(null,"d",`M ${inP.x} ${inP.y} L ${e.x} ${e.y}`)
      changeToMode("line");
      console.log(path.id+"に変形しました")
      break;

    case d/s<0.3:
      let rx; let ry
      if(Math.abs(w/h-1)<0.25){
        rx=ry=(w+h)/4//円
      }else{
        rx=w/2; ry=h/2//楕円
      }
      id--
      path.setAttributeNS(null,"id","eliips"+id);id++
      path.setAttributeNS(null,"style",`stroke:${penColor};stroke-width:${penSize};fill-opacity:0`)
      path.setAttributeNS(null,"d",`M ${center.x+rx} ${center.y}`)
      const n = Math.max(rx,ry)
      for(let i=0;i<n;i++){
        path.setAttributeNS(null,"d",path.getAttributeNS(null,"d")+` A ${rx} ${ry} 0 0 0 ${center.x+rx*Math.cos(degToRad(i/n*360))} ${center.y+ry*Math.sin(degToRad(i/n*360))}`)
      }
      changeToMode("ellipse");
      selected.transformStart(e,"translate")
      console.log(path.id+"に変形しました")
      break;

    case inP.y<box.y+h/10||e.y<box.y+h/10://放物線
      id--
      path.setAttributeNS(null,"id","curve"+id);id++
      const m = midPoint(inP,e)
      const points = path.getPoints()
      let i = 1
      while(points[i].x<m.x){i++}
      const r = midPoint(points[i-1],points[i])//x座標が中央付近にある点rをとる
      const c = symmetryPointAbout(r,m)
      path.setAttributeNS(null,"d",`M ${inP.x} ${inP.y} Q ${c.x} ${c.y} ${e.x} ${e.y}`)
      changeToMode("curve");
      selected.transformStart(e,"translate")
      console.log(path.id+"に変形しました")
  }
}


Event.prototype.pastP = function(){
  return new DOMPoint(this.x-this.movementX,this.y-this.movementY)
}


// || 'pointermove'の振る舞い
layers.addEventListener('pointermove', writting)

function writting(e){
  e.preventDefault();
  if(pressed){
    console.log(mode+"で書いている")
    switch(mode){
    case "shape":
      clearTimeout(timer1)
      timer1 = setTimeout(()=>{changeToShape(e)},200)

    case "write":
      const midP = midPoint(e.pastP() ,e)
      path.setAttributeNS(null,"d",`${path.getAttributeNS(null,"d")} Q ${pastP.x} ${pastP.y} ${midP.x} ${midP.y}`)
      pastP = e
      break
      
    case "line"://ShapeModeに移行したい
      outP.x = crrection(e)[0]
      outP.y = crrection(e)[1]
      path.setAttributeNS(null,"d",`M ${inP.x} ${inP.y} L ${outP.x} ${outP.y}`)
      break
    
    case "ball":
      path.setAttributeNS(null,"d",`M ${inP.x} ${inP.y} L ${e.x} ${e.y}`)//lineのみ(いづれ球も描きたい)
      break

    case "erase":
      eraser.setAttributeNS(null,"cx",e.x)
      eraser.setAttributeNS(null,"cy",e.y)
      erase(e)//arcに触れるcurrentPagePvgのpathを削除する。
      break

    case "select":
      path.setAttributeNS(null,"d",`${path.getAttributeNS(null,"d")} L ${e.x} ${e.y}`)
      break
    
    case "selected":
      if(distance(e,inP)>=5&&!operate){
        active.transformStart(e,"translate")
      }
      break

    case "transform":
      if(!operate){
        uiClear()//fransformUIのうちの何にも触れていない場合はselectに逆戻り
        decribeToPage()
      }
      break
  
    case "graph":
      if(!operate){
        uiClear()//fransformUIのうちの何にも触れていない場合はselectに逆戻り
        decribeToPage()
      }
      break
    }
  }
};

let selectLineWidth = 2
let axisLines = []

// || 'pointerup'の振る舞い
layers.addEventListener('pointerup', writeEnd)

function writeEnd(e){
  e.preventDefault();
  pressed = false
  dx = e.x - inP.x 
  dy = e.y - inP.y
  console.log(mode+"で描きおわる")
  switch(mode){
  case "shape":  
  case "write":
    clearTimeout(timer1)
    currentPage.appendChild(path)
    console.log(path.id+"を確定しました")
    break;
    
  case "line":
    if(distance(e,inP)!==0){
      outP.x = crrection(e)[0]
      outP.y = crrection(e)[1]
      path.setToLine(inP,outP)
      currentPage.appendChild(path)
      console.log(path.id+"を確定しました")
      checkAxisLines()
    }
  case "ellipse":
  case "curve":
    // path.SVGmatrixTransform(new DOMMatrix().translate(e.x-inP.x ,e.y-inP.y))//これはまだ無理
    changeToMode("shape")
    console.log(path.id+"を確定しました")
    break;

  case "ball":
    createBall(e.x,e.y,(inP.x-e.x)/10,(inP.y-e.y)/10,penColor,penSize/2)
    uiClear()
    break

  case "erase":
    if(deleteCount===0){
      changeToMode("write")
    }else{
      deleteCount=0
    }
    ui.removeChild(eraser)
    break

  case "select":
    path.setAttributeNS(null,"d",`${path.getAttributeNS(null,"d")} Z`)
    select(path)
    if(selected.childElementCount>0){
      changeToMode("selected")
    }else{
      uiClear()
      decribeToPage()
      changeToMode("write")
    }
    break

  case "selected"://実際にはtranlateの可能性しかない。
    if(!operate){
      console.log("一旦UIを消します")
      changeToMode("transform")
      uiClear()
      createTransformUi() 
    }
  break

  case "transform":
    if(!operate){
      uiClear()//fransformUIのうちの何にも触れていない場合はselectに逆戻り
      decribeToPage()
      changeToMode("select")
    }

  break
  case "graph":
    if(!operate){
      uiClear()//fransformUIのうちの何にも触れていない場合はselectに逆戻り
      decribeToPage()
      changeToMode("write")
    }
  }
  console.log(
    back.childElementCount+", "
   +currentPage.childElementCount+", "
   +selected.childElementCount+", "
   +ui.childElementCount+", "
   +mode+", "+operate+"で描きおわり")
  endOperate()
};


// ポインターの位置"e"を変数とする関数
let hoseitenGroup =[] 

function crrection(e){ 
  const r = Math.abs((e.y-inP.y)/(e.x-inP.x))
  switch(true){}
    if(r>10){curX = inP.x}else{curX=e.x}
    if(r<0.1){curY = inP.y}else{curY=e.y}
  let hoseiPoint=[curX,curY]
  for(let i = 1; i<hoseitenGroup.length;i++){
    let d = distance(hoseiPoint,hoseitenGroup[i])
    if((d>0)&&(d<10)){
      // return [thisX,thisY]
      hoseiPoint = hoseitenGroup[i]
      break;
    }
    // console.log(thisX+","+thisY)
  }
  return hoseiPoint
}

function erase(e){
  for(let i=0;i<currentPage.childElementCount;i++){
    thisPath = currentPage.children[i]
    const size = thisPath.style.strokeWidth
    thisPath.style.strokeWidth = Number(eraserSize)+Number(penSize);
    const touch = thisPath.isPointInStroke(e)
    thisPath.style.strokeWidth = size;
    if(touch){ 
      console.log("消去: "+thisPath.id)
      back.appendChild(thisPath)
      deleteCount++
      // i--
    }
  }
  
  //ballの消去
  for(let i=0;i<balls.length;i++){
    const d = distance(balls[i],e)
    if(d < Number(eraserSize/2)+Number(balls[i].size)){
      const index=balls.indexOf(balls[i])
      balls.splice(index,1)
      deleteCount++
      i--
    }
  }
}

function select(path){
  for(let i=0;i<currentPage.childElementCount;i++){
    const thisPath = currentPage.children[i]
    const points = thisPath.getPoints()
    for(let j=0;j<points.length;j++){
      if(path.isPointInFill(points[j])){
        selected.appendChild(thisPath)
        console.log(thisPath.id+"をselectedにしました")
        i--
        break
      }
    }
  }
}

// selectedの変換情報をそのChildに引き継いで、全てのChildをcurrentPageに移す。

function decribeToPage() {
  console.log("decribeToPageを実行します")
  while(selected.childElementCount>0){
    currentPage.appendChild(selected.firstChild)
    console.log(currentPage.lastChild.id+" をcurrentPageにしました")
  }
  // if(active.style.transform){
  //   active.SVGmatrixTransform(new DOMMatrix(active.style.transform))
  //   active.style.transform = ""
  // }
  graphFunction = NaN
  axisX = NaN
  axisY = NaN
}

// 制御点を作って直線化
SVGPathElement.prototype.setToLine =function(p1,p2){
  dx = p2.x-p1.x
  dy = p2.y-p1.y
  this.setAttributeNS(null,"d",`M ${p1.x} ${p1.y}`)
  const n = Math.max(dx,dy)
  for(let i=1;i<n+1;i++){
    this.setAttributeNS(null,"d",this.getAttributeNS(null,"d")+` L ${p1.x+i/n*dx} ${p1.y+i/n*dy}`)
  }
  hoseitenGroup.push(p1,p2)
}

//ui共通

let operatingPoints
let transformRect
let centerPoints

//uiを全て消去し、変換情報もリセット

function uiClear(){
  ui.style.transform = ""
  ui.transformCash = ""
  console.log("ui.transformCashをリセット")
  while(ui.firstChild){
    ui.removeChild(ui.firstChild)
    console.log("uiを全て削除しました")
  }
}