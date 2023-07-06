import cv2

def Change_images_to_pictures():
  
    # 동영상 파일 경로 설정
    capture = cv2.VideoCapture('exmple.mp4')
    
    if not capture.isOpened():
        print("비디오를 재생할 수 없습니다.")
        return

    # 동영상 저장을 위한 설정
    fps = capture.get(cv2.CAP_PROP_FPS)
    
    # 가로, 세로 프레임 계산
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 인코딩 포멧 코드
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    # 동영상 저장을 위한 설정
    output = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

    # 동영상 프레임 단위로 읽음
    while True:
        ret, frame = capture.read() # 한프레임씩 읽음
        if not ret: # 프레임을 읽지봇하면 반복문 종료
            break
        
        # BGR형식의 이미지를 그레이스케일로 프레임변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 그레이스케일 이미지를 미디안 필터를 적용하여 블러처리
        blur = cv2.medianBlur(gray, 5)
        
        # 블러처리된 이미지에 적응 임계값 처리를 수행하여 edge를 감지
        edge = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1.5)
        
        # 그레이스케일 이미지를 RGB형식으로 변환
        edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
        
        # 스케일화된 이미지 생성
        style = cv2.stylization(frame, sigma_s=60, sigma_r=0.5)

        # 스케일화된 이미지를 AND연산으로 최종 이미지 생성
        result_Change_images_to_pictures= cv2.bitwise_and(style, edge)
        
        # 이미지 화면출력
        cv2.imshow("result", result_Change_images_to_pictures)
        
        # 영상 저장
        output.write(result_Change_images_to_pictures)

        # 'q' 버튼으로 영상 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 동영상 파일 닫음
    capture.release()
    output.release()
    
    cv2.destroyAllWindows()

# 결과물 함수 호출
Change_images_to_pictures() 
