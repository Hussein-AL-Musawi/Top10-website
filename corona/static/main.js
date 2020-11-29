
// const para=document.querySelector("p")
// // console.log(para.offsetTop);
// document.addEventListener("scroll",(e)=>{
//     if(window.scrollY>para.offsetTop-window.innerHeight/2-50){
//         para.classList.add("add")
//     };
// })
const toggle=document.querySelector(".navbar__toggle");
const container=document.querySelector(".container");
const nav=document.querySelector(".navigation");
const imgs=document.querySelectorAll(".img__container img");
const imgsContainer = document.querySelectorAll(".img__container");
let widthOfNav=0;
imgs.forEach((img,index)=>{
  img.addEventListener("mousemove",(e)=>{
    const imgWidth= imgsContainer[index].getBoundingClientRect().width;
    const position = (e.layerX+widthOfNav)/imgWidth;
    // console.log(position*100);
    img.style["object-position"]=`${position*100}%`;


  })
  img.addEventListener("mouseout",()=>{
    img.style["object-position"] = `center`;
  })
})




toggle.addEventListener("click",()=>{
    container.classList.toggle("open");
    toggle.classList.toggle("open")
    if(container.classList.contains("open")){
        const navWidth=nav.getBoundingClientRect().width;
        widthOfNav=navWidth
        container.style["transform"]=`translateX(${-navWidth}px)`;
        

    }else{
        container.style["transform"] = `translateX(${0}px)`;
        widthOfNav=0;
        
    }
    nav.classList.toggle("open")
})
document.addEventListener("scroll",()=>{
    const navbar=document.querySelector(".navbar");
    const navbarHeight=navbar.getBoundingClientRect().height;
    // const containerHeight=container.getBoundingClientRect().height;
    const divOffset=document.querySelector(".cards").offsetTop;
    
    if (window.scrollY > divOffset - navbarHeight / 2) {
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
    }
})


function orderWeight(string) {
  if(!string){
    return "";
  }
  string=string.trim().split(/ +/g).sort();
  
  
  let arr=[];
  let arrNum=[];
  let orderArr=[]
  // let str=[];

  string.forEach(item=>{
    let sum = 0;
    item.split("").forEach(num=>{
      sum+=parseInt(num)
    })
    arr.push({item,sum})
    arrNum.push(sum)
  })
  arrNum= arrNum.sort((a,b)=>a-b)
  arrNum.forEach(num=>{
    arr.forEach(item=>{
      if(item.sum===num && !orderArr.includes(item)){
        orderArr.push(item)
        
      }
    })
  })
  
  orderArr=orderArr.map(item=>item.item);
  return orderArr.join(" ")

}
orderWeight("103 123 414 9 2000");

