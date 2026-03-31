pipeline {
  agent any

    environment {
      IMAGE = "yogramming/traffic-analyzer"
        TAG = "${BUILD_NUMBER}"
    }

  stages {

    stage('Build Image') {
      steps {
        sh 'docker build -t $IMAGE:$TAG .'
      }
    }

    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(
              credentialsId: 'dockerhub-creds',
              usernameVariable: 'USER',
              passwordVariable: 'PASS'
              )]) {
          sh '''
            echo $PASS | docker login -u $USER --password-stdin
            docker push $IMAGE:$TAG
            '''
        }
      }
    }

    stage('Update K8s Repo') {
      steps {
        withCredentials([usernamePassword(
              credentialsId: 'github-creds',
              usernameVariable: 'GIT_USER',
              passwordVariable: 'GIT_PASS'
              )]) {
          sh '''
            rm -rf traffic-analyzer-k8s

            git clone https://$GIT_USER:$GIT_PASS@github.com/yogramming/traffic-analyzer-k8s.git
            cd traffic-analyzer-k8s

            git config user.name "jenkins"
            git config user.email "jenkins@local"

            sed -i "s|image: yogramming/traffic-analyzer:.*|image: yogramming/traffic-analyzer:${BUILD_NUMBER}|" deployment.yml

            git add .
            git commit -m "Update image to ${BUILD_NUMBER}" || echo "No changes"
            git push
            '''
        }
      }
    }

  }
}
