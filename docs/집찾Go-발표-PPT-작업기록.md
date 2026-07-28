# 집찾Go 부동산 웹 플랫폼 — 발표 PPT 작업 기록

**작업 일자:** 2026-07-28  
**목적:** 부동산 웹 플랫폼 제작 결과 발표 (약 **20분**, 슬라이드 **10장**)  
**서비스명:** 집찾Go (ZipChatGo) — 스마트 부동산 플랫폼

---

## 1. 작업 요약

- `python-pptx` 기반으로 발표용 PowerPoint를 **코드로 생성**하도록 구현했다.
- 저장소 내 `프로젝트/팀 프로젝트 소개페이지` 등 기존 집찾Go 소개 문구(실거래·시장동향·모바일 모델하우스·집 내놓기·중개 라이브)를 반영했다.
- 요청된 **팀원 4명**, **기술 스택**, **RPA+AI Python 패키지**를 슬라이드에 포함했다.

### 산출물

| 파일 | 설명 |
|------|------|
| `scripts/generate_presentation.py` | 10장 PPT 생성 스크립트 |
| `집찾Go_부동산플랫폼_제작결과발표.pptx` | 최종 발표 파일 |
| `docs/집찾Go-발표-PPT-작업기록.md` | 본 문서 |

---

## 2. 팀 구성 (4명)

| 이름 | 슬라이드 역할 (예시) |
|------|----------------------|
| 맹준형 | 기획 · 프론트/백엔드 개발 |
| 이승우 | UI/UX · 프론트엔드 · API 연동 |
| 안종범 | 백엔드 · DB · 보안(Spring Security) |
| 황상옥 | 데이터 · RPA/AI · 시각화 |

> 역할 문구는 발표용 초안이다. 실제 분담에 맞게 `scripts/generate_presentation.py`의 `team_slide()` 함수에서 수정 후 재생성하면 된다.

---

## 3. 기술 스택 (발표 반영 내용)

### Frontend

- HTML, CSS, JavaScript
- Bootstrap 5
- Flexbox 레이아웃

### Backend

- JDK 21
- Spring Boot 3.5.x
- Thymeleaf
- Tomcat 10.1
- MySQL 8

### 빌드 · 배포

- **빌드:** Gradle
- **DB(클라우드):** TiDB
- **배포:** Render 또는 AWS EC2

### Spring 의존성 (DI)

- Spring Web
- Spring Security (BCrypt)
- Thymeleaf
- MySQL Connector
- Lombok
- JDBC Template

### RPA + AI (Python)

- NumPy, Pandas
- Matplotlib, Seaborn
- Folium, Plotly
- Requests, BeautifulSoup
- Scikit-learn

---

## 4. 슬라이드 구성 (10장)

| # | 제목 | 권장 시간 | 내용 요약 |
|---|------|-----------|-----------|
| 1 | 표지 | ~1분 | 집찾Go, 20분·10장, 팀원 |
| 2 | 목차 | ~1분 | 발표 흐름 |
| 3 | 프로젝트 개요 | ~2분 | 목표, 가치, 차별점 |
| 4 | 팀 구성원 소개 | ~2분 | 4인 카드 레이아웃 |
| 5 | 주요 기능 및 서비스 | ~2분 | 모델하우스, 집 내놓기, 중개 라이브 등 |
| 6 | 시스템 아키텍처 | ~2분 | Client → Spring → DB → 배포 → Python 파이프라인 |
| 7 | 기술 스택 | ~2분 | Frontend / Backend 2단 |
| 8 | 빌드·배포·의존성 | ~2분 | Gradle, TiDB, Render/EC2, starter 목록 |
| 9 | RPA + AI | ~2분 | Python 패키지·시각화 |
| 10 | 제작 결과 및 Q&A | ~2분 | 완료 항목, 향후 계획 |

**디자인:** 네이비(`#1A365D`) · 틸(`#0D9488`) 테마, 맑은 고딕, 슬라이드 크기 10×7.5 inch.

---

## 5. PPT 재생성 방법

### 사전 요구

```bash
pip install python-pptx
```

### 실행

```bash
python scripts/generate_presentation.py
```

기본 출력 경로: 저장소 루트의 `집찾Go_부동산플랫폼_제작결과발표.pptx`

---

## 6. 발표 팁 (20분)

1. **3~4장:** 문제 정의 + 팀 + 서비스 — 청중이 “무엇을 왜 만들었는지”를 먼저 이해하게 한다.
2. **6~9장:** 아키텍처와 스택 — 데모 없을 때는 “한 장에 한 레이어”만 말하고 깊이는 질문 때 확장한다.
3. **10장:** 완료 vs 향후를 구분해 말하고, Q&A용으로 TiDB/Render 선택 이유 한 줄 준비.

---

## 7. 변경 이력

| 날짜 | 내용 |
|------|------|
| 2026-07-28 | 최초 PPT 생성 스크립트 및 10장 구성 작성, docs 정리 |
