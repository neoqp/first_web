# first_web
cykor first website
address : http://184.73.53.253:5000/

1. flask를 사용하기로 결정 => dreamhack 에서 종종 보이던 프레임워크라서 비교적 익숙함.
2. 뼈대를 먼저 만듬 => home.html과 crud와 관련된 html 파일 생성
3. flask를 이용하여 로컬에서 실행이 되는지 확인
4. flask에서 render_template를 사용하여 html 파일 렌더링 => 안됨... => templates 폴더 안에 존재해야함 => 수정 후 작동 확인
5. windows에서 mysql 설치 후 flask와 연동 => 추후에 aws를 사용하고 linux에 mysql 을 설치함
  5-1. 기초적인 query 문법을 익힘
  5-2. flask에서 sql을 어떻게 사용할 수 있는 지 학습
6. methods=['GET','POST'] 와 같이 하나의 경로에 두 개 이상의 메서드를 사용하여 효율적인 관리를 할 수 있음을 알게됨
7. js를 하나도 사용하지 않아 공백을 입력하면 경고팝업을 띄우는 js코드 작성 => 파일로 만들지는 않고 html 파일 안에 작성
8. aws 인스턴트를 생성하여 ssh로 접속하여 git clone 후 run.py 실행 => 화면을 끄면 run.py도 꺼짐
  => python3 run.py
     Ctrl + Z
     bg
     disown -h

     lsof -i :5000
     sudo kill -9 <PID>
  => 이렇게 하면 소유권을 넘기고 화면을 꺼도 실행이 가능.
  
(만들고보니 되게 단순하지만 엄청난 삽질을 했습니다...ㅠㅠ)
end.
