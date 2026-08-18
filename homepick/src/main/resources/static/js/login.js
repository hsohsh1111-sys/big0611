document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    // 1. URL 파라미터에 error가 존재하는지 확인 (로그인 실패 시)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('error')) {
        alert('아이디 또는 비밀번호가 올바르지 않습니다.\n다시 시도해 주세요.');
        // 확인 버튼을 누르면 URL의 ?error 파라미터를 깔끔하게 제거하여 재로그인 상태로 만듦
        history.replaceState({}, document.title, window.location.pathname);
    }

    // 2. 폼 제출 시 빈값 유효성 검사
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            const usernameInput = document.getElementById('username');
            const passwordInput = document.getElementById('password');

            if (!usernameInput.value.trim()) {
                alert('아이디를 입력해 주세요.');
                usernameInput.focus();
                event.preventDefault();
                return;
            }

            if (!passwordInput.value.trim()) {
                alert('비밀번호를 입력해 주세요.');
                passwordInput.focus();
                event.preventDefault();
                return;
            }
        });
    }
});