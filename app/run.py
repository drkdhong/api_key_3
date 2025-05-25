import os
from app import create_app
app =create_app()

# local testing
#if __name__ == '__main__':
#    app.run(debug=True)

# render.com + local testing
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render가 포트 넘버 환경변수로 줍니다!
    app.run(host="0.0.0.0", port=port, debug=False)
 