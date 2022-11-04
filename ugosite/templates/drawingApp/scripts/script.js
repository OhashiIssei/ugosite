//高さと幅のの調整

let alpha =1/10000

const menuHeight = 85
const width = window.innerWidth;
const height = window.innerHeight;

const SVG_URL = 'http://www.w3.org/2000/svg'


const layers = document.querySelector("#layers")
const active = document.querySelector("#active")
const ui = document.querySelector("#ui")
const selected = document.querySelector("#selected")
const back = document.querySelector("#back")

const pages = document.querySelector("#pages")
const pageText = document.querySelector('#page-text');

const styleInfo = document.querySelector('#style-info');



//localStrageのnotesを調べる

if(!localStorage.notes){//localStorage.notesがなければ初めの訪問てです。
  localStorage.currentNoteId = 1
  localStorage.noteIdCounter = 1
  const p = prompt('ようこそ、UgoSuuの世界へ!     新しいNoteの名前を入力してください');
  localStorage.currentNoteTitle = p
  document.title = p
  localStorage.notes = JSON.stringify([getCurrentNoteData()]);
  console.log(getCurrentNoteData())
}

if(!localStorage.currentNoteId){
  localStorage.noteIdCounter++
  localStorage.currentNoteId = localStorage.noteIdCounter
  console.log("新しく currentNoteId : "+localStorage.noteIdCounter+"を割り振りました")
}

let notes = JSON.parse(localStorage.notes)

let pageId = 2
let noteIndex

searchNotes()

function searchNotes(){
  console.log("id : "+localStorage.currentNoteId+"がlocalStrage.notesに存在しているかを調べます")
  for(i = 0; i<notes.length; i++){
    if(notes[i].noteId === localStorage.currentNoteId){//一致したら
      document.title = notes[i].title
      pages.innerHTML = notes[i].pages
      styleInfo.innerHTML = notes[i].styleInfo
      noteIndex = i
      console.log("ありました。noteId"+notes[i].noteId+"を読み込みました")
      console.log(getCurrentNoteData())
      break
    }
    if(i===notes.length-1){//いずれにも一致しないなら
      const p = prompt('新しいNoteの名前を入力してください');
      localStorage.currentNoteTitle = p
      notes.push(getCurrentNoteData())//新たなデータを最後に追加
      noteIndex = i+1
      console.log("ありませんでした。新しくid : "+localStorage.currentNoteId+"を作りました")
      console.log(getCurrentNoteData())
      break
    }
  }
}

function getCurrentNoteData(){
  const youbi = ["日","月","火","水","木","金","土"];
  const date1 = new Date();
  const date2 = date1.getFullYear() + "年" + 
    (date1.getMonth() + 1)  + "月" + 
    date1.getDate() + "日(" + 
    youbi[date1.getDay()] + ") "+
    date1.getHours().toString().padStart(2,"0") + ":" + 
    date1.getMinutes().toString().padStart(2,"0") + ":" + 
    date1.getSeconds().toString().padStart(2,"0")
  return {
    "noteId" : localStorage.currentNoteId,
    "title" : localStorage.currentNoteTitle,
    "pages" : pages.innerHTML,
    "styleInfo" : styleInfo.innerHTML,
    "lastEditDate" : date2,
  }
}


let currentPage = document.querySelector(".current-page")

let svg = document.querySelectorAll("svg")
for(let i=0;i<svg.length;i++){//高さと幅の調整
  svg[i].setAttributeNS(null,"style","stroke-linecap:round;stroke-linejoin:round")
  svg[i].setAttributeNS(null,"height",height)
  svg[i].setAttributeNS(null,"width",width)
}



// || note-operate ボタンの機能実装
const noteBtns = document.querySelectorAll('#note-operate button');

//ページ移動/追加
for(let i=0;i<2;i++){
  currentPage = document.querySelector(".current-page")
  noteBtns[i].addEventListener("click",(e)=>{
    currentPage = pageChangeOrAdd(e,i)
  })
}

//ページ削除
noteBtns[2].addEventListener("click",function(e){
  currentPage = document.querySelector(".current-page")
  if(currentPage.nextElementSibling){
    newPage = pageChangeOrAdd(e,1)
  }else{
    newPage = pageChangeOrAdd(e,0)
  }
  back.appendChild(currentPage)
  console.log(currentPage.id+"を削除しました")
  currentPage = newPage
  pageTextUpgrade(newPage)
})



function pageChangeOrAdd(e,i){
  e.preventDefault();
  let newPage
  i===0?newPage = currentPage.previousElementSibling:newPage = currentPage.nextElementSibling
  if(newPage){
    console.log(newPage.id+"に移動しました")
  }else{
    newPage = currentPage.cloneNode(false)
    i===1?pages.appendChild(newPage):pages.prepend(newPage)
    newPage.setAttributeNS(null,"id","page"+pageId);pageId++
    console.log(newPage.id+"を追加しました")
  }
  currentPage.setAttributeNS(null,"class","not-current-page")
  newPage.setAttributeNS(null,"class","current-page")
  pageTextUpgrade(newPage)
  return newPage
}

pageTextUpgrade(currentPage)

function pageTextUpgrade(newPage){
  const pageNum = [].slice.call(pages.children).indexOf(newPage)+1
  pageText.textContent = pageNum+"/"+pages.childElementCount
}

// localStrageに保存
noteBtns[3].addEventListener("click",function(e){
  e.preventDefault();
  overWrite(e)
})

function overWrite(){
  decribeToPage()
  notes[noteIndex] = getCurrentNoteData()
  localStorage.notes = JSON.stringify(notes);
  console.log("noteId"+localStorage.currentNoteId+"を上書きしました")
  console.log(getCurrentNoteData())
}


noteBtns[4].addEventListener("click",function(e){
  e.preventDefault()
  overWrite()
  if(!localStorage.noteIdCounter){
      localStorage.noteIdCounter=1
  }
  localStorage.currentNoteId =  localStorage.noteIdCounter
  localStorage.noteIdCounter++
  window.open("../drawingApp/index.html")
})

//上書きしてホームに戻る
noteBtns[5].addEventListener("click",function(e){
  e.preventDefault();
  overWrite()
  console.log("上書きしてホームへ戻ります")
  window.open("../notes/index.html")
})



const Btns = document.querySelectorAll('button');

const keys =  ["b","u","a","x","p","n","r","s","c","h"]
for(let i=0;i<Btns.length;i++){
  Btns[i].textContent += " ("+keys[i].charAt(0).toUpperCase()+")"
}




//style-info の設定

const colorPicker = document.querySelectorAll('input[type="color"]');
const sizePicker = document.querySelectorAll('.penSize');
const eraserSizePicker = document.querySelectorAll('.eraserSize');

changeStyle(colorPicker[0])
changeStyle(sizePicker[0])
changeStyle(eraserSizePicker[0])

pickers = document.querySelectorAll("#style-info input")

for(let j=0;j<pickers.length;j++){
  pickers[j].addEventListener('click', (e)=>{changeStyle(e.target)})
  pickers[j].addEventListener('change', (e)=>{changeStyle(e.target)})
}

function changeStyle(picker){
  if(selected.childElementCount>0){
    for(let i=0;i<selected.childElementCount;i++){
      switch(picker.getAttribute("class")){
        case "penColor":
          selected.children[i].style.strokeStyle = picker.value
        case "penSize":
          selected.children[i].style.strokeWidth = pickervalue
      }
      console.log(selected.children[i].id+"を"+picker.value+"に再設定しました")
    }
  }else{
    for(let k=0;k<picker.parentNode.childElementCount;k++){
      picker.parentNode.children[k].setAttribute("status","off")
    }
    picker.setAttribute("status","on")
    switch(picker.getAttribute("class")){
      case "penColor":
        penColor=picker.value
        ;break
      case "penSize":
        penSize=picker.value;
        break
      case "eraserSize":
        eraserSize=picker.value;
        // changeToMode("erase")
        break
    }
    picker.setAttribute("value",picker.value) 
    console.log(picker.getAttribute("class")+"を"+picker.value+"に設定しました")
  }
}






// ||edit-operate ボタンの実装
const editBtns = document.querySelectorAll('#edit-operate button');

// ||戻る

editBtns[0].addEventListener("click",function(e){
  e.preventDefault();
  uiClear()
  decribeToPage()
  switch(mode){
    case "erase":
      if(back.lastChild){
        currentPage.appendChild(back.lastChild)
      }
      break;
    case "write":
      if(currentPage.lastChild){
        back.appendChild(currentPage.lastChild)
      }
      break
  }
  console.log("戻したい（まだ未実装）")
})

// ||取り消す

editBtns[1].addEventListener("click",function(e){
  e.preventDefault();
  uiClear()
  decribeToPage()
  switch(mode){
    case "erase":
      if(currentPage.lastChild){
        back.appendChild(currentPage.lastChild)
      }
      break;
    case "write":
      if(back.lastChild){
        currentPage.appendChild(back.lastChild)
      }
      break
  }
  console.log("取り消したい（まだ未実装）")
})

// || 全消去

editBtns[2].addEventListener("click",function(e){
  e.preventDefault();
  uiClear()
  decribeToPage()
  while(currentPage.firstChild){
    back.appendChild(currentPage.firstChild)
  }
  console.log("全消去しました")
  changeToMode("write")
});


// シミュレーション開始
let symurate=false

editBtns[3].addEventListener("click",function(e){
  e.preventDefault();
  uiClear()
  decribeToPage()
  if(symurate){
    symurate=false
    console.log("ボールOFF")
  }else{
    symurate=true
    createManyBall()
    console.log("ボールON")
  }
  // console.log("ボール")
})



