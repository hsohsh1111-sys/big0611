document.addEventListener('DOMContentLoaded', function (){
    const joinForm = document.getElementById('joinForm');

    if (joinForm) {
        joinForm.addEventListener('submit', function (event){
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();
            const name = document.getElementById('name').value.trim();

            if (!username) {
                alert('아이디를 입력해 주세요.');
                document.getElementById('username').focus();
                event.preventDefault();
                return;
            }

            if (!password) {
                alert('비밀번호를 입력해 주세요.');
                document.getElementById('password').focus();
                event.preventDefault();
                return;
            }

            if (!name) {
                alert('이름을 입력해 주세요.');
                document.getElementById('name').focus();
                event.preventDefault();
                return;
            }
        });
    }
});