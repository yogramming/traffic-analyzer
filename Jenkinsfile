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
                sh '''
                git clone https://github.com/yogramming/traffic-analyzer-k8s.git
                cd traffic-analyzer-k8s

                sed -i "s|image: .*|image: yogramming/traffic-analyzer:${BUILD_NUMBER}|" deployment.yaml

                git commit -am "Update image to ${BUILD_NUMBER}"
                git push
                '''
              }
          }
    }
}
