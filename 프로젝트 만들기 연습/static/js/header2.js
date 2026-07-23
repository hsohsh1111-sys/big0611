// 대상 요소 선택
const header = document.querySelector("#header");
const subBg = document.querySelector(".sub-bg");
// 클래스이므로 전체 선택
const depth1List = document.querySelectorAll(".depth1>li");
const depth2List = document.querySelectorAll(".depth2");
// 마우스가 들어왔을 때 (mouseenter)
depth1List.forEach(function (depth1) {
  depth1.addEventListener("mouseenter", function () {
    // this.classList.add("active");
    if (subBg) subBg.classList.add("active");

    // depth2는 여러 개이므로 반복문을 돌며 각각 클래스 추가
    const depth2 = depth1.querySelector(".depth2");
    if (depth2) {
      depth2.classList.add("active");
    }
  });
  // 마우스가 나갔을 때 (mouseleave)
  depth1.addEventListener("mouseleave", function () {
    // this.classList.remove("active");
    if (subBg) subBg.classList.remove("active");

    // depth2는 여러 개이므로 반복문을 돌며 각각 클래스 제거
    const depth2 = depth1.querySelector(".depth2");
    if (depth2) {
      depth2.classList.remove("active");
    }
  });

});