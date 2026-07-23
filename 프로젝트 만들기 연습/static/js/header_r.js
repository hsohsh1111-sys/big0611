const header = document.querySelector("#header");
const subBg = document.querySelector(".sub-bg");
const depth2List = document.querySelectorAll(".depth2");

// [추가] 모바일 햄버거 메뉴, 오버레이, 닫기 버튼 및 1차 메뉴 링크 선택
const btnHamburger = document.querySelector(".btn-hamburger");
const gnb = document.querySelector(".gnb");
const btnClose = document.querySelector(".btn-close");
const menuOverlay = document.querySelector(".menu-overlay");
const depth1Links = document.querySelectorAll(".depth1 > li > a");

header.addEventListener("mouseenter", function () {
  // [수정] PC 데스크톱 화면(992px 이상)에서만 PC용 메뉴 호버 동작이 실행되도록 조건 추가
  if (window.innerWidth > 991) {
    if (subBg) subBg.classList.add("active");
    depth2List.forEach(function (depth2) {
      depth2.classList.add("active");
    });
  }
});

header.addEventListener("mouseleave", function () {
  // [수정] PC 데스크톱 화면(992px 이상)에서만 PC용 메뉴 호버 닫기 동작이 실행되도록 조건 추가
  if (window.innerWidth > 991) {
    if (subBg) subBg.classList.remove("active");
    depth2List.forEach(function (depth2) {
      depth2.classList.remove("active");
    });
  }
});

// [추가] 모바일 햄버거 버튼 클릭 시 우측 사이드 메뉴 열기
if (btnHamburger) {
  btnHamburger.addEventListener("click", function () {
    gnb.classList.add("active");
    if (menuOverlay) menuOverlay.classList.add("active");
    document.body.style.overflow = "hidden"; // [추가] 메뉴가 열려 있을 때 배경 스크롤 방지
  });
}

// [추가] 모바일 닫기(X) 버튼 클릭 시 사이드 메뉴 닫기
if (btnClose) {
  btnClose.addEventListener("click", closeMobileMenu);
}

// [추가] 메뉴 외부 영역(어두운 오버레이 배경) 클릭 시 사이드 메뉴 닫기
if (menuOverlay) {
  menuOverlay.addEventListener("click", closeMobileMenu);
}

// [추가] 모바일 메뉴를 닫는 공통 함수
function closeMobileMenu() {
  gnb.classList.remove("active");
  if (menuOverlay) menuOverlay.classList.remove("active");
  document.body.style.overflow = ""; // [추가] 배경 스크롤 다시 허용
}

// [추가] 모바일 아코디언 메뉴 동작 (1차 메뉴 클릭 시 하위 메뉴 토글)
depth1Links.forEach(function (link) {
  link.addEventListener("click", function (e) {
    // [추가] 모바일 및 태블릿 화면(991px 이하)일 때만 아코디언 동작
    if (window.innerWidth <= 991) {
      const subMenu = this.nextElementSibling;
      
      // [추가] 하위 메뉴(depth2)가 존재하는 경우 페이지 이동을 막고 메뉴를 펼침
      if (subMenu && subMenu.classList.contains("depth2")) {
        e.preventDefault();
        const parentLi = this.parentElement;

        // [추가] (선택사항) 다른 열려있는 메뉴를 자동으로 닫으려면 아래 3줄 주석 해제
        // document.querySelectorAll(".depth1 > li").forEach(function(item) {
        //   if (item !== parentLi) { item.classList.remove("open"); item.querySelector(".depth2")?.classList.remove("active"); }
        // });

        parentLi.classList.toggle("open");
        subMenu.classList.toggle("active");
      }
    }
  });
});

// [추가] 창 크기를 조절하여 PC 화면으로 넘어갈 경우 모바일 열린 메뉴 및 스타일 초기화
window.addEventListener("resize", function () {
  if (window.innerWidth > 991) {
    closeMobileMenu();
    document.querySelectorAll(".depth1 > li").forEach(function (li) {
      li.classList.remove("open");
    });
    depth2List.forEach(function (depth2) {
      depth2.classList.remove("active");
    });
    if (subBg) subBg.classList.remove("active");
  }
});