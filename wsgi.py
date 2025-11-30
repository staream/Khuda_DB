from .app import create_app # Flask 앱 생성 함수 가져오기
app = create_app() # Flask 앱 인스턴스 생성

if __name__ == "__main__": # 직접 실행 시 실행할 코드 조건
    app.run(debug=True, port=5005) # Flask 내장 서버 실행, 디버그 모드 켬(개발용)