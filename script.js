function show(id){
document.querySelectorAll('.box').forEach(b=>b.classList.add('hidden'))
document.getElementById(id).classList.remove('hidden')
}

async function detectImage(){
let res = await fetch('/detect',{method:'POST'})
let data = await res.json()
document.getElementById('detectResult').innerText=data.result
}

async function generateCode(){
let language=document.getElementById('lang').value
let features=document.getElementById('features').value

let res=await fetch('/code',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({language,features})
})

let data=await res.json()
document.getElementById('codeResult').innerText=data.code
}

async function askAI(){
let question=document.getElementById('question').value

let res=await fetch('/ask',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({question})
})

let data=await res.json()
document.getElementById('answer').innerText=data.answer
}
