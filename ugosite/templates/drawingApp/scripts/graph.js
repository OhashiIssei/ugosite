// Graph
let axisX
let axisY
let originP = new DOMPoint()

//グラフ生成

modeRadio[4].addEventListener("click",function(){
  changeToMode("graph")
  const n= selected.childElementCount
  if(n>1&&n<4){
    for(let i=0;i<n;i++){
      const thisPath = selected.children[i]
      const points = thisPath.getPoints()
      if(points[0].y===points.slice(-1)[0].y){//始点と終点のy座標が一致
        axisX = thisPath
        console.log(thisPath.id+" をx軸を記録")
      }else if(points[0].x===points.slice(-1)[0].y){//始点と終点のx座標が一致
        axisY = thisPath
        console.log(thisPath.id+" をy軸を記録")
      }
    }
    originP.x = axisY.clientCenter().x
    originP.y = axisX.clientCenter().y  
  }else{
    box = new DOMRect(width/4,height/4,width/2,height/2)
    originP = new DOMPoint(width/2,height/2)
    addAxis(originP,box)
  }
  askFunction()
  drawGraph(originP,box,100)
  center = selected.clientCenter()
  createGraphUi(originP,box,center)
})

// line mode 終了時、水平/垂直のpathを書いているかどうかを調べる。
function checkAxisLines(){
  if(inP.y===outP.y){
    axisX = path
    console.log(path.id+" をx軸に設定")
  }else if(inP.x===outP.x){
    axisY = path
    console.log(path.id+" をy軸に設定")
    if(axisX){
      changeToMode("graph")
      selected.appendChild(axisX)
      selected.appendChild(axisY)

      askFunction()
      box = selected.getBoundingClientRect()
      drawGraph(originP,box,100)
      center = selected.clientCenter()
      createGraphUi(originP,box,center)
    }
  }
}

//axisX,axisYを作る（originP,boxに対して）
function addAxis(point,box){
  axisX = document.createElementNS(SVG_URL,"path")
  selected.appendChild(axisX)
  axisX.setAttributeNS(null,"id","line"+id);id++
  axisX.setToLine(new DOMPoint(box.left,point.y),new DOMPoint(box.right,point.y))
  axisX.setAttributeNS(null,"style",`stroke:${penColor}; stroke-width:${penSize/2}`)

  axisY = document.createElementNS(SVG_URL,"path")
  selected.appendChild(axisY)
  axisY.setAttributeNS(null,"id","line"+id);id++
  axisY.setToLine(new DOMPoint(point.x,box.top),new DOMPoint(point.x,box.bottom))
  axisY.setAttributeNS(null,"style",`stroke:${penColor}; stroke-width:${penSize/2}`)

  console.log(axisX.id+" と "+ axisY.id+" をaddAxisで追加しました")
}

function askFunction(){
  const p = prompt('引数xの関数の式をJS形式で入力してください。y=?');
  graphFunction = new Function("x","return "+p)
}

let scale =100
let graphFunction = NaN

function drawGraph(originP,box,scale){
  path = document.createElementNS(SVG_URL,"path")
  selected.appendChild(path)
  path.setAttributeNS(null,"id","graph"+id);id++ 
  path.setAttributeNS(null,"d","")
  path.setAttributeNS(null,"style",`stroke:${penColor}; stroke-width:${penSize}; fill-opacity:0`)

  console.log("drawGraphを開始します")
  let isInAxisY = false
  for(let x=box.left;x<=box.right;x++){
    const graphY =-graphFunction((x-originP.x)/scale)*scale+originP.y
    // console.log(x,graphY)
    if(graphY){
      if(graphY>=box.top && graphY<=box.bottom){
        if(isInAxisY){
          path.setAttributeNS(null,"d",path.getAttributeNS(null,"d")+` L ${x} ${graphY}`)
        }else{
          path.setAttributeNS(null,"d",path.getAttributeNS(null,"d")+` M ${x} ${graphY}`)
          isInAxisY=true
        }
        console.log("内")
      }else{
        isInAxisY=false
        console.log("外")
      }
    }
  }
}

function Anker(x,y,cursor,element,operate,centerX,centerY){
  this.x = x;
  this.y = y;
  this.cursor = cursor;
  this.element =  element;
  this.operate = operate;
  this.centerX = centerX;
  this.centerY = centerY;
}


function createGraphUi(originP,box,center){
  const data1 = [
    new Anker(box.left,box.top,"nwse-resize",active,"scale",box.right,box.bottom),
    new Anker(box.left,box.bottom,"nesw-resize",active,"scale",box.right,box.top),
    new Anker(box.right,box.bottom,"nwse-resize",active,"scale",box.left,box.top),
    new Anker(box.right,box.top,"nesw-resize",active,"scale",box.left,box.bottom),
    new Anker(box.left,center.y,"ew-resize",axisX,"scaleX",box.right,center.y),
    new Anker(center.x,box.bottom,"ns-resize",axisY,"scaleY",center.x,box.top),
    new Anker(box.right,center.y,"ew-resize",axisX,"scaleX",box.left,center.y),
    new Anker(center.x,box.top,"ns-resize",axisY,"scaleY",center.x,box.bottom)
  ]
  addTransformRect(box)
  addOperatingPoints(data1)
  const data2 = 
    [new Anker(center.x,center.y,"zoom-in",active,"scale",center),
    new Anker(center.x,center.y,"grab",centerPoints,"translate")]
  addCenterPoints(data2,center)
  console.log(box+ "のGraphUIをcreateしました")
}


  
  
    // startOperate("scaleGraph")
    // inP = e;
    // center = centerPoints.clientCenter()
    // layers.addEventListener("pointermove",transforming = (e)=>{selected.transforming(e,"scale",center)})
    // layers.addEventListener("pointerup",transformSelf= (e)=>{
    //   while(selected.firstChild){
    //     selected.removeChild(selected.firstChild)
    //   }
    //   console.log("一旦selectedを消しました")
    //   const matrix = new DOMMatrix(selected.style.transform)
    //   selected.style.transform=""
    //   originP = originP.matrixTransform(matrix)
    //   addAxis(originP,box)
    //   drawGraph(originP,box,scale)
    //   uiClear()
    //   createGraphUi(originP,box,center)
    //   layers.removeEventListener("pointermove",transforming)
    //   layers.removeEventListener("pointerup",transformSelf)
    // })

// scale = scale*Math.sqrt(ratio)