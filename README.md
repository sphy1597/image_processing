
# 영상처리 프로젝트

## 개요
 동영상을 이미지 처리 기법들을 활용하여 애니메이션틱한 결과를 얻을 수 있도록 하는 프로젝트
![캡처](https://github.com/sphy1597/image_processing/blob/main/ouput/%EC%98%81%EC%83%81%EC%B2%98%EB%A6%AC%20%EA%B8%B0%EB%A7%90%20.png)
## 기능 및 특징
 일반적인 이미지 처리기법을 활용하여 동영상의 프레임마다 아래 기법들을 적용하여 영상을 변환하는 작업을 수행 
- **입력영상**: 배경이 복잡하지 않은 영상에 대해서 효과가 좋게 나타납니다.
- **Step1**: 임계값 처리로 수월하게 엣지를 찾을 수 있도록 전처리하는 과정으로 그레이스케일 변환을 합니다.
- **Step2**: 엣지를 부드럽게 찾기 위해서 미디안 블러 필터를 적용합니다.
- **Stpe3**: 임계값 처리를 통해 영상에서 그림에 해당하는 선을 찾습니다.
- **Step4**: 임계값 처리를 통해 검출한 경계선 영상의 잡티를 제거하여 깔끔한 영상으로 변환
- **Step5**: step1에서 그레이스케일로 변환한 영상을 색상을 입히고 위해서 다시 컬러 스케일로 변환
- **Step6**: 원본 영상의 색상을 애니메이션처럼 변환
- **Step7**: step5와 step6의 결과 영상을 합쳐 하나의 결과 영상으로 생성

## 기술적 정보
- **개발환경**: vscode, opencv
- **플랫폼**: window
- **언어**: Python
  

## 팀원  
- 심규철 : [GitHub](https://github.com/sphy1597)
- 최광혁 : [GitHub](https://github.com/806hyogi)
- 이동준


## 라이선스
이 프로젝트는 [MIT 라이선스](/path/to/license)를 따릅니다.
