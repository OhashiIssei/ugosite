//"operater"の管理
let operate=NaN

function startOperate(operateName){
  operate = operateName
  console.log("startOperate: "+operate)
}

function  endOperate(){
  console.log("endOperate: "+operate)
  operate = NaN
}

//UI作成
function createTransformUi() {
  const box = selected.getBoundingClientRect()  
  
  w = box.width
  h = box.height

  // transformRectの設定
  addTransformRect(box)
  // operattingPointsの設定
  center = selected.clientCenter()
  const data1 = [
    new Anker(box.left,box.top,"nwse-resize",active,"scale",box.right,box.bottom),
    new Anker(box.left,box.bottom,"nesw-resize",active,"scale",box.right,box.top),
    new Anker(box.right,box.bottom,"nwse-resize",active,"scale",box.left,box.top),
    new Anker(box.right,box.top,"nesw-resize",active,"scale",box.left,box.bottom),
    new Anker(box.left,center.y,"ew-resize",active,"scaleX",box.right,center.y),
    new Anker(center.x,box.bottom,"ns-resize",active,"scaleY",center.x,box.top),
    new Anker(box.right,center.y,"ew-resize",active,"scaleX",box.left,center.y),
    new Anker(center.x,box.top,"ns-resize",active,"scaleY",center.x,box.bottom)
  ]
  addOperatingPoints(data1)

  //centerPointsの設定
  const data2 = 
    [new Anker(center.x,center.y,"zoom-in",active,"scale",center),
    new Anker(center.x,center.y,"grab",centerPoints,"translate")]
  addCenterPoints(data2,center)

  console.log(box + "のTransformUIを表示しました")
}

// transformRectの設定
function addTransformRect(box){
  w = box.width
  h = box.height

  transformRect = document.createElementNS(SVG_URL,"path")
  transformRect.setAttributeNS(null,"d",`M ${box.x} ${box.y} v ${h} h ${w} v ${-h} h ${-w} `)
  transformRect.setAttributeNS(null,"style","stroke:white; stroke-width:1; stroke-opacity:0.5; fill-opacity:0")
  transformRect.style.cursor="all-scroll"
  ui.appendChild(transformRect)

  transformRect.addEventListener("pointerdown",function(e){
    active.transformStart(e,"translate")
  })
  console.log("addTransformRectを実行")
}


// operattingPointsの設定
function addOperatingPoints(data){
  operatingPoints = document.createElementNS(SVG_URL,"g")
  ui.appendChild(operatingPoints)

  for(let i=0;i<data.length;i++){
    operatingPoints.appendChild(document.createElementNS(SVG_URL,"path"))
    operatingPoints.lastChild.setAttributeNS(null,"style","fill:white;fill-opacity:0.5")
    const cx = data[i].x
    const cy = data[i].y
    const r = (w+h)/80
    operatingPoints.lastChild.setAttributeNS(null,"d",`M ${cx} ${cy} m ${-r} ${0} a ${r} ${r} 0 1 1 ${0} ${alpha}`)
    operatingPoints.lastChild.setAttributeNS(null,"class",data[i].cursor)
    operatingPoints.lastChild.addEventListener("pointerdown",function(e){
      data[i].element.transformStart(e,data[i].operate,new DOMPoint(data[i].centerX,data[i].centerY))
    })
  }
  
  console.log("addOperatingPointsを実行")
}


// //centerPointsの設定
function addCenterPoints(data,center){
  centerPoints = document.createElementNS(SVG_URL,"g")
  centerPoints.appendChild(document.createElementNS(SVG_URL,"path"))
  centerPoints.appendChild(document.createElementNS(SVG_URL,"path"))
  ui.appendChild(centerPoints)

  let cx = center.x
  let cy = center.y
  let r = (w+h)/10
  centerPoints.children[0].setAttributeNS(null,"style",`stroke:white;stroke-opacity:0.5;stroke-width:${(w+h)/200};fill-opacity:0`)
  centerPoints.children[0].setAttributeNS(null,"d",`M ${cx} ${cy} m ${-r} ${0} a ${r} ${r} 0 1 1 ${0} ${alpha}`)
  r = (w+h)/60
  centerPoints.children[1].setAttributeNS(null,"style","fill:white;fill-opacity:0.5")
  centerPoints.children[1].setAttributeNS(null,"d",`M ${cx} ${cy} m ${-r} ${0} a ${r} ${r} 0 1 1 ${0} ${alpha}`)

  for(let i=0;i<data.length;i++){
    operatingPoints.children[i].setAttributeNS(null,"class",data[i].cursor)
    operatingPoints.children[i].addEventListener("pointerdown",function(e){
      data[i].element.transformStart(e,data[i].operate,data[i].center)
    })
  }
  console.log("addCenterPointsを実行")
}


//変形開始
Element.prototype.transformStart = function(e,operate,center){
  startOperate(operate)
  inP = e
  layers.addEventListener("pointermove",transforming= (e)=>{this.transforming(e,operate,center)})
  layers.addEventListener("pointerup",transformSelf= (e)=>{this.transformSelf(e)})
}


//変形中
Element.prototype.transforming = function(e,operate,center){
  switch(operate){
    case "translate": 
      this.style.transform = `translate(${e.x-inP.x}px,${e.y-inP.y}px)`;break
    case "scale": const complex = denotedByComplex(e,center,inP)
      this.style.transform = ` translate(${center.x}px,${center.y}px) scale(${norm(complex)}) translate(${-center.x}px,${-center.y}px)`;break
    case "scaleX": let ratio = (e.x-center.x)/(inP.x-center.x)
      this.style.transform = `translate(${center.x}px,${center.y}px) scale(${ratio},1) translate(${-center.x}px,${-center.y}px)` ;break
    case "translate": ratio = (e.y-center.y)/(inP.y-center.y)
      this.style.transform = `translate(${center.x}px,${center.y}px) scale(1,${ratio}) translate(${-center.x}px,${-center.y}px)`;break
  }
  
}

//変形終了
Element.prototype.transformSelf = function(e){
  this.SVGmatrixTransform(new DOMMatrix(this.style.transform))
  layers.removeEventListener("pointermove",transforming)
  layers.removeEventListener("pointerup",transformSelf)
  if(mode==="graph"){
    selected.removeChild(selected.lastChild)
    box = selected.getBoundingClientRect()
    drawGraph(originP,box,scale)
    uiClear()
    createGraphUi(originP,box,center)
  }
  console.log(this.id)
  console.log("↑を変換しました")
}



//uiを全て消去し、変換情報もリセット

function uiClear(){
  while(ui.firstChild){
    ui.removeChild(ui.firstChild)
    console.log("uiを全て削除しました")
  }
}

SVGPathElement.prototype.getPoints = function(){
  const d = this.getAttributeNS(null,"d")
  const regexp = /[a-zA-Z][^a-zA-Z]+/g
  const list = d.match(regexp)
  // console.log(list)
  points = []
  for(let i=0;i<list.length;i++){
    const regexp2 = /\b[-]*[0-9.]+/g
    const nums = list[i].match(regexp2)
    // console.log(nums)
    points.push(new DOMPoint(nums.slice(-2)[0],nums.slice(-1)[0]))
  }
  return points
}

Element.prototype.SVGmatrixTransform = function(DOMMatrix){
  let ratio =  Math.sqrt(Math.abs(det(DOMMatrix)))
  if(this.childElementCount>0){
    for(let i=0;i<this.childElementCount;i++){
      this.children[i].SVGmatrixTransform(DOMMatrix)
    }
  }else{
    let d = this.getAttributeNS(null,"d")
    const regexp = /[a-zA-Z][^a-zA-Z]+/g
    const list = d.match(regexp)
    // console.log(list)
    d = ""
    for(let i=0;i<list.length;i++){
      const regexp2 = /\b[a-zA-Z]\b|\s[0-9._-]+\b/g
      const mod = list[i].match(regexp2)
      // console.log(mod)
      let endP = new DOMPoint(mod.slice(-2)[0],mod.slice(-1)[0]).matrixTransform(DOMMatrix)
      // console.log(ratio)
      switch(mod[0]){
        case "M":
        case "L":
          d+=` ${mod[0]} ${endP.x} ${endP.y}`
          break;

        case "V":
          endP = new DOMPoint(mod[1],0).matrixTransform(DOMMatrix)
          d+=` L ${endP.x} ${endP.y}`
          break;
        
        case "V":
          endP = new DOMPoint(0,mod[1]).matrixTransform(DOMMatrix)
          d+=` L ${endP.x} ${endP.y}`
          break;

        case "Q":
          const ancP = new DOMPoint(mod[1],mod[2]).matrixTransform(DOMMatrix)
          d+=` ${mod[0]} ${ancP.x} ${ancP.y} ${endP.x} ${endP.y}`
          break;

        case "A":
          d+=` ${mod[0]} ${mod[1]} ${mod[2]} ${mod[3]} ${mod[4]} ${mod[5]} ${endP.x} ${endP.y}`
          break;

        case "m":
          d+= ` ${mod[0]} ${mod[1]*ratio} ${mod[2]*ratio}`
          break;

        
        case "a":
          d+= ` ${mod[0]} ${mod[1]*ratio} ${mod[2]*ratio} ${mod[3]} ${mod[4]} ${mod[5]} ${mod[6]} ${mod[7]}`
          // console.log(d)
          break;
        
      }
      // console.log(mod)
    }
    this.setAttributeNS(null,"d",d)
    console.log(this.id+" を "+DOMMatrix+" で変換しました")
  }
  this.style.transform =""
  if(mode==="shape"){
    currentPage.appendChild(path)
  }
}

