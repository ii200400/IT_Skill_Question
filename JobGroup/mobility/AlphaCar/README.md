# 🚖 알파카 (Alpha car)

스켈레톤 코드 공개 불가로 인하여 알파카 프로젝트의 README 만을 옮겨놓았습니다.

### 당신의 택시 드라이버

<details>
<summary>자율주행 자동차 시뮬레이션 이미지</summary>
<div markdown="1">
  
  <img src="https://user-images.githubusercontent.com/19484971/220051703-3c3d3a39-ef08-492b-bbb3-cd3a24abe893.png">

  > 출발지와 도착지를 지정하여 만들어진 전역경로를 따라 이동하는 자동차와 Rviz 시각화 프로그램

</div>
</details>

<details>
<summary>모바일 어플리케이션 이미지</summary>
<div markdown="1">

  <img src="https://user-images.githubusercontent.com/19484971/220055480-421fdfec-9554-467b-97a0-a206a462fa65.png" width=200>

</div>
</details>

<details>
<summary>발표 시연 이미지</summary>
<div markdown="1">

  <img src="https://user-images.githubusercontent.com/19484971/220267070-72ef7ca7-8041-4c0d-8b45-10ae3d64ed0e.png" width=600>

</div>
</details>

- [발표 시연 동영상](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fdf501bb-8635-478e-b55e-af3af29ea018/ezgif.com-gif-maker_%281%29.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230220T083816Z&X-Amz-Expires=86400&X-Amz-Signature=c6d372d8f4c5f367f313053df6a727e9b44b838e26875910d03746d02318c5ad&X-Amz-SignedHeaders=host&x-id=GetObject)

- [센서 및 주행 영상 모음](https://determined-elderberry-389.notion.site/1518071df6014a47bc14f24956136105)

</br>

## 💁‍♀️ 프로젝트 소개

- **프로젝트 기간**

  - 2022.08.22 ~ 2022.10.07 (7주)

- **👨‍👧‍👧 팀원**

  - 6명 (주행팀 2명, 센서팀 2명, 모바일팀 2명)

- **기획 배경**

자율주행 자동차에 대한 기술연구가 진행되면 많은 사람들이 자동차를 공유하여 주차장 부족 문제를 해소할 수 있다는 기대에서 기획하였습니다. 

갑작스러운 상황에서도 센서를 활용하여 위험한 상황을 피하거나 대처하여 운전자가 없는 자동차를 구현하고 모바일 앱으로 택시를 호출할 수 있는 자율주행 택시 서비스 입니다.


</br>

## 🔧 주요 기능

### 🚗 모빌리티

- LiDAR, 카메라 센서를 활용하여 주변 물체 인식
- 자동 조향(3차 궤적함수) 및 속도조절(PID 제어기)
- 장애물 회피(Lattice Planner)
- 전방 자동차 거리 조절(Smart Cruise Control)

### 📱 모바일

- 회원 관리 (회원가입, 로그인, 마이페이지, 회원정보 수정 등)
- 도착지와 출발지 지정, 특정 위치 즐겨찾기
- 목적지까지 예상 거리, 요금, 경로 제공
- 택시 위치 실시간 조회
- 결제 및 후기 등록/관리
- 1:1 채팅 / 챗봇
- 자동차 관리
  - 관리자의 차량 정보 및 평가 목록 조회
  - 차량 운행시간 조정
  - 수입 금액을 조회

</br>

## 📒 주요 기술

`Mobility`

- ROS
- [Morai Simulation - Drive](https://www.morai.ai/ko/drive)
- Python (2.7.17)
- Ubuntu (18.04.6 LTS)
- Oracle VM VirtualBox

`Mobile`

- Android Studio
- Kotlin
- Naver Map API
- BootPay
- Firebase

`Cooperation Tools`

- GitLab
- Jira
- Notion
- Kakao Oven
- Figma

### 🖼 기술 스택 구조도

![image](https://user-images.githubusercontent.com/19484971/220055541-8c2e8766-38f5-41b6-b3d2-fbab5c4efaec.png)

</br>

## 📖 기술별 자료 정리

- [ROS](https://github.com/ii200400/IT_Skill_Question/tree/master/JobGroup/mobility/ROS)
- [인지(Cognition)](https://github.com/ii200400/IT_Skill_Question/tree/master/JobGroup/mobility/cognition)
- [판단(Judgment)](https://github.com/ii200400/IT_Skill_Question/tree/master/JobGroup/mobility/judgment)
- [제어(Control)](https://github.com/ii200400/IT_Skill_Question/tree/master/JobGroup/mobility/control)
- [모바일](./mobile.md)

</br>

## 👀 더 찾아보기

- [노션](https://www.notion.so/5a5568486fbd4730ab43569cce17472c)
