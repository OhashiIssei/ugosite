// 関数集
function degToRad(degrees) {
  return degrees * Math.PI / 180;
};



function conj(p1){
  return new DOMPoint(p1.x,-p1.y)
}

function sum(p1,p2){
  return new DOMPoint(p1.x+p2.x,p1.y+p2.y)
}

function diff(p1,p2){
  return new DOMPoint(p1.x-p2.x,p1.y-p2.y)
}

function times(p1,p2){
  return new DOMPoint(p1.x*p2.x-p1.y*p2.y,p1.x*p2.y+p1.y*p2.x)
}

function dev(p1,p2){
  return new DOMPoint(times(p1,conj(p2)).x/(norm(p2)**2),times(p1,conj(p2)).y/(norm(p2)**2))
}

function innerProduct(p1,p2){
  return p1.x*p2.x+p1.y*p2.y
}

function crossProduct(p1,p2){
  return p1.x*p2.y-p1.y*p2.x
}


function distance(p1,p2){
  return Math.hypot(p1.x-p2.x,p1.y-p2.y)
}

function midPoint(p1,p2){
  return new DOMPoint((p1.x+p2.x)/2,(p1.y+p2.y)/2)
}

function scalarTimes(p,scalar){
  return new DOMPoint(p.x*scalar,p.y*scalar)
}

function symmetryPointAbout(center,p){
  return diff(scalarTimes(center,2),p)
}

function norm(p){
  return Math.sqrt(p.x**2+p.y**2)
}

function denotedByComplex(p0,p1,p2){
  return dev(diff(p0,p1),diff(p2,p1))
}

function det(Matrix){
  return Matrix.a*Matrix.d-Matrix.b*Matrix.c
}




SVGElement.prototype.clientCenter = function(){
  const rect = this.getBoundingClientRect()
  return new DOMPoint(rect.x+rect.width/2,rect.y+rect.height/2)
}