const header = document.querySelector("#header");
const subBg = document.querySelector(".sub-bg");
const depth2List = document.querySelectorAll(".depth2"); // 클래스이므로 전체 선택

header.addEventListener("mouseenter", function (){
  this.classList.add("active");
  if (subBg) subBg.classList.add("active");

  // depth2는 여러 개이므로 반복문을 돌며 각각 클래스 추가
  depth2List.forEach(function (depth2){
    depth2.classList.add("active");
  });
});

header.addEventListener("mouseleave", function (){
  this.classList.remove("active");
  if (subBg) subBg.classList.remove("active");

  // depth2는 여러 개이므로 반복문을 돌며 각각 클래스 제거
  depth2List.forEach(function (depth2){
    depth2.classList.remove("active");
  });
});